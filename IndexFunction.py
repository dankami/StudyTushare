# 技术指标类

class IndexFunction(object):
    __instance = None

    daycol = None

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if IndexFunction.__instance is None:
            IndexFunction.__instance = object.__new__(cls,*args, **kwargs)
        return IndexFunction.__instance

    def kdj(self):
        return 

    def rsi(self, stock_code):
        return

    def macd(self):
        return