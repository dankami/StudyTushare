import pandas as pd
from MongoManager import MongoManager

dayCol = MongoManager().getDaycol()

df = pd.DataFrame(columns = ["ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])

for x in dayCol.find():
    pd_data = pd.DataFrame.from_dict(x, orient = 'index').T
    df = df.append(pd_data, ignore_index = True)  
