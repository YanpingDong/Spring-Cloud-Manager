import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''DROP TABLE IF EXISTS  USER;''')
conn.execute('''DROP TABLE IF EXISTS SERVICE_INFO;''')
conn.execute('''DROP TABLE IF EXISTS MESSAGE;''')


conn.execute('''CREATE TABLE USER
       (ID INTEGER PRIMARY KEY autoincrement,
       NAME           TEXT    NOT NULL,
       PASSWORD           TEXT    NOT NULL,
       EMAIL            TEXT     NOT NULL,
       PHONE        TEXT);''')
print "USER Table created successfully";

conn.execute('''CREATE TABLE SERVICE_INFO
       (ID INTEGER PRIMARY KEY autoincrement,
       NAME           TEXT    NOT NULL,
       DESCRIPTION           TEXT    NOT NULL,
       UPLOAD_TIME            TEXT     NOT NULL,
       PHONE        TEXT);''')
print "SERVICE_INFO Table created successfully";

conn.execute('''CREATE TABLE MESSAGE
       (ID INTEGER PRIMARY KEY autoincrement,
       USER_ID           INT    NOT NULL,
       DESCRIPTION           TEXT    NOT NULL,
       UPDATE_TIME            TEXT     NOT NULL,
       TOPIC        TEXT    NOT NULL);''')
print "MESSAGE Table created successfully";

conn.close()