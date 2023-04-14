import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
      id INTEGER PRIMARY KEY,
      username VARCHAR(255) NOT NULL,
      password VARCHAR(255) NOT NULL
      
)
""")

username1, password1 = "neerajy0326", hashlib.sha256("Secure@111".encode()).hexdigest()
username2, password2 = "admin", hashlib.sha256("Admin@111".encode()).hexdigest()
username3, password3 = "user", hashlib.sha256("User@111".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1,password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2,password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3,password3))

conn.commit()