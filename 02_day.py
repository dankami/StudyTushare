import tushare as ts
import pandas as pd

import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb']
mycol = mydb['mycol']

dblist = myclient.list_database_names()
if 'mydb' in dblist:
    print('数据库已存在！')

collist = mydb.list_collection_names()
if 'mycol' in collist:   # 判断 sites 集合是否存在
    print('集合已存在！')

mydict = { "name": "RUNOOB1", "alexa": "10000", "url": "https://www.runoob.com1" }
x = mycol.insert_one(mydict) 
print(x)

for x in mycol.find():
    myquery = { "_id": x["_id"] }
    mycol.delete_one(myquery)

for x in mycol.find():
    print(x)

print('完成删除')

# ts.set_token('872c53c263944f8e513a5096984af3b0fbbe55db6f2b785e36e94f42')

# #显示所有列
# pd.set_option('display.max_columns', None)
# #显示所有行
# pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# # pd.set_option('max_colwidth',100)

# pro = ts.pro_api()

# df = pro.daily(ts_code='000300.SH', start_date='20210101', end_date='20220311')
# df = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20180701', end_date='20180718')
# df = pro.index_basic(market='SSE')

# print(df)