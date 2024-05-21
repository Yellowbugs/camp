import sqlite3

con = sqlite3.connect("Activity.db")
c = con.cursor()

def createTable():
    c.execute("drop table activity")
    c.execute("create table activity(name text not null, size integer not null, spotsLeft integer not null, levels text not null, day text not null, startTime text not null, endTime text not null)")

def addActivity(name,size,levels,day,startTime,endTime):
    c.execute("insert into activity (name,size,spotsLeft,levels,day,startTime,endTime) values (?,?,?,?,?,?,?)",(name,size,size,levels,day,startTime,endTime,))
    con.commit()

def viewAllActivities():
    return  c.execute("select * from activity order by name ASC").fetchall()

def searchActivity(name,level,day):
    return c.execute("select * from activity where name like (?) order by name ASC",("%"+name+"%",)).fetchall()


