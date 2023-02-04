import time

import psycopg2
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

cache = psycopg2.connect(
    database="postgres",
    user="admin",
    password="root",
    host="postgresqldb"
)

def get_counter():
    retries = 5
    while True:
        try:
            with cache:
                with cache.cursor() as curs:
                    curs.execute('''UPDATE Register set count = count + 1''')
                    curs.execute('''SELECT * FROM Register''')
                    return curs.fetchall()[0][0]
        except psycopg2.OperationalError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
            
            
def reset_counter():
    retries = 5
    while True:
        try:
            with cache:
                with cache.cursor() as curs:
                    curs.execute('''UPDATE Register set count = 0''')
                    curs.execute('''SELECT * FROM Register''')
                    return curs.fetchall()[0][0]
        except psycopg2.OperationalError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
            
def set_counter(value):
    retries = 5
    while True:
        try:
            with cache:
                with cache.cursor() as curs:
                    instruction = "UPDATE Register set count = " + str(value)
                    curs.execute(instruction)
                    curs.execute('''SELECT * FROM Register''')
                    return curs.fetchall()[0][0]
        except psycopg2.OperationalError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/counter/get/')
def GET():
    count = get_counter()
    return 'La pagina ha sido visitada {} times.\n'.format(count)
    
@app.route('/counter/reset/')
def DELETE():
    reset_counter()
    return 'El contador ha sido reseteado'

@app.route('/counter/set/<int:new_value>')
def PUT(new_value):
    count = set_counter(new_value)
    return 'El valor del contador cambio a {}.\n'.format(count)

@app.route('/counter/update/<int:new_value>')
def POST(new_value):
    count = set_counter(new_value)
    return 'El valor del contador cambio a {}.\n'.format(count)
    