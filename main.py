import mysql.connector as mysql
from openpyxl import Workbook

#initializing connection to Mysql host
def sql_init(host,user,password,db):
    try:
        conn=mysql.connect(host=host,user=user,passwd=password,database=db)
        return conn
    except Exception as err:
        print("error occured --> ",err)
        exit()

#function to execute sql queries 
def sql_query(conn,query):
    cursor=conn.cursor()
    cursor.execute(query)
    records=cursor.fetchall()
    return records

#inserting column_names into data
def data_prep(structure,data):
    data.insert(0,[i[0] for i in structure])
    return data

#Exporting excel_sheet
def push_data(data,tb_name):
    try:    
        wb = Workbook()  
        sheet = wb.active      
        for i in data:  
            print(i)
            sheet.append(i)  
        wb.save(f"{tb_name}.xlsx")
        print('## Export Finished ##')  
    except Exception as err:
        print(err)
        exit()

#main function
def main():
    db_name=input('## Enter database name : ')
    conn=sql_init('localhost','root','',db_name)
    tb_name=input('## Enter table name : ')
    structure=sql_query(conn,f'show columns from {tb_name}')
    data=sql_query(conn,f'select * from {tb_name}')
    data=data_prep(structure,data)
    push_data(data,tb_name)

if __name__ == "__main__":
    main()