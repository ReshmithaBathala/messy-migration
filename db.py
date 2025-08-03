import sqlite3
from flask import g
from config import DATABASE

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(error=None):
    db = g.pop('db', None)
    if db:
        db.close()

def dict_from_row(row):
    return dict(row)
