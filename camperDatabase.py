import sqlite3

con = sqlite3.connect("Camper.db")
c = con.cursor()

def createTable():
    c.execute("drop table campers")
    c.execute("create table campers(firstName text PRIMARY KEY not null, lastName text not null, level text not null)")


def addCamper(firstName,lastName,level):
    c.execute("insert into campers (firstName, lastName, level) values (?,?,?)",(firstName,lastName,level))
    con.commit()

def viewAllcampers():
    return c.execute("select * from campers order by lastName ASC").fetchall()

def searchCampersByName(firstName,lastName,level):
    if firstName == "" and lastName == "" and level == "Any":
        return viewAllcampers()
    if level == "Any":
        return c.execute("select * from campers where firstName like (?) and lastName like (?) order by lastName ASC",("%"+firstName+"%","%"+lastName+"%",)).fetchall()
    else:
        return c.execute("select * from campers where firstName like (?) and lastName like (?) and level = (?) order by lastName ASC",("%"+firstName+"%","%"+lastName+"%",level,)).fetchall()


def deleteCamper(firstName,lastName,level):
    c.execute("delete from campers where firstName = (?) and lastName = (?) and level = (?)",(firstName,lastName,level,))
    c.commit()


def addTestCampers():
    addCamper("Josh","Clinton","Advanced")
    addCamper("Anthony","Clinton","Intermediate")


#print(viewAllcampers())