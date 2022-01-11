from os import listdir
import sqlite3 as sql
import csv

# vars
files = []

def process_file(filePath):
    items = []
    isHeader = True
    # read CSV
    with open(filePath) as dataFile:
        # read the file
        reader = csv.reader(dataFile)
        
        # print each row
        for row in reader:        
            if isHeader: #skip Header
                isHeader = False
            else:
                # print(row)
                items.append([row[1],row[2],row[3],row[4],row[5]])
                

    # connect to Database and insert records
    con = sql.connect('test.db')
    cursor = con.cursor();

    # insert data
    cursor.executemany("INSERT INTO TEST (FIRST_NAME,LAST_NAME,EMAIL,CAR_MODEL,CAR_YEAR)VALUES(?,?,?,?,?)",items)

    # while i > 0:
        # cursor.execute("INSERT INTO TEST(NAME,SCHOOL)VALUES('ELIZABETH','CULTURAL')")
        # i = i-1
    con.commit()

    # cursor.execute("SELECT * FROM TEST")
    # for item in cursor.fetchall():
        # print(item)
        

#read all files on folder; we do this using listdir
files = [listdir("./data_sample/")]
for f in files[0]:
    process_file("./data_sample/" + f)
    