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
rc=False

file=open("phone_book.txt", "r")
if rc:
    with open('phone_book2.csv', newline='') as csvfile:
        ss = csv.reader(csvfile,)
        #print("reading")

        for row in ss:
            cursor.execute("INSERT INTO "+tname+" VALUES ('"+row[0]+"' , '"+row[1]+"')")
            #print("inserted")

cursor.execute("CREATE TABLE IF NOT EXISTS "+tname+"(name text, number text)")

if rt:
    for x in file:
        ss=x.split(",")
        cursor.execute("INSERT INTO "+tname+" VALUES ('"+ss[0]+"' , '"+ss[1]+"')")


def insert(name, num):
    if num.isdigit() and len(num)==11:
        cursor.execute("INSERT INTO "+tname+" VALUES ('"+name+"' , '"+num+"')")
    else:
        print("!!  incorrect phone number  !!")
        print("!! "+name+" , "+num+" !!")

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
    if not contact=="all":
        cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT name FROM "+tname+" WHERE name = '"+contact+"')")
        f=cursor.fetchall()
        cursor.execute("SELECT name FROM "+tname+" WHERE EXISTS (SELECT number FROM "+tname+" WHERE number = '"+contact+"')")
        g=cursor.fetchall()
        if f:
            cursor.execute("DELETE FROM "+tname+" WHERE name = '"+contact+"'")
        elif g:
            cursor.execute("DELETE FROM "+tname+" WHERE number = '"+contact+"'")
    else:
        cursor.execute("DELETE FROM "+tname+" ")
def show(page =1, fil="all",pattern=" "):
    page-=1
    if fil=="all":
        cursor.execute("SELECT * FROM "+tname+" ORDER BY name LIMIT 5 OFFSET "+str(5*page)+" ")
        print("************")
        for i in cursor.fetchall():
            print(str(i[0])+" "+str(i[1]))
        print("************")
    elif fil=="/p":
        cursor.execute("SELECT * FROM "+tname+" WHERE number LIKE '%"+pattern+"%' ORDER BY name LIMIT 5 OFFSET "+str(5*page)+" ")
        f=cursor.fetchall()
        cursor.execute("SELECT * FROM "+tname+" WHERE name LIKE '%"+pattern+"%' ORDER BY name LIMIT 5 OFFSET "+str(5*page)+" ")
        g=cursor.fetchall()
        print("************")
        for i in f:
            print(str(i[0])+" "+str(i[1]))
        for j in g:
            print(str(j[0])+" "+str(j[1]))
        print("************")

    '''elif fil=="+7":
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
        print("************")'''

def shall():
    cursor.execute("SELECT * FROM "+tname+" ORDER BY name")
    print("************")
    for i in cursor.fetchall():
        print(str(i[0])+" "+str(i[1]))
    print("************")

while run:
    s=input()
    ss=s.split(", ")
    if ss[0]=="add":
        if not ss[1]=="/m":
            update(ss[1], ss[2])
        else:
            while not ss[0]==".":
                s=input()
                ss=s.split(", ")
                if not ss[0]=="." and len(ss)>1:
                    update(ss[0], ss[1])
        cursor.execute("COMMIT")
    elif ss[0]=="up" and len(ss)>2:
        update(ss[1],ss[2])
    elif ss[0]=="sh":
        if len(ss)==3:
            show(int(ss[1]),ss[2])
        elif len(ss)==4:
            show(int(ss[1]), ss[2],ss[3])
        elif len(ss)==2:
            show(int(ss[1]))
        else:
            show()
    elif ss[0]=="ex":
        cursor.execute("COMMIT")
        run=False
    elif ss[0] == "del" and len(ss)>1:
        delete(ss[1])
    elif ss[0]=="shall":
        shall()


