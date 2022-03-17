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

    def kdj(self, df, t):
        # print('收盘：%d'%(df[0].close))
        print(df)
        print(df.close[0])
        # 1
        close = 0
        nlow = 0
        nheight = 0
        rsv = (close - nlow)/(nheight-nlow)
        # 2
        k = 2/3 * 50 + 1/3 * rsv
        d = 2/3 * 50 + 1/3 * k
        j = 3 * k - 2 * d

        return 1, 2, 3

    def rsi(self, stock_code):
        return

    def macd(self):
        return