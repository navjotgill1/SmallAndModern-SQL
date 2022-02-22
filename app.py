import mysql.connector


#establish connection to database, mysql here
db = mysql.connector.connect(
    host="localhost",
    user="root",
#your password may vary
    password = "pwd",
    database="testdatabase"
)

#cursor für die datenbank
mycursor = db.cursor()

#comment out the code in the next lines for the first time, to create the database

#mycursor.execute("CREATE TABLE film(titel varchar(50))")
#db.commit()


#method to add films into the table
def add(titel):
    sql = ("INSERT INTO filme(titel) values(%s);")
    mycursor.execute(sql, (titel,))
    db.commit()

#method to edit entries in the table
def update(titel, neuertitel):
    sql = ("UPDATE filme SET titel= %s WHERE titel=%s;")
    mycursor.execute(sql, (neuertitel,titel))
    db.commit()

#method to delete entries from the table
def delete(titel):
    sql = ("DELETE FROM filme WHERE titel=%s;")
    mycursor.execute(sql, (titel, ))
    db.commit()

#method to print out all entries from the table
def getFilms():
    sql = ("SELECT * FROM filme ORDER BY titel DESC")
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for row in result:
        print(row)

add("wall-street")
getFilms()
#add("dune")
#add("dune 2")
#add("tenet")

#update("dune 2", "dune part two")

#delete("tenet")
