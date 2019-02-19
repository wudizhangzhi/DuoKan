__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
def PyJs_LONG_11_(var=var):
    @Js
    def PyJs_anonymous_0_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'e'])
        PyJsComma(var.get(u"this").put('bigEndian', var.get('t')),var.get(u"this").put('allowExceptions', var.get('e')))
    PyJs_anonymous_0_._set_name('anonymous')
    @Js
    def PyJs_anonymous_1_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'e', 'n', 't'])
        var.put('i', var.get('Math').callprop('pow', Js(2.0), var.get('e')))
        var.put('n', Js([]))
        #for JS loop
        PyJsComma(((((var.get('t')>=var.get('i')) or ((-(var.get('i')>>Js(1.0)))>var.get('t'))) and var.get(u"this").callprop('warn', Js('encodeInt::overflow'))) and var.put('t', Js(0.0))),((Js(0.0)>var.get('t')) and var.put('t', var.get('i'), '+')))
        while var.get('t'):
            try:
                pass
            finally:
                    PyJsComma(var.get('n').put(var.get('n').get('length'), var.get('String').callprop('fromCharCode', (var.get('t')%Js(256.0)))),var.put('t', var.get('Math').callprop('floor', (var.get('t')/Js(256.0)))))
        #for JS loop
        var.put('e', ((-((-var.get('e'))>>Js(3.0)))-var.get('n').get('length')))
        while (var.put('e',Js(var.get('e').to_number())-Js(1))+Js(1)):
            try:
                pass
            finally:
                    var.get('n').put(var.get('n').get('length'), Js('\x00'))
        return (var.get('n').callprop('reverse') if var.get(u"this").get('bigEndian') else var.get('n')).callprop('join', Js(''))
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_2_(t, e, i, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'h', 'd', 'a', 'i', 's', 't', 'o', 'n', 'c', 'u', 'l', 'e'])
        var.put('s', PyJsComma(var.put('s', var.get(u"this").get('Buffer').create(var.get(u"this").get('bigEndian'), var.get('t'))).callprop('checkBuffer', ((var.get('e')+var.get('i'))+Js(1.0))),var.get('s')))
        var.put('a', (var.get('Math').callprop('pow', Js(2.0), (var.get('i')-Js(1.0)))-Js(1.0)))
        var.put('l', var.get('s').callprop('readBits', (var.get('e')+var.get('i')), Js(1.0)))
        var.put('c', var.get('s').callprop('readBits', var.get('e'), var.get('i')))
        var.put('u', Js(0.0))
        var.put('h', Js(2.0))
        var.put('d', ((var.get('s').get('buffer').get('length')+((-var.get('e'))>>Js(3.0)))-Js(1.0)))
        while 1:
            #for JS loop
            PyJsComma(PyJsComma(var.put('n', var.get('s').get('buffer').get(var.put('d',Js(var.get('d').to_number())+Js(1)))),var.put('r', ((var.get('e')%Js(8.0)) or Js(8.0)))),var.put('o', (Js(1.0)<<var.get('r'))))
            while var.put('o', Js(1.0), '>>'):
                try:
                    pass
                finally:
                        PyJsComma(((var.get('n')&var.get('o')) and var.put('u', (Js(1.0)/var.get('h')), '+')),var.put('h', Js(2.0), '*'))
            if not var.put('e', var.get('r'), '-'):
                break
        def PyJs_LONG_3_(var=var):
            return (((Js(0.0)/Js(0.0)) if var.get('u') else (((-Js(1.0))/Js(0.0)) if var.get('l') else ((+Js(1.0))/Js(0.0)))) if (var.get('c')==((var.get('a')<<Js(1.0))+Js(1.0))) else ((Js(1.0)+((-Js(2.0))*var.get('l')))*(((var.get('Math').callprop('pow', Js(2.0), (var.get('c')-var.get('a')))*(Js(1.0)+var.get('u'))) if var.get('c') else (var.get('Math').callprop('pow', Js(2.0), ((-var.get('a'))+Js(1.0)))*var.get('u'))) if (var.get('c') or var.get('u')) else Js(0.0))))
        return PyJs_LONG_3_()
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(t, e, i, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 't', 'o', 'n', 'i', 'e'])
        var.put('n', var.get(u"this").get('Buffer').create(var.get(u"this").get('bigEndian'), var.get('t')))
        var.put('r', var.get('n').callprop('readBits', Js(0.0), var.get('e')))
        var.put('o', var.get('Math').callprop('pow', Js(2.0), var.get('e')))
        return ((var.get('r')-var.get('o')) if (var.get('i') and (var.get('r')>=(var.get('o')/Js(2.0)))) else var.get('r'))
    PyJs_anonymous_4_._set_name('anonymous')
    @Js
    def PyJs_anonymous_5_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'e'])
        PyJsComma(PyJsComma(var.get(u"this").put('bigEndian', (var.get('t') or Js(0.0))),var.get(u"this").put('buffer', Js([]))),var.get(u"this").callprop('setBuffer', var.get('e')))
    PyJs_anonymous_5_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(t, e, this, arguments, var=var):
        var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'l', 'a', 's', 't', 'o', 'n', 'i', 'e'])
        @Js
        def PyJsHoisted_i_(t, e, this, arguments, var=var):
            var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'e'])
            #for JS loop
            var.put('e',Js(var.get('e').to_number())+Js(1))
            while var.put('e',Js(var.get('e').to_number())-Js(1)):
                try:
                    pass
                finally:
                        var.put('t', ((Js(2.0)*var.get('t')) if (Js(1073741824.0)==(Js(1073741824.0)&var.put('t', Js(2147483648.0), '%'))) else (((Js(2.0)*(var.get('t')-Js(1073741824.0)))+Js(2147483647.0))+Js(1.0))))
            return var.get('t')
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        pass
        if ((Js(0.0)>var.get('t')) or (Js(0.0)>=var.get('e'))):
            return Js(0.0)
        var.get(u"this").callprop('checkBuffer', (var.get('t')+var.get('e')))
        #for JS loop
        var.put('r', (var.get('t')%Js(8.0)))
        var.put('o', ((var.get(u"this").get('buffer').get('length')-(var.get('t')>>Js(3.0)))-Js(1.0)))
        var.put('s', (var.get(u"this").get('buffer').get('length')+((-(var.get('t')+var.get('e')))>>Js(3.0))))
        var.put('a', (var.get('o')-var.get('s')))
        def PyJs_LONG_7_(var=var):
            return (((var.get(u"this").get('buffer').get(var.get('o'))>>var.get('r'))&((Js(1.0)<<((Js(8.0)-var.get('r')) if var.get('a') else var.get('e')))-Js(1.0)))+(((var.get(u"this").get('buffer').get((var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1)))&((Js(1.0)<<var.get('n'))-Js(1.0)))<<(((var.put('a',Js(var.get('a').to_number())-Js(1))+Js(1))<<Js(3.0))-var.get('r'))) if (var.get('a') and var.put('n', ((var.get('t')+var.get('e'))%Js(8.0)))) else Js(0.0)))
        var.put('l', PyJs_LONG_7_())
        while var.get('a'):
            try:
                pass
            finally:
                    var.put('l', var.get('i')(var.get(u"this").get('buffer').get((var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))), (((var.put('a',Js(var.get('a').to_number())-Js(1))+Js(1))<<Js(3.0))-var.get('r'))), '+')
        return var.get('l')
    PyJs_anonymous_6_._set_name('anonymous')
    @Js
    def PyJs_anonymous_8_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'e', 'n', 't'])
        if var.get('t'):
            #for JS loop
            var.put('i', var.put('e', var.get('t').get('length')))
            var.put('n', var.get(u"this").put('buffer', var.get('Array')(var.get('e'))))
            while var.get('i'):
                try:
                    pass
                finally:
                        var.get('n').put((var.get('e')-var.get('i')), var.get('t').callprop('charCodeAt', var.put('i',Js(var.get('i').to_number())-Js(1))))
            (var.get(u"this").get('bigEndian') and var.get('n').callprop('reverse'))
    PyJs_anonymous_8_._set_name('anonymous')
    @Js
    def PyJs_anonymous_9_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return (var.get(u"this").get('buffer').get('length')>=(-((-var.get('t'))>>Js(3.0))))
    PyJs_anonymous_9_._set_name('anonymous')
    @Js
    def PyJs_anonymous_10_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        if var.get(u"this").callprop('hasNeededBits', var.get('t')).neg():
            PyJsTempException = JsToPyException(var.get('Error')(Js('checkBuffer::missing bytes')))
            raise PyJsTempException
    PyJs_anonymous_10_._set_name('anonymous')
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('BinaryParser', PyJs_anonymous_0_),var.put('p', var.get('BinaryParser').get('prototype'))),var.get('p').put('encodeInt', PyJs_anonymous_1_)),var.get('p').put('decodeFloat', PyJs_anonymous_2_)),var.get('p').put('decodeInt', PyJs_anonymous_4_)),var.put('p', var.get('p').put('Buffer', PyJs_anonymous_5_).get('prototype'))),var.get('p').put('readBits', PyJs_anonymous_6_)),var.get('p').put('setBuffer', PyJs_anonymous_8_)),var.get('p').put('hasNeededBits', PyJs_anonymous_9_)),var.get('p').put('checkBuffer', PyJs_anonymous_10_))
PyJs_LONG_11_()
def PyJs_LONG_29_(var=var):
    @Js
    def PyJs_anonymous_12_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        if var.get(u"this").get('allowExceptions'):
            PyJsTempException = JsToPyException(var.get('Error')(var.get('t')))
            raise PyJsTempException
        return Js(1.0)
    PyJs_anonymous_12_._set_name('anonymous')
    @Js
    def PyJs_anonymous_13_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(8.0), Js(0.0).neg())
    PyJs_anonymous_13_._set_name('anonymous')
    @Js
    def PyJs_anonymous_14_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(8.0), Js(0.0).neg())
    PyJs_anonymous_14_._set_name('anonymous')
    @Js
    def PyJs_anonymous_15_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(8.0), Js(1.0).neg())
    PyJs_anonymous_15_._set_name('anonymous')
    @Js
    def PyJs_anonymous_16_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(8.0), Js(1.0).neg())
    PyJs_anonymous_16_._set_name('anonymous')
    @Js
    def PyJs_anonymous_17_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(16.0), Js(0.0).neg())
    PyJs_anonymous_17_._set_name('anonymous')
    @Js
    def PyJs_anonymous_18_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(16.0), Js(0.0).neg())
    PyJs_anonymous_18_._set_name('anonymous')
    @Js
    def PyJs_anonymous_19_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(16.0), Js(1.0).neg())
    PyJs_anonymous_19_._set_name('anonymous')
    @Js
    def PyJs_anonymous_20_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(16.0), Js(1.0).neg())
    PyJs_anonymous_20_._set_name('anonymous')
    @Js
    def PyJs_anonymous_21_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(32.0), Js(0.0).neg())
    PyJs_anonymous_21_._set_name('anonymous')
    @Js
    def PyJs_anonymous_22_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(32.0), Js(0.0).neg())
    PyJs_anonymous_22_._set_name('anonymous')
    @Js
    def PyJs_anonymous_23_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeInt', var.get('t'), Js(32.0), Js(1.0).neg())
    PyJs_anonymous_23_._set_name('anonymous')
    @Js
    def PyJs_anonymous_24_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeInt', var.get('t'), Js(32.0), Js(1.0).neg())
    PyJs_anonymous_24_._set_name('anonymous')
    @Js
    def PyJs_anonymous_25_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeFloat', var.get('t'), Js(23.0), Js(8.0))
    PyJs_anonymous_25_._set_name('anonymous')
    @Js
    def PyJs_anonymous_26_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeFloat', var.get('t'), Js(23.0), Js(8.0))
    PyJs_anonymous_26_._set_name('anonymous')
    @Js
    def PyJs_anonymous_27_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('decodeFloat', var.get('t'), Js(52.0), Js(11.0))
    PyJs_anonymous_27_._set_name('anonymous')
    @Js
    def PyJs_anonymous_28_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['t'])
        return var.get(u"this").callprop('encodeFloat', var.get('t'), Js(52.0), Js(11.0))
    PyJs_anonymous_28_._set_name('anonymous')
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('p').put('warn', PyJs_anonymous_12_),var.get('p').put('toSmall', PyJs_anonymous_13_)),var.get('p').put('fromSmall', PyJs_anonymous_14_)),var.get('p').put('toByte', PyJs_anonymous_15_)),var.get('p').put('fromByte', PyJs_anonymous_16_)),var.get('p').put('toShort', PyJs_anonymous_17_)),var.get('p').put('fromShort', PyJs_anonymous_18_)),var.get('p').put('toWord', PyJs_anonymous_19_)),var.get('p').put('fromWord', PyJs_anonymous_20_)),var.get('p').put('toInt', PyJs_anonymous_21_)),var.get('p').put('fromInt', PyJs_anonymous_22_)),var.get('p').put('toDWord', PyJs_anonymous_23_)),var.get('p').put('fromDWord', PyJs_anonymous_24_)),var.get('p').put('toFloat', PyJs_anonymous_25_)),var.get('p').put('fromFloat', PyJs_anonymous_26_)),var.get('p').put('toDouble', PyJs_anonymous_27_)),var.get('p').put('fromDouble', PyJs_anonymous_28_))
PyJs_LONG_29_()


# Add lib to the module scope
example = var.to_python()