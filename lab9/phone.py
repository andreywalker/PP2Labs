import psycopg2
import csv

conn = psycopg2.connect(dbname='postgres', user='postgres', password='53515759sql', host='localhost')
cursor = conn.cursor()
run=True
print("for ADDING new contact enter add,name,number separating with comas")
print("for UPDATING contact enter add,name,number separating with comas'")
print("for DELETING contact enter del,name or del,number separating with comas'")
print("for SHOWING the phone number list enter sh,filter (filters: all, +7, 8")
print("for EXIT enter 'ex'")

tname="ph_b"
rt=False
rc=True

file=open("phone_book.txt", "r")
with open('phone_book2.csv', newline='') as csvfile:
    ss = csv.reader(csvfile,)
    print("reading")
    for row in ss:
        cursor.execute("INSERT INTO "+tname+" VALUES ('"+row[0]+"' , '"+row[1]+"')")
        print("inserted")

cursor.execute("CREATE TABLE IF NOT EXISTS "+tname+"(name text, number text)")

if rt:
    for x in file:
        ss=x.split(",")
        cursor.execute("INSERT INTO "+tname+" VALUES ('"+ss[0]+"' , '"+ss[1]+"')")


def insert(name, num):
    cursor.execute("INSERT INTO "+tname+" VALUES ('"+name+"' , '"+num+"')")

def update(name, newnum):
    cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT name FROM "+tname+" WHERE name = '"+name+"')")
    f=cursor.fetchall()
    cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT number FROM "+tname+" WHERE number = '"+newnum+"')")
    g=cursor.fetchall()
    #print(f)
    if f and not g:
        if f[0][0]==name:
            cursor.execute("UPDATE "+tname+" SET number = '"+newnum+"' WHERE name = '"+name+"'")
        else:
            insert(name , newnum)
    elif g and not f:
        if g[0][1]==newnum:
            cursor.execute("UPDATE "+tname+" SET name = '"+name+"' WHERE number = '"+newnum+"'")
        else:
            insert(name , newnum)
    else:
        insert(name , newnum)
def delete(contact):
    cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT name FROM "+tname+" WHERE name = '"+contact+"')")
    f=cursor.fetchall()
    cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT number FROM "+tname+" WHERE number = '"+contact+"')")
    g=cursor.fetchall()
    if f:
        cursor.execute("DELETE FROM "+tname+" WHERE name = '"+contact+"'")
    elif g:
        cursor.execute("DELETE FROM "+tname+" WHERE number = '"+contact+"'")
    
def show(fil):
    if fil=="all":
        cursor.execute("SELECT * FROM "+tname+" ")
        print("************")
        for i in cursor.fetchall():
            print(str(i[0])+" "+str(i[1]))
            print("___________")
            print(" ")
        print("************")
    elif fil=="+7":
        cursor.execute("SELECT * FROM "+tname+" WHERE number LIKE '+7%'")
        print("************")
        for i in cursor.fetchall():
            print(str(i[0])+" "+str(i[1]))
            print("___________")
            print(" ")
        print("************")
    elif fil=="8":
        cursor.execute("SELECT * FROM "+tname+" WHERE number LIKE '8%'")
        print("************")
        for i in cursor.fetchall():
            print(str(i[0])+" "+str(i[1]))
            print("___________")
            print(" ")
        print("************")

while run:
    s=input()
    ss=s.split(",")
    if ss[0]=="add":
        update(ss[1], ss[2])
    elif ss[0]=="up":
        update(ss[1],ss[2])
    elif ss[0]=="sh":
        show(ss[1])
    elif ss[0]=="ex":
        cursor.execute("COMMIT")
        run=False
    elif ss[0] == "del":
        delete(ss[1])


