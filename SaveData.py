import tushare as ts
import datetime
from MongoManager import MongoManager


##### 获取数据 #####
ts.set_token('872c53c263944f8e513a5096984af3b0fbbe55db6f2b785e36e94f42')
pro = ts.pro_api()
stock_code = '000001.SZ'
time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
end_dt = time_temp.strftime('%Y%m%d')
df = pro.query('daily', ts_code = stock_code, start_date = '20180701', end_date = end_dt)
print(df)

##### 保存数据 #####
# daycol = MongoManager().getDaycol()
# df_records = df.to_dict('records')
# print(df_records)
# x = daycol.insert_many(df_records) 

#获取20200101至今所有有交易的日期
# time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
# end_dt = time_temp.strftime('%Y%m%d')
# print(end_dt)
# trade_cal_df = pro.trade_cal(exchange='SSE', is_open='1', start_date='20210101', end_date=end_dt, fields='cal_date')
# print(trade_cal_df)

# mydict = { "name": "RUNOOB1", "alexa": "10000", "url": "https://www.runoob.com1" }
# x = mycol.insert_one(mydict) 
# print(x)

# for x in mycol.find():
#     myquery = { "_id": x["_id"] }
#     mycol.delete_one(myquery)

# for x in mycol.find():
#     print(x)

# print('完成删除')

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