import json
import urllib.parse


def unsafeStringify(x):
    return json.dumps(x)


def unsafeToFixed(digits):
    def n_(n):
        f = r"{:0." + str(digits) + r"f}"
        return f.format(n)

    return n_


def unsafeToExponential(digits):
    def n_(n):
        f = r"{:" + str(digits) + r"e}"
        return f.format(n)

    return n_


def unsafeToPrecision(digits):
    def n_(n):
        f = r"{:." + str(digits) + r"e}"
        return f.format(n)

    return n_


def unsafeDecodeURI(s):
    return urllib.parse.unquote(str, safe="~@#$&()*!+=:;,.?/'")


def unsafeEncodeURI(s):
    return urllib.parse.quote(str, safe="~@#$&()*!+=:;,.?/'")


def unsafeDecodeURIComponent(s):
    return urllib.parse.unquote(str, safe="~()*!.'")


def unsafeEncodeURIComponent(s):
    return urllib.parse.quote(str, safe="~()*!.'")
