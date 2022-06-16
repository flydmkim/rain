import time
import sqlite3
import pymysql
import pandas as pd


bmi = pd.read_csv('./data/bmi.csv')
print(bmi)
print()
print(bmi.info())
print()

config = {
    'host' : '127.0.0.1' ,
    'user' : 'root' ,
    'password' : '1234' ,
    'database' : 'work' ,
    'port' : 3306 ,
    'charset' : 'utf8'
}

CN = pymysql.connect(**config)
cursor = CN.cursor()

sql ='''
create table if not exists bmi_tab(
height int  not null ,
weight int  not null ,
label text(15) not null
)
'''
cursor.execute(sql)
CN.commit()
print( 'bmi_tab 테이블 성공했습니다 ')

msg = "delete from bmi_tab "    #기존데이타 입력
cursor.execute(msg)
CN.commit()

height = bmi['height']
weight = bmi['weight']
label = bmi['label']

for k in range(200):
    h = height[k]
    w = weight[k]
    lb = label[k]

    msg = f"insert into bmi_tab values( {h}, {w}, '{lb}' ) "
    cursor.execute(msg)
    CN.commit()

print('bmi_tab 저장 성공 ============')

# 1. table추천  
'''
create table if not exists goods(
 code integer primary key,
 name text(20)  not null,
 su integer default 0,
 dan real default 0.0
)
''' 

'''
#마리아db 콘솔창에서 입력
create table goods(
 code integer primary key ,
 name text(20)  not null ,
 su integer default 0 ,
 dan real default 0.0 
);

''' 






