import sqlite3
import csv
import sys

#to create sqlite3 databsae

con=sqlite3.connect("nba.db")
cur=con.cursor()
drop="DROP TABLE IF EXISTS nba"

#SQL code to create nba table inside database

sql="""
    CREATE TABLE nba (
        SL INTEGER PRIMARY KEY,
        Date VARCHAR(100),
        Start VARCHAR(100),
        Visitor VARCHAR(100),
        PTS INTEGER,
        Home VARCHAR(100),
        PTS1 INTEGER,
        Unnamed6 VARCHAR(100),
        Unnamed7 VARCHAR(100),
        Attend VARCHAR(100),
        Notes VARCHAR(100)
        )"""
cur.execute(drop)
cur.execute(sql)
print("Database created")
con.commit()

inFile = sys.argv[1]

#to read files from csv 

csv_file = open(inFile,'r')
csv_reader = csv.reader(csv_file)
next(csv_reader)
num=0

#to push data from csv to nba table

for row in csv_reader:
    cur.execute("INSERT INTO nba VALUES(?,?,?,?,?,?,?,?,?,?,?)", row)
    con.commit()
    num+=1
con.close()
print(num," records transfered")