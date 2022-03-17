# 数据库管理类
import tushare as ts
import pandas as pd
import datetime
import pymongo

class MongoManager(object):
    __instance = None

    daycol = None

    def __init__(self, *args, **kwargs):
        ts.set_token('872c53c263944f8e513a5096984af3b0fbbe55db6f2b785e36e94f42')
        pro = ts.pro_api()

        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        stockdb = myclient['stockdb']
        self.daycol = stockdb['daycol']
        dblist = myclient.list_database_names()
        if 'stockdb' in dblist:
            print('数据库已存在！')
        collist = stockdb.list_collection_names()
        if 'daycol' in collist:   # 判断 sites 集合是否存在
            print('集合已存在！')

    def __new__(cls, *args, **kwargs):
        if MongoManager.__instance is None:
            MongoManager.__instance = object.__new__(cls,*args, **kwargs)
        return MongoManager.__instance

    def getDaycol(self):
        return self.daycol

    # 下载数据
    def downLoadData(self, stock_code):
        time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
        end_dt = time_temp.strftime('%Y%m%d')
        df = self.pro.query('daily', ts_code = stock_code, start_date = '20180701', end_date = end_dt)

        df_records = df.to_dict('records')
        print(df_records)
        x = self.daycol.insert_many(df_records) 
        print(x)

    # 获取数据
    def getData(self):
        df = pd.DataFrame(columns = ["ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])

        for x in self.daycol.find():
            pd_data = pd.DataFrame.from_dict(x, orient = 'index').T
            df = pd.concat([df, pd_data], ignore_index = True)
        return df