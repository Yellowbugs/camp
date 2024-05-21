import sqlite3

con = sqlite3.connect("Activity.db")
c = con.cursor()

def createTable():
    c.execute("drop table activity")
    c.execute("create table activity(name text not null, size int not null, levels text not null, day text not null, startTime text not null, endTime text not null)")

def addActivity(name,size,levels,day,startTime,endTime):
    c.execute("insert into activity (name,size,levels,day,startTime,endTime) values (?,?,?,?,?,?)",(name,size,levels,day,startTime,endTime,))
    con.commit()

def viewAllActivities():
    return  c.execute("select * from activity order by name ASC").fetchall()

