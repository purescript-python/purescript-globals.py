import json
import urllib.parse


def unsafeStringify(x):
    return json.dumps(x)


def unsafeToFixed(digits):
    def n_(n):
        f = r"{:" + str(n) + "." + str(n) + r"f}"
        return f.format(n)

    return n_


def unsafeToExponential(digits):
    def n_(n):
        f = r"{:" + str(n) + "." + str(n) + r"e}"
        return f.format(n)

    return n_


def unsafeToPrecision(digits):
    def n_(n):
        f = r"{:." + str(n) + r"e}"
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

