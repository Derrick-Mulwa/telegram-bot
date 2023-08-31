from telegram import Update

import mysql.connector

db = mysql.connector.connect(
    host = 'derrickyy.mysql.pythonanywhere-services.com',
    user = 'derrickyy',
    password = 'python 101',
    database = 'derrickyy$database1')

cursor = db.cursor()

print('Done')