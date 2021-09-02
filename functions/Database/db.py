import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

def create_db():
  mycursor.execute("CREATE DATABASE IF NOT EXISTS aawaz")

  mycursor.execute("USE aawaz")

  mycursor.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR(50), password_hash VARCHAR(255), logged CHAR(5), recovery VARCHAR(50))")

  mycursor.execute("CREATE TABLE IF NOT EXISTS data (md5 VARCHAR(255), text LONGTEXT)")

  mycursor.execute("CREATE TABLE IF NOT EXISTS passmanager (name VARCHAR(255), pass_hash LONGTEXT)")

def signupdb(val1, val2, val3):
  sql = "INSERT INTO user (username, password_hash, logged, recovery) VALUES (%s, %s, %s, %s)"
  val = (val1, val2, "T", val3)
  mycursor.execute(sql, val)

  mydb.commit()

def insertdb(val1, val2):
  sql = "INSERT INTO data (md5, text) VALUES (%s, %s)"
  val = (val1, val2)
  mycursor.execute(sql, val)

  mydb.commit()

def insertpassdb(val1, val2):
  sql = "INSERT INTO passmanager (name, pass_hash) VALUES (%s, %s)"
  val = (val1, val2)
  mycursor.execute(sql, val)

  mydb.commit()

def update_passdb(val1, val2):
  sql = "UPDATE passmanager SET pass_hash = %s WHERE name = %s"
  val = (val1, val2)

  mycursor.execute(sql, val)

  mydb.commit()

def show_passdb(uname):
  sql = "SELECT * FROM passmanager WHERE name = %s"
  val = (uname,)
  mycursor.execute(sql, val)

  result = mycursor.fetchall()

  res = []

  if len(result) != 0:
    res = [x for x in result[0]]

  return res

def logindb(username):

  sql = "SELECT * FROM user WHERE username = %s"
  val = (username,)
  mycursor.execute(sql, val)

  result = mycursor.fetchall()
  # un, pas, log, key = mycursor.fetchall()
  # print(un,pas,log,key)

  res = []

  if len(result) != 0:
    res = [x for x in result[0]]

  return res

def login_updatedb(username):
  sql = "UPDATE user SET logged = %s WHERE username = %s"
  val = ("T", username)

  mycursor.execute(sql, val)

  mydb.commit()

def displaydb(md5):
  mycursor.execute("SELECT * FROM data WHERE md5 = %s",(md5, ))

  result = mycursor.fetchall()
  res = []

  if len(result) != 0:
    res = [x for x in result[0]]

  return res

def logoutdb(username):
  sql = "UPDATE user SET logged = %s WHERE username = %s"
  val = ("F", username)

  mycursor.execute(sql, val)

  mydb.commit()


def forgot_passdb(val1, val2):
  sql = "UPDATE user SET password_hash = %s WHERE username = %s"
  val = (val1, val2)

  mycursor.execute(sql, val)

  mydb.commit()

def user_deldb(username):
  sql = "DELETE FROM user WHERE username = %s"

  val = (username, )

  mycursor.execute(sql, val)

  mydb.commit()

def display_all():
  mycursor.execute("SELECT * FROM data")

  results = mycursor.fetchall()
  print(results)
  res = []

  if len(results) != 0:
    for result in results:
      res.append(result[1])

  return res

def dropdb():
  mycursor.execute("DELETE FROM data")
  mydb.commit()

  mycursor.execute("SELECT * FROM data")

  res = mycursor.fetchall()
  if len(res) == 0:
    return True
  else:
    return False