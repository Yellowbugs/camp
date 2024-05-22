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

def searchActivity(name,available,levels,days):
    if available:
        return c.execute("select * from activity where name like (?) and spotsLeft > 0 and (levels like (?) or levels like (?) or levels like (?)) and (day like (?) or day like (?) or day like (?) or day like (?) or day like (?)) order by name ASC",("%"+name+"%","%"+levels[0]+"%","%"+levels[1]+"%","%"+levels[2]+"%","%"+days[0]+"%","%"+days[1]+"%","%"+levels[2]+"%","%"+days[3]+"%","%"+days[4]+"%",)).fetchall()
    else:
        return c.execute("select * from activity where name like (?) and (levels like (?) or levels like (?) or levels like (?)) and (day like (?) or day like (?) or day like (?) or day like (?) or day like (?)) order by name ASC",("%"+name+"%","%"+levels[0]+"%","%"+levels[1]+"%","%"+levels[2]+"%","%"+days[0]+"%","%"+days[1]+"%","%"+levels[2]+"%","%"+days[3]+"%","%"+days[4]+"%",)).fetchall()

