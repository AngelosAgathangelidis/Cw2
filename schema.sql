import sqlite3

with sqlite3.connect('sample.db') as connection
  c = connection.cursor()
  c.execute("""DROP TABLE seats""")
  c.execute('CREATE TABLE seats(title TEXT, price TEXT)')

  c.execute('INSERT INTO seats VALUES("seat 1 row 1", "10")')
  c.execute('INSERT INTO seats VALUES("seat 2 row 1", "10")')
  c.execute('INSERT INTO seats VALUES(seat 3 row 1", "10")')
  c.execute('INSERT INTO seats VALUES(seat 4 row 1", "10")')
  c.execute('INSERT INTO seats VALUES(seat 5 row 1", "10")')
