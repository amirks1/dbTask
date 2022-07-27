import pandas as pd
import mysql.connector as conn
import pymongo
import json

mydb = conn.connect(host = "localhost" , user ="root"  )
cursor = mydb.cursor()
cursor.execute("use selldb;")

SQL_Query = pd.read_sql_query('select * from  attribute;', mydb)
df = pd.DataFrame(SQL_Query, columns=['Dress_ID', 'Style', 'Price','Rating','Size', 'Season', 'NeckLine', 'SleeveLength', 'waiseline', 'Material', 'FabricType', 'Decoration', 'Pattern_Type', 'Recommendation'])
print(df)

attribute_json = json.loads(df.to_json())
print(attribute_json)

SQL_Query = pd.read_sql_query('select * from  selldb.dress;', mydb)
df2 = pd.DataFrame(SQL_Query, columns=['Dress_ID', '29/8/2013', '31/8/2013', '09/02/2013', '09/04/2013', '09/06/2013', '09/08/2013', '09/10/2013', '09/12/2013', '14/9/2013', '16/9/2013', '18/9/2013', '20/9/2013', '22/9/2013', '24/9/2013', '26/9/2013', '28/9/2013', '30/9/2013', '10/02/2013', '10/04/2013', '10/06/2013', '10/08/2010', '10/10/2013', '10/12/2013'])
print(df2)

dress_json = json.loads(df2.to_json())
print(dress_json)

client = pymongo.MongoClient("mongodb+srv://amir:19c81u74@cluster0.rnwtb.mongodb.net/?retryWrites=true&w=majority")
#print(client.test)

database = client['dbsell']
collection = database["attribute"]
collection.insert_one(attribute_json)

collection2 = database["dress"]
collection2.insert_one(dress_json)