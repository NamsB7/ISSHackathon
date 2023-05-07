# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # Configure SQLite connection
# app.config['DATABASE'] = 'items.db'

# # Create items table if it does not exist
# def create_table():
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('''CREATE TABLE IF NOT EXISTS items
#                        (item_no INTEGER PRIMARY KEY,
#                         item_description TEXT NOT NULL,
#                         item_type TEXT NOT NULL,
#                         person_name TEXT NOT NULL,
#                         person_phone_no TEXT NOT NULL,
#                         person_email_id TEXT NOT NULL,
#                         roll_no INTEGER NOT NULL,
#                         item_status TEXT NOT NULL)''')

# create_table()

# @app.route('/')
# def index():
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('SELECT * FROM items')
#         items = cur.fetchall()
#     return render_template('index.html', items=items)

# @app.route('/sell')
# def sell():
#     return render_template('sell.html')

# @app.route('/insert', methods=['POST'])
# def insert_item():
#     item_no = request.form['item_no']
#     item_description = request.form['item_description']
#     item_type = request.form['item_type']
#     person_name = request.form['person_name']
#     person_phone_no = request.form['person_phone_no']
#     person_email_id = request.form['person_email_id']
#     roll_no = request.form['roll_no']
#     item_status = request.form['item_status']
    
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('''INSERT INTO items 
#                        (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status)
#                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
#                     (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status))
    
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)


# 

# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
# import uuid

# app = Flask(__name__)

# # Configure SQLite connection
# app.config['DATABASE'] = 'items.db'

# # Create items table if it does not exist
# def create_table():
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('''CREATE TABLE IF NOT EXISTS items
#                        (item_no INTEGER PRIMARY KEY,
#                         item_description TEXT NOT NULL,
#                         item_type TEXT NOT NULL,
#                         person_name TEXT NOT NULL,
#                         person_phone_no TEXT NOT NULL,
#                         person_email_id TEXT NOT NULL,
#                         roll_no INTEGER NOT NULL,
#                         item_status TEXT NOT NULL)''')

# create_table()



# @app.route('/index')
# def found():
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('SELECT * FROM items WHERE item_status = "found"')
#         items = cur.fetchall()
#     return render_template('found.html', items=items)

# @app.route('/sell')
# def sell():
#     item_no = str(uuid.uuid4().int)[:6] # generate a 6-digit random number
#     return render_template('sell.html', item_no=item_no)

# @app.route('/insert', methods=['POST'])
# def insert_item():
#     item_no = request.form['item_no']
#     item_description = request.form['item_description']
#     item_type = request.form['item_type']
#     person_name = request.form['person_name']
#     person_phone_no = request.form['person_phone_no']
#     person_email_id = request.form['person_email_id']
#     roll_no = request.form['roll_no']
#     item_status = request.form['item_status']
    
#     with sqlite3.connect(app.config['DATABASE']) as con:
#         cur = con.cursor()
#         cur.execute('''INSERT INTO items 
#                        (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status)
#                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
#                     (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status))
    
#     return redirect(url_for('found'))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import uuid

app = Flask(__name__)

# Configure SQLite connection
app.config['DATABASE'] = 'items.db'

# Create items table if it does not exist
def create_table():
    with sqlite3.connect(app.config['DATABASE']) as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS items
                       (item_no INTEGER PRIMARY KEY,
                        item_description TEXT NOT NULL,
                        item_type TEXT NOT NULL,
                        person_name TEXT NOT NULL,
                        person_phone_no TEXT NOT NULL,
                        person_email_id TEXT NOT NULL,
                        roll_no INTEGER NOT NULL,
                        item_status TEXT NOT NULL)''')

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/found')
def found():
    with sqlite3.connect(app.config['DATABASE']) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM items WHERE item_status = "found"')
        items = cur.fetchall()
    return render_template('found.html', items=items)

@app.route('/sell')
def sell():
    item_no = str(uuid.uuid4().int)[:6] # generate a 6-digit random number
    return render_template('sell.html', item_no=item_no)

@app.route('/insert', methods=['POST'])
def insert_item():
    item_description = request.form['item_description']
    item_type = request.form['item_type']
    person_name = request.form['person_name']
    person_phone_no = request.form['person_phone_no']
    person_email_id = request.form['person_email_id']
    roll_no = request.form['roll_no']
    item_status = request.form['item_status']
    
    with sqlite3.connect(app.config['DATABASE']) as con:
        cur = con.cursor()
        cur.execute('''INSERT INTO items 
                       (item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status))
    
    return redirect(url_for('found'))


@app.route('/buy',methods=['POST','GET'])
def buy():
    if request.method == 'POST':
        item_description = request.form['item_description']
        item_name = request.form['item_name']
        if item_description != "" and item_name != "":
            desc = 'item_description LIKE "%'+item_description+'%" AND '
            name = 'item_type LIKE "%'+item_name+'%"'
        elif item_description != "":
            desc = 'item_description LIKE "%'+item_description+'%" AND '
            name = '1'
        elif item_name != "":
            desc = '1 AND '
            name = 'item_type LIKE "%'+item_name+'%"'
        else:
            desc = '1 AND '
            name = '1'
        with sqlite3.connect(app.config['DATABASE']) as con:
            cur = con.cursor()
            cur.execute('SELECT item_type, item_description, person_name FROM items WHERE item_status="on-sale" AND ('+desc+name+')')
            items = cur.fetchall()
    else:
        with sqlite3.connect(app.config['DATABASE']) as con:
            cur = con.cursor()
            cur.execute('''SELECT item_type, item_description, person_name FROM items WHERE item_status="on-sale"''')
            items = cur.fetchall()
    
    return render_template('buy2.html', items=items)

@app.route('/search', methods=['POST','GET'])
def search():
    
    if request.method == 'GET':
        return render_template('search.html')
        item_description = request.form['item_description']
    
    
    
if __name__ == '__main__':
    app.run(port=5001, debug=True)
