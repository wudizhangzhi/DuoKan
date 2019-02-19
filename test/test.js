BinaryParser = function(t, e) {
        this.bigEndian = t,
        this.allowExceptions = e
    },
p = BinaryParser.prototype,
p.encodeInt = function(t, e) {
    var i = Math.pow(2, e)
      , n = [];
    for ((t >= i || -(i >> 1) > t) && this.warn("encodeInt::overflow") && (t = 0),
    0 > t && (t += i); t; n[n.length] = String.fromCharCode(t % 256),
    t = Math.floor(t / 256))
        ;
    for (e = -(-e >> 3) - n.length; e--; n[n.length] = "\0")
        ;
    return (this.bigEndian ? n.reverse() : n).join("")
}
,
p.decodeFloat = function(t, e, i) {
    var n, r, o, s = ((s = new this.Buffer(this.bigEndian,t)).checkBuffer(e + i + 1),
    s), a = Math.pow(2, i - 1) - 1, l = s.readBits(e + i, 1), c = s.readBits(e, i), u = 0, h = 2, d = s.buffer.length + (-e >> 3) - 1;
    do
        for (n = s.buffer[++d],
        r = e % 8 || 8,
        o = 1 << r; o >>= 1; n & o && (u += 1 / h),
        h *= 2)
            ;
    while (e -= r);return c == (a << 1) + 1 ? u ? 0 / 0 : l ? -1 / 0 : +1 / 0 : (1 + -2 * l) * (c || u ? c ? Math.pow(2, c - a) * (1 + u) : Math.pow(2, -a + 1) * u : 0)
}
,
p.decodeInt = function(t, e, i) {
    var n = new this.Buffer(this.bigEndian,t)
      , r = n.readBits(0, e)
      , o = Math.pow(2, e);
    return i && r >= o / 2 ? r - o : r
}
,

p = (p.Buffer = function(t, e){
    this.bigEndian = t || 0,
        this.buffer = [],
        this.setBuffer(e)
}).prototype,


    p.readBits = function(t, e) {
        function i(t, e) {
            for (++e; --e; t = 1073741824 == (1073741824 & (t %= 2147483648)) ? 2 * t : 2 * (t - 1073741824) + 2147483647 + 1)
                ;
            return t
        }
        if (0 > t || 0 >= e)
            return 0;
        this.checkBuffer(t + e);
        for (var n, r = t % 8, o = this.buffer.length - (t >> 3) - 1, s = this.buffer.length + (-(t + e) >> 3), a = o - s, l = (this.buffer[o] >> r & (1 << (a ? 8 - r : e)) - 1) + (a && (n = (t + e) % 8) ? (this.buffer[s++] & (1 << n) - 1) << (a-- << 3) - r : 0); a; l += i(this.buffer[s++], (a-- << 3) - r))
            ;
        return l
    }
    ,
    p.setBuffer = function(t) {
        if (t) {
            for (var e, i = e = t.length, n = this.buffer = Array(e); i; n[e - i] = t.charCodeAt(--i))
                ;
            this.bigEndian && n.reverse()
        }
    }
    ,
    p.hasNeededBits = function(t) {
        return this.buffer.length >= -(-t >> 3)
    }
    ,
    p.checkBuffer = function(t) {
        if (!this.hasNeededBits(t))
            throw Error("checkBuffer::missing bytes")
    }
    ;
p.warn = function(t) {
    if (this.allowExceptions)
        throw Error(t);
    return 1
}
,
p.toSmall = function(t) {
    return this.decodeInt(t, 8, !0)
}
,
p.fromSmall = function(t) {
    return this.encodeInt(t, 8, !0)
}
,
p.toByte = function(t) {
    return this.decodeInt(t, 8, !1)
}
,
p.fromByte = function(t) {
    return this.encodeInt(t, 8, !1)
}
,
p.toShort = function(t) {
    return this.decodeInt(t, 16, !0)
}
,
p.fromShort = function(t) {
    return this.encodeInt(t, 16, !0)
}
,
p.toWord = function(t) {
    return this.decodeInt(t, 16, !1)
}
,
p.fromWord = function(t) {
    return this.encodeInt(t, 16, !1)
}
,
p.toInt = function(t) {
    return this.decodeInt(t, 32, !0)
}
,
p.fromInt = function(t) {
    return this.encodeInt(t, 32, !0)
}
,
p.toDWord = function(t) {
    return this.decodeInt(t, 32, !1)
}
,
p.fromDWord = function(t) {
    return this.encodeInt(t, 32, !1)
}
,
p.toFloat = function(t) {
    return this.decodeFloat(t, 23, 8)
}
,
p.fromFloat = function(t) {
    return this.encodeFloat(t, 23, 8)
}
,
p.toDouble = function(t) {
    return this.decodeFloat(t, 52, 11)
}
,
p.fromDouble = function(t) {
    return this.encodeFloat(t, 52, 11)
}