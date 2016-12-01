from flask import Flask, render_template, url_for, request, redirect, flash, g, session
import sqlite3

app = Flask(__name__)

app.secret_key="superkey"
#db_location = 'var/test.db'

#def get_db():
#  db = gettatr(g, 'db', None)
#  if db is None:
#    db = sqlite3.connect(db_location)
#    g.db = db
#  return db

#@app.teardown_appcontext
#def close_db_connection(exception):
#  db = getattr(g, 'db', None)
#  if db is not None:
#    db.close()

#def init_db():
#  with app.app_context():
#    db = get_db()
#    with app.open_resource('schema.sql', mode='r') as f:
#      db.cursor().executescript(f.read())
#    db.commit()

@app.route('/')
def root():
  return render_template('base.html'), 200


@app.route('/history/')
def history():
  return render_template('history.html'), 200


@app.route('/login/', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] !=  'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      session['logged_in']= True
      flash("You logged in !")
      return redirect(url_for('root'))
  return render_template('login.html', error=error)

@app.route('/tickets/')
def tickets():
#  page = []
# page.append('<html><ul>')
#  sql = "SELECT rowid, * FROM seats ORDER BY price"
#  for row in db.cursor().execute(sql):
#    page.append('<li>')
#    page.append(str(row))
#    page.append('</li>')
#  page.append('</ul><html>')

  return render_template('tickets.html'), 200

@app.route('/home/')
def home():
  return redirect(url_for('root'))

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "The page you requested doesn't exist.", 404

@app.route('/contact/')
def contact():
  return render_template('contact.html'), 200


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
