import tmdbsimple as tmdb
import requests
import mysql.connector

tmdb.API_KEY = '2f67f766f9080c17e2a3a1a2528d14c5'

movie = None

i = 5000
try:
    movie = tmdb.Movies(500000).info()
    print(f"{i}: {movie['title']}")
except requests.exceptions.HTTPError as e:
    # print(f"Movie with id {i} not found")
    print(e.response)

mydb = mysql.connector.connect(
  host="sql7.freemysqlhosting.net",
  user="sql7338051",
  passwd="4zmaynvryX",
  database="sql7338051"
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO test_table (id ,txt, num) VALUES (%s, %s, %s)"
val = (None, "Inserted!!!", 27)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


        

