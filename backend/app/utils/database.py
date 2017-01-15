import sqlite3

#TODO change to static path
from flask import Flask, jsonify, g, request
from sqlite3 import dbapi2 as sqlite3

DATABASE = 'test.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		db.row_factory = sqlite3.Row
	return db

def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None: db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv


def add_user(id,name, password, email,phone):
	sql = "INSERT INTO USER (id,name, password, email,phone) VALUES(%d, '%s', '%s','%s','%s')" %(id,name, password,email,phone)
	print(sql)
	db = get_db()
	db.execute(sql)
	res = db.commit()
	return res

def find_student(name=''):
	sql = "select * from students where name = '%s' limit 1" %(name)
	print(sql)
	db = get_db()
	rv = db.execute(sql)
	res = rv.fetchall()
	rv.close()
	return res[0]
