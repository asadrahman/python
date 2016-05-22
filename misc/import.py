from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

import xlrd

DB_NAME = 'company_boss'

cnx = mysql.connector.connect(user='boss', password='boss', database=DB_NAME)
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_timesheet= ( "INSERT INTO time_sheet "
                 "( time_sheet_id, USERID, NAME, PROJECT_NO, PROJECT_NAME, YYYYMMDD, HOURS, NO, APPROVER, ONSITE, OFFSITE) "
                 "VALUES ( NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

data_timesheet = ( 'BA9574', 'Asad Rahman',    '20016945',    'MCRRT', '2016/01/04', '7.5','1','E41766','0','1')



# Create a database if it doesn't exist
try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


def open_file(path):
    book = xlrd.open_workbook(path)
 
    # print number of sheets
    print(book.nsheets)
 
    # print sheet names
    print(book.sheet_names())
 
    # get the first worksheet
    first_sheet = book.sheet_by_index(0)
 
    # read a row
    print(first_sheet.row_values(1))
 
    # read a cell
    cell = first_sheet.cell(0,0)
    print(cell)
    print(cell.value)
 
    # read a row slice
    print(first_sheet.row_slice(rowx=0, start_colx=0, end_colx=2))

    return first_sheet

#for name, ddl in DDL_INSERT.items():
path = "C:/Users/Rahman/Documents/WorkArea/MySQL/company_boss/Asad Rahman - Timesheet - January 2016.xlsx"
first_sheet = open_file(path)

first_row = [] # The row where we stock the name of the column
for col in range(first_sheet.ncols):
    first_row.append( first_sheet.cell_value(0,col) )
# tronsform the workbook to a list of dictionnary
data =[]
for row in range(1, first_sheet.nrows):
    
    elm = {}
    for col in range(first_sheet.ncols):
        if first_row[col] == 'DATE':
           date_obj = datetime(*xlrd.xldate_as_tuple(first_sheet.cell_value(row,col), 0))
           date = date_obj.strftime('%Y%m%d')
           elm[first_row[col]] = date
        else :
            elm[first_row[col]]=first_sheet.cell_value(row,col)
    data.append(elm)
#print (data)

for variable in data:
    print(variable)

counter = 1
#while True:
#    counter+=1
#    # read a row
#    print(first_sheet.row_values(counter))
#    data_timesheet = first_sheet.row_values(counter)
#    
#    try:
#        print("Inserting data {}: ")
#        cursor.execute(add_timesheet, data_timesheet)
#    except mysql.connector.Error as err:
#        print(err.msg)
#    else:
#        print("OK")
#    
#    cell = first_sheet.cell(counter,0)
#    print(cell.value)
#    
#    if cell.value != 'BA9574' :
#        break
#    try:
#        print("Inserting data {}: ".format(name), end='')
#        cursor.execute(ddl)
#    except mysql.connector.Error as err:
#        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#            print(err.msg)
#    else:
#        print("OK")
#
#
#try:
#    print("Inserting data {}: ")
#    cursor.execute(add_timesheet, data_timesheet)
#except mysql.connector.Error as err:
#    print(err.msg)
#else:
#    print("OK")

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()

input('Press any key to continue...')