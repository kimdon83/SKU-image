# %% Load Modules

from datetime import datetime

import os
import pandas as pd
from sqlalchemy import create_engine
import smartsheet

from sqlalchemy.engine import URL
import pyodbc


# %%
import json

with open('data.json', 'r') as f:
    data = json.load(f)

# ID와 비밀번호 가져오기
server = data['server']
database = data['database']
username = data['username']
password = data['password']
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
print("Connection Established:")

# %%

smartsheet_client = smartsheet.Smartsheet(data['smartsheetAPI'])
smartsheet_client.Sheets.get_sheet_as_csv(
  data['sku_image_sheet'],           # sheet_id
  r'C:\Users\KISS Admin\Downloads')
# TODO: change above location if the location is not effective

# %% backup dim.mtrl_new
todays = datetime.today()

backup_df = pd.read_sql("""
SELECT * FROM sku_image
""", con=engine)
backup_df.to_csv(r"C:\Users\KISS Admin\Desktop\IVYENT_DH\Rq25. Image Sql\Product Photo"+todays.strftime("%Y-%m-%d")+".csv")

# %%
name_File = r"C:\Users\KISS Admin\Downloads\Product Photo.csv"
new_df = pd.read_csv(name_File)

new_df=new_df.loc[new_df["Material"].notnull()].copy()
b=pd.DataFrame(new_df["Material"])
sum(b.duplicated())
if sum(b.duplicated()) !=0:
  print("duplicated check please")

new_df.drop(0,inplace=True)
# %% upload to SQL
new_df.to_sql('sku_image', engine, schema = "dbo", if_exists='replace', index=False, chunksize=1000)

# %%
with engine.connect() as con:    
    con.execute("""DELETE FROM sku_image
WHERE material like '0000%';""")

old_name=r"C:\Users\KISS Admin\Downloads\Product Photo.csv"
os.remove(old_name)

# %%
