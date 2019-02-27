import re

import requests
import time
from base64 import b64decode
from dkbson import duokan_decode
from hashlib import md5
from lxml import etree
import os

from user_agent import generate_user_agent


def load_cookie(filepath):
    if not os.path.exists(filepath):
        raise Exception('找不到文件:%s' % filepath)
    cookie = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()
        content = ''.join(lines)
        for pair in content.split(';'):
            key, value = pair.strip().split('=')
            cookie[key] = value
    return cookie


class DuoKanBase(object):
    def __init__(self, cookies=None):
        self.sess = self.initSession()
        self.cookies = cookies
        # self.sess.cookies = self.cookies
        requests.utils.add_dict_to_cookiejar(self.sess.cookies, self.cookies)

    def initSession(self):
        sess = requests.Session()
        headers = {
            'User-Agent': generate_user_agent(os=('win',)),
        }
        sess.headers = headers
        sess.verify = False  # 关闭ssl验证
        return sess

    def _request(self, method, url, *args, **kwargs):
        if method.lower() == 'post':
            method = self.sess.post
        else:
            method = self.sess.get
        return method(url, *args, **kwargs)

    def _get(self, url, *args, **kwargs):
        return self._request('get', url, *args, **kwargs)

    def _post(self, url, *args, **kwargs):
        return self._request('post', url, *args, **kwargs)


class DuoKan(DuoKanBase):
    """

    过程:
        获取书信息 -> 获取书章节 -> 获取加密后的内容

    http://www.duokan.com/dk_id/api/xiaomi_web_reg
    https://account.xiaomi.com/pass/serviceLogin
    
    https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=1550050378157
    
    http://login.dushu.xiaomi.com/dk_id/api/checkin
    (返回的header中的location中有大部分需要的参数)
    Cookie: uLocale=zh_CN; userId=95331636; cUserId=ifDH-qSB3BgJ04o8wpU4a5sy_dc; userName=wud***com
    Host: login.dushu.xiaomi.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36
    [GET]
    followup: http://www.duokan.com/?app_id=web
    sign: ZTdkMmM5Njg3NTI5YjhlOGQzOGFkMDdiMzAxYzUwOTY=
    device_id: 
    wx_bind: 
    ticket: 0
    pwd: 1
    d: wb_0dfedab0-b776-4ea8-b491-1f82fb364ad7
    p_ts: 1550050438000
    fid: 0
    p_lm: 1
    auth: A52jtjoZgwfi+tc7/EOPUwuunhwCc8rTkxRkP+J9/d+kIMEhnFQDDQtYb4uf6FKrBPTvsQYCHZRBwJuWCcrHxdDPETfLbg9cPoSiTn/Bq1QWcWujfcrTGtNGJaL+GHtgTADTfPFfbZc+9xm5ER2/wagow0OAPMZrPzSfW7N3iJc=
    m: 1
    nonce: EZz0ooWvs7UBijK9
    _ssign: veWEh0ajGvOYF37z8+sFfTAR5SA=
    
    http://www.duokan.com/dk_id/api/web_reg_followup
    [GET]:
    auth: A52jtjoZgwfi+tc7/EOPUwuunhwCc8rTkxRkP+J9/d+kIMEhnFQDDQtYb4uf6FKrBPTvsQYCHZRBwJuWCcrHxdDPETfLbg9cPoSiTn/Bq1QWcWujfcrTGtNGJaL+GHtgTADTfPFfbZc+9xm5ER2/wagow0OAPMZrPzSfW7N3iJc=
    (从 http://login.dushu.xiaomi.com/dk_id/api/checkin 中的cookie的serviceToken获取)
    followup: http://www.duokan.com/?app_id=web
    sign: N2YwODI1N2JlNjZhNWRmODdjMzkxZDAxMTRlMGFjNDk=
    app_id: web
    t: 1550050438
    wx_bind: 
    
    
    获取书基本信息的接口(无需解密)
    http://www.duokan.com/store/v0/web/book/b64829f41e6d11e2ad8a00163e0123ac
    
    获取书信息的接口
    http://www.duokan.com/reader/book_info/b64829f41e6d11e2ad8a00163e0123ac/small?1550050792694
    
    Cookie: channel=49PXVQ; 
            device_id=D900YCKJTRI201FQ; 
            app_id=web; 
            Hm_lvt_1c932f22da573f2870e8ab565f4ff9cb=1550050341; 
            token=dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx; 
            user_id=95331636; 
            userId=dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx; 
            name=%E6%9C%88%E7%89%99%E5%A4%A9%E5%86%B2; 
            thumbnail=http%3A%2F%2Flxcdn.dl.files.xiaomi.net%2Fmfsv2%2Favatar%2Fs008%2Fp01ZFtVJsdZn%2FEMiGwDZ2fVK8RV.jpg; 
            last_uid=dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx; 
            last_user=95331636; 
            bdshare_firstime=1550050385360; reader_preference=horizontal; 
            store_noob=check; 
            Hm_lpvt_1c932f22da573f2870e8ab565f4ff9cb=1550050793
    Host: www.duokan.com
    Referer: http://www.duokan.com/reader/www/app.html?id=b64829f41e6d11e2ad8a00163e0123ac
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36
    X-Requested-With: XMLHttpRequest
    
    获取具体内容接口
    http://www.duokan.com/reader/page/b64829f41e6d11e2ad8a00163e0123ac/small954?trait=small&revision=undefined
    """

    def __init__(self, cookies=None):
        super(DuoKan, self).__init__(cookies)
        # 章节列表
        self.chapters = []
        self.current_page = 1  # 当前章节
        self.current_book_id = None  # 当前阅读的书籍

    def login(self, username, password):
        location = self.fetchXiaoMiWebReg()
        self.fetchServiceLogin(location)
        # serviceLoginAuth2
        # checkin

    def fetchXiaoMiWebReg(self):
        url = 'http://www.duokan.com/dk_id/api/xiaomi_web_reg?login=1&followup=http%3A%2F%2Fwww.duokan.com%2F%3Fapp_id%3Dweb'
        headers = {
            'Host': 'www.duokan.com',
            'Referer': 'http://www.duokan.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
        }
        ret = self._get(url, headers=headers, allow_redirects=False)
        location = ret.headers['Location']
        return location

    def fetchServiceLogin(self, location):
        headers = {
            'Host': 'account.xiaomi.com',
            'Referer': 'http://www.duokan.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
        }
        ret = self._get(location, headers=headers, allow_redirects=False)
        # print(ret.cookies.get_dict())

    def fetchServiceLoginAuth2(self, username, password, refer):
        url = 'https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=%s' % int(time.time() * 1000)
        headers = {
            'Host': 'account.xiaomi.com',
            'Referer': refer,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
        }
        # TODO 未知参数
        data = {
            '_json': 'true',
            'callback': 'http://login.dushu.xiaomi.com/dk_id/api/checkin?followup=http%3A%2F%2Fwww.duokan.com%2F%3Fapp_id%3Dweb&sign=ZTdkMmM5Njg3NTI5YjhlOGQzOGFkMDdiMzAxYzUwOTY=&device_id=&wx_bind=',
            'sid': 'reader',
            'qs': '%3Fcallback%3Dhttp%253A%252F%252Flogin.dushu.xiaomi.com%252Fdk_id%252Fapi%252Fcheckin%253Ffollowup%253Dhttp%25253A%25252F%25252Fwww.duokan.com%25252F%25253Fapp_id%25253Dweb%2526sign%253DZTdkMmM5Njg3NTI5YjhlOGQzOGFkMDdiMzAxYzUwOTY%253D%2526device_id%253D%2526wx_bind%253D%26sid%3Dreader',
            '_sign': 'yA9KQYrgGKt4hcw/DOU65tEbEmw=',
            'serviceParam': '{"checkSafePhone":false}',
            'user': username,
            'hash': md5(password.encode('utf8')).hexdigest(),  # 密码MD5
            'cc': '',
        }
        ret = self._get(url, headers=headers, data=data)
        # print(ret.cookies.get_dict())

    def fetchBookInfo(self, book_id):
        url = 'http://www.duokan.com/reader/book_info/%s/small?%s' % (book_id, int(time.time() * 100))

        headers = {
            'Host': 'www.duokan.com',
            'Referer': 'http://www.duokan.com/reader/www/app.html?id=b64829f41e6d11e2ad8a00163e0123ac',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # cookies = {
        #     'token': 'dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx',
        #     'device_id': 'D900YCKJTRI201FQ',
        #     'app_id': 'web',
        #     'user_id': '95331636',
        # 'channel': '49PXVQ',
        # 'Hm_lvt_1c932f22da573f2870e8ab565f4ff9cb': '1550050341',
        # 'last_uid': 'dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx',
        # 'last_user': '95331636',
        # 'userId': 'dIo8bgxs1Z_pkvlMQZCUZehbB7MAWqnu69vyr-MAmK2pSQoilYvJg9YeRcTiFOzx',
        # 'name': '%E6%9C%88%E7%89%99%E5%A4%A9%E5%86%B2',
        # 'thumbnail': 'http%3A%2F%2Flxcdn.dl.files.xiaomi.net%2Fmfsv2%2Favatar%2Fs008%2Fp01ZFtVJsdZn%2FEMiGwDZ2fVK8RV.jpg',
        # 'bdshare_firstime': '1550050385360',
        # 'reader_preference': 'horizontal',
        # 'store_noob': 'check',
        # 'Hm_lpvt_1c932f22da573f2870e8ab565f4ff9cb': '1550050793'
        # }
        ret = self._get(url, headers=headers, cookies=self.cookies)
        return duokan_decode(ret.text)

    def fetchPage(self, book_id, page_id):
        url = 'http://www.duokan.com/reader/page/%s/small%s?trait=small&revision=undefined' % (book_id, page_id)
        headers = {
            'Host': 'www.duokan.com',
            'Referer': 'http://www.duokan.com/reader/www/app.html?id=%s' % book_id,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        ret = self._get(url, headers=headers)
        return duokan_decode(ret.text)

    def fetchPageContent(self, book_id, page_id):
        """

        Args:
            book_id:
            page_id:

        Returns:

        """
        page_source_json = self.fetchPage(book_id, page_id)
        ret = self._get(page_source_json['url'])
        m = re.findall(r"duokan_page\('([^']+)'\)", ret.text)
        page_data = duokan_decode(m[0])
        return [(i['char'], i['pos']) for i in page_data['items'] if 'char' in i]

    def fetchMyBookList(self):
        """
        获取我的书架
        :return: 
        """
        # TODO
        url = 'http://www.duokan.com/u/mybook'
        ret = self._get(url)
        # print(ret.text)
        root = etree.HTML(ret.text)
        with open('test.html', 'wb') as f:
            f.write(ret.content)
        lis = root.xpath('//ul[@class="j-list"]/li')
        return lis

    def readBook(self, book_id):
        """
        开始阅读
        :param book_id: 
        :return: 
        """
        self.current_book_id = book_id
        self.fetchPageContent(book_id=book_id, page_id=self.current_page)

        # duokanview = DuokanMenu(self)
        # duokanview.set_items()
        # duokanview.listen()

    def run(self):
        """
        开始阅读
        
        login
        获取书列表
        init a view
        设置显示
        choose a book
        read page by page
        
        Args:
            book_id:

        Returns:

        """

        books = self.fetchMyBookList()
        # print(books)
        # duokanview = DuokanMenu(self)
        # duokanview.set_items(books)
        # duokanview.listen()


if __name__ == "__main__":
    """
    init a view
    login
    start a book
    read page by page
    """
    # duokan = DuoKan()
    # duokan.login('', '')
    # duokan.fetchBookInfo('b64829f41e6d11e2ad8a00163e0123ac')
    book_id = '7e2a574ab76e478996e48609fd86bb2e'
    cookie = load_cookie('cookie.txt')
    duokan = DuoKan(cookie)
    # duokan.run()
    # ret = duokan.fetchPageContent(book_id, 10)
    # ret = duokan.fetchMyBookList()
    # print(ret)
    ret = duokan.fetchPageContent(book_id, 42)
    print(''.join([i[0] for i in ret]))
