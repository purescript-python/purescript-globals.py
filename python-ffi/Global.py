import math
import urllib.parse as up


def _not_implemented_yet():
    raise NotImplementedError()


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


# exports.readInt = function (radix) {
#   return function (n) {
#     return parseInt(n, radix);
#   };
# };

readFloat = float
# exports.readFloat = parseFloat;

# var formatNumber = function (format) {
#   return function (fail, succ, digits, n) {
#     try {
#       return succ(n[format](digits));
#     }
#     catch (e) {
#       return fail(e.message);
#     }
#   };
# };

# exports._toFixed = formatNumber("toFixed");
# exports._toExponential = formatNumber("toExponential");
# exports._toPrecision = formatNumber("toPrecision");
_toFixed = _not_implemented_yet
_toExponential = _not_implemented_yet
_toPrecision = _not_implemented_yet


def encdecURI(encdec):
    def ap(fail, succ, s):
        try:
            return succ(encdec(s))
        except Exception as e:
            return fail(str(e))

    return ap


# var encdecURI = function (encdec) {
#   return function (fail, succ, s) {
#     try {
#       return succ(encdec(s));
#     }
#     catch (e) {
#       return fail(e.message);
#     }
#   };
# };

_decodeURI = _not_implemented_yet
_encodeURI = _not_implemented_yet
_decodeURIComponent = _not_implemented_yet
_encodeURIComponent = _not_implemented_yet

# exports._decodeURI = encdecURI(decodeURI);
# exports._encodeURI = encdecURI(encodeURI);
# exports._decodeURIComponent = encdecURI(decodeURIComponent);
# exports._encodeURIComponent = encdecURI(encodeURIComponent);
