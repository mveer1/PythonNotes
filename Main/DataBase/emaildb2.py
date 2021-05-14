import sqlite3
#the program reads the number or frequency of each email, but on a file on database
conn = sqlite3.connect('emaildb2.sqlite')                #if doesnt exists, it will create a file
cur = conn.cursor()                                      #kinda like a handle

cur.execute('DROP TABLE IF EXISTS Counts')               #this string will be run in sqlite app, as a code line, you send your commands through cursor and recieve commands too

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    fullemail = pieces[1]
    pieces2 = fullemail.split('@')
    email=pieces2[1]                                                         #till here you know what was going
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))          #email is put in place of ? #(email,) is a one-tuple, *weird syntax*, Now, it is dangerous to put those strings, especially from user-entered data, into your SQL. You technically could. I could make this be a ...email = 'csev@umich.edu' I would have to escape the quotes and stuff, but this question mark is a placeholder. And this is a way to basically make sure that we don't allow SQL injection.
    row = cur.fetchone()                                                        #now the first one (the response from db afaiu) to row, if the above line fails, row is gonna be none. which it will, the first time, as we dont have a database, we're creating it with mbox-short.txt
    if row is None:                                                             #which happens for the first email
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))                                     #email in place of ?, we make a row, set the email coloumn to the first email, and count coloumn to 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))                                                   #increament by 1 if emails comesby again
conn.commit()                                                               #commit is to write the things which are in memory rn, to disk, so as to free up the memory ig, usually it depends how often we use it, here we use it every time we run the loop, also its the slowest step.

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'         #readable, and we're getting the top 10

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
