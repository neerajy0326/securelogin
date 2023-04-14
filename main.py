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

print(password1)