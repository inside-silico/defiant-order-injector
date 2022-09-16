from config import *
from sqlalchemy import create_engine
from PyOBD import *
import pandas as pd
import time

PyOBD=openBYMAdata()

if PyOBD.isworkingDay()==False:
    exit()

engine = create_engine("mysql+pymysql://{user}:{pw}@{db_host}:{port}/{db}"
                .format(user=db_usr,pw=db_pass,db_host=db_host,
                    db=quots_db,port=db_port,auth_plugin='mysql_native_password',))
time_sleep=4
now = "10"
while now!="17":
    PyOBD=openBYMAdata()
    PyOBD.get_bonds().drop(["expiration"],axis=1).to_sql("bonds_48hs",con=engine,if_exists="replace")
    print("bonds_df")
    time.sleep(time_sleep)
    
    PyOBD.get_bonds().to_sql("bluechips_48hs",con=engine,if_exists="replace")
    print("bluechips_dF")
    time.sleep(time_sleep)

    PyOBD.get_galpones().to_sql("galpones_48hs",con=engine,if_exists="replace")
    print("galpones_dF")
    time.sleep(time_sleep)

    PyOBD.get_cedears().to_sql("cedear_48hs",con=engine,if_exists="replace")
    print("cedear_df")
    time.sleep(time_sleep)
    

    now = time.strftime("%H")
