import pandas as pd
import mysql.connector as conn
import pymongo
import json

mydb = conn.connect(host = "localhost" , user ="root"  )
cursor = mydb.cursor()
#cursor.execute("select * from  selldb.attribute;")

SQL_Query = pd.read_sql_query('select * from  selldb.attribute;', mydb)
df = pd.DataFrame(SQL_Query, columns=['Dress_ID', 'Style', 'Price','Rating','Size', 'Season', 'NeckLine', 'SleeveLength', 'waiseline', 'Material', 'FabricType', 'Decoration', 'Pattern_Type', 'Recommendation'])
print(df)

#df.to_json('attribute.json')
attribute_json = pd.read_json('attribute.json')


SQL_Query = pd.read_sql_query('select * from  selldb.dress;', mydb)
df2 = pd.DataFrame(SQL_Query, columns=['Dress_ID', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23'])
print(df2)
dress_json = {}
dress_json = df2.to_json()
#dress_json = pd.read_json('dress.json')
print(dress_json)

client = pymongo.MongoClient("mongodb+srv://amir:19c81u74@cluster0.rnwtb.mongodb.net/?retryWrites=true&w=majority")
#print(client.test)

database = client['dbsell']
collection = database["attribute"]
#collection.insert_many(attribute_json)

collection2 = database["dress"]
collection2.insert_many(dress_json)