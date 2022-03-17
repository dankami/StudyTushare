from IndexFunction import IndexFunction
import pandas as pd
from MongoManager import MongoManager

df = MongoManager().getData()

kdj_var = IndexFunction().kdj(df, 9)

print(type(kdj_var))