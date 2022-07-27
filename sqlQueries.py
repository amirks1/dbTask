import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root")
cursor = mydb.cursor()
cursor.execute("use selldb;")
cursor.execute("select * from attribute a left join dress d on a.Dress_ID = d.Dress_ID ;")

print(cursor.fetchall())

cursor.execute("SELECT count(DISTINCT Dress_ID) from dress")
print(cursor.fetchall())

cursor.execute("SELECT count(DISTINCT Dress_ID) from attribute where recommendation = 0")
print(cursor.fetchall())

cursor.execute("SELECT COALESCE(c1,0) + COALESCE(c2,0) + COALESCE(c3,0) + COALESCE(c4,0) + COALESCE(c5,0) + COALESCE(c6,0) + COALESCE(c7,0) + COALESCE(c8,0) + COALESCE(c9,0) + COALESCE(c10,0) + COALESCE(c11,0) + COALESCE(c12,0) + COALESCE(c13,0) + COALESCE(c14,0) + COALESCE(c15,0) + COALESCE(c16,0) + COALESCE(c17,0) + COALESCE(c18,0) + COALESCE(c19,0) + COALESCE(c20,0) + COALESCE(c21,0) + COALESCE(c22,0) + COALESCE(c23,0) as sum FROM `dress` ")
print(cursor.fetchall())

cursor.execute("SELECT COALESCE(c1,0) + COALESCE(c2,0) + COALESCE(c3,0) + COALESCE(c4,0) + COALESCE(c5,0) + COALESCE(c6,0) + COALESCE(c7,0) + COALESCE(c8,0) + COALESCE(c9,0) + COALESCE(c10,0) + COALESCE(c11,0) + COALESCE(c12,0) + COALESCE(c13,0) + COALESCE(c14,0) + COALESCE(c15,0) + COALESCE(c16,0) + COALESCE(c17,0) + COALESCE(c18,0) + COALESCE(c19,0) + COALESCE(c20,0) + COALESCE(c21,0) + COALESCE(c22,0) + COALESCE(c23,0) as sum FROM `dress` order by sum desc")
print(cursor.fetchall())

cursor.execute("SELECT COALESCE(c1,0) + COALESCE(c2,0) + COALESCE(c3,0) + COALESCE(c4,0) + COALESCE(c5,0) + COALESCE(c6,0) + COALESCE(c7,0) + COALESCE(c8,0) + COALESCE(c9,0) + COALESCE(c10,0) + COALESCE(c11,0) + COALESCE(c12,0) + COALESCE(c13,0) + COALESCE(c14,0) + COALESCE(c15,0) + COALESCE(c16,0) + COALESCE(c17,0) + COALESCE(c18,0) + COALESCE(c19,0) + COALESCE(c20,0) + COALESCE(c21,0) + COALESCE(c22,0) + COALESCE(c23,0) as sum FROM `dress` order by sum desc LIMIT 2,1 ")
print(cursor.fetchall())