import mysql.connector as conn
import pandas as pd

mydb = conn.connect(host = "localhost" , user ="root"  )
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS selldb;")
#cursor.execute("DROP DATABASE attribute;")

s = "create table if not exists selldb.attribute(Dress_ID int(20), Style varchar(30), Price varchar(20),	Rating FLOAT(3),	Size varchar(10),	Season varchar(10),	NeckLine varchar(30),	SleeveLength varchar(30),	waiseline varchar(20),	Material varchar(20),	FabricType varchar(20),	Decoration varchar(20),	Pattern_Type varchar(20),	Recommendation int(1));"
s2 = "create table if not exists selldb.dress(Dress_ID int(20), c1 int(20),	c2 int(20),	c3 int(20),	c4 int(20),	c5 int(20),	c6 int(20),	c7 int(20),	c8 int(20),	c9 int(20),	c10 int(20),	c11 int(20),	c12 int(20),	c13 int(20),	c14 int(20),	c15 int(20),	c16 int(20),	c17 int(20),	c18 int(20),	c19 int(20),	c20 int(20),	c21 int(20),	c22 int(20),	c23 int(20));"

#s2 = cursor.execute("DROP table selldb.dress;")
q1 = cursor.execute(s)
q2= cursor.execute(s2)



df = pd.read_excel(r'C:\Users\dou\PycharmProjects\dress\Attribute DataSet.xlsx')
for index, row in df.iterrows():
    s3 = "insert into selldb.attribute(Dress_ID, Style, Price,	Rating,	Size, Season, NeckLine, SleeveLength, waiseline, Material, FabricType, Decoration, Pattern_Type, Recommendation)" \
         "values({},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{});".format(row['Dress_ID'],row['Style'],row['Price'],row['Rating'],row['Size'],row['Season'],row['NeckLine'],row['SleeveLength'],row['waiseline'],row['Material'],row['FabricType'],row['Decoration'],row['Pattern Type'],row['Recommendation'])
    cursor.execute(s3)
   # print(s3)

#s4 = cursor.execute("delete from selldb.attribute;")
#cursor.execute(s4)
mydb.commit()



