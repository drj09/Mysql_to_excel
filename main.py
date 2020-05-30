import mysql.connector as mysql
from openpyxl import Workbook


def data_prep(structure,data):
    data.insert(0,[i[0] for i in structure])
    return data

def push_data(data,tb_name):
    try:    
        wb = Workbook()  
        sheet = wb.active      
        for i in data:  
            print(i)
            sheet.append(i)  
        wb.save(f"{tb_name}.xlsx")  
    except Exception as err:
        print(err)
        exit()

def sql_init(host,user,password,db):
    try:
        conn=mysql.connect(host=host,user=user,passwd=password,database=db)
        return conn
    except Exception as err:
        print("error occured --> ",err)
        exit()


def sql_query(conn,query):
    cursor=conn.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    return records


db_name=input('## Enter database name : ')
conn=sql_init('localhost','root','',db_name)
tb_name=input('## Enter table name : ')
structure=sql_query(conn,f'show columns from {tb_name}')
#print(structure)
data=sql_query(conn,'select * from blending_s')
#print(data)
data=data_prep(structure,data)

push_data(data,tb_name)

#sql_query(conn,'select * from datarefresh')


"""
db_name=input("Enter Database Name")
table_name=input("Enter Table Name")
file_path=input("Enter path where excel sheet is to be save")

"""


#get data from database
#export it into excel file