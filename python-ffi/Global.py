import math
import urllib.parse


nan = math.nan
isNaN = math.isnan


infinity = math.inf
isFinite = math.isfinite


def readInt(radix):
    def ap(n):
        try:
            return int(n, base=radix)
        except ValueError:
            return math.nan

    return ap


readFloat = float


def formatNumber(fmt):
    def ap(fail, succ, digits, n):
        try:
            return succ(n[format](digits))
        except Exception as e:
            return fail(str(e))

    return ap


_toFixed = formatNumber("toFixed")
_toExponential = formatNumber("toExponential")
_toPrecision = formatNumber("toPrecision")


def encdecURI(encdec):
    def ap(fail, succ, s):
        try:
            return succ(encdec(s))
        except Exception as e:
            return fail(str(e))

    return ap


_decodeURI = encdecURI(decodeURI)
_encodeURI = encdecURI(encodeURI)
_decodeURIComponent = encdecURI(decodeURIComponent)
_encodeURIComponent = encdecURI(encodeURIComponent)


def decodeURI(s):
    return urllib.parse.unquote(str, safe="~@#$&()*!+=:;,.?/'")


def encodeURI(s):
    return urllib.parse.quote(str, safe="~@#$&()*!+=:;,.?/'")


def decodeURIComponent(s):
    return urllib.parse.unquote(str, safe="~()*!.'")


def encodeURIComponent(s):
    return urllib.parse.quote(str, safe="~()*!.'")
