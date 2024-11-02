from flask import Flask, render_template
import util

username = 'raywu1990'
pwd = 'test'
host = '127.0.0.1'
port = '5432'
db = 'dvdrental'

app = Flask(__name__, template_folder='templates')
@app.route('/')

def index():
    cursor, connection = util.connect_db(username, pwd, host, port, db)

    cursor.execute('INSERT INTO basket_a (a, fruit_a)\nVALUES\n(5, \'cherry\');')
    record = util.run_sql(cursor, 'SELECT * FROM basket_a')
    if record == -1:
        return "Error with the SQL command."
    else:
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]

    util.disconnect_db(connection, cursor)

    return record


if __name__ == '__main__':

    app.debug = True
    ip = '127.0.0.1'
    app.run(host = ip)