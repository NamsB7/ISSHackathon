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
    item_no = request.form['item_no']
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
                       (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                    (item_no, item_description, item_type, person_name, person_phone_no, person_email_id, roll_no, item_status))
    
    return redirect(url_for('found'))


@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    
    with sqlite3.connect(app.config['DATABASE']) as con:
        cur = con.cursor()
        cur.execute('''SELECT * FROM items WHERE item_description LIKE ? OR item_type LIKE ?''', ('%' + search_query + '%', '%' + search_query + '%'))
        items = cur.fetchall()
        
    return render_template('search_results.html', items=items)
    
if __name__ == '__main__':
    app.run(debug=True)