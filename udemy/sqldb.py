import sqlite3 as sql

# establish connection with the db and create sql object to perform action
database1 = sql.connect('test1.db')

# create a cursor object to commit sql code to
db1_cursor = database1.cursor()

# use db1_cursor to execute sql
#cmd = 'create table users(username TEXT, password TEXT)'

# execute above statement
#db1_cursor.execute(cmd)

# inserting data in database
cmd2 = 'insert into users(username, password) values ("testuser", "testpassword")'
db1_cursor.execute(cmd2)

# retrieving data from database
cmd3 = 'select username, password from users'
db1_cursor.execute(cmd3)

# commit data
database1.commit()

# for loop to print data
for x in db1_cursor:
	print x