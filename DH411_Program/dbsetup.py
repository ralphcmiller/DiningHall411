import sqlite3

def createMenuDB():
    connection = sqlite3.connect('DHmenus.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS DiningHallMenus
                  (Date TEXT, DiningHall TEXT, MealName TEXT, MealTime TEXT)''')
    connection.commit()
    connection.close()

def addMenuItem(Date, DiningHall, MealName, MealTime):
    #try to connect to database
    #if it doesnt connect create the database

    createMenuDB()
    connection = sqlite3.connect('DHmenus.db')

    #Generate SQL Query and insert Data
    sql = f''' INSERT INTO DiningHallMenus(Date, DiningHall, MealName, MealTime)
                  VALUES(?,?,?,?) '''
    params = (Date,DiningHall,MealName,MealTime)
    cur = connection.cursor()
    cur.execute(sql, params)
    connection.commit()
    connection.close()

def findMenuItem(Date, DiningHall, MealName):
    #generates SQL for Date, Dining Hall Location, and optional specific meal
    connection = sqlite3.connect('DHmenus.db')
    if MealName:
        sql = f'''SELECT * from DiningHallMenus 
            WHERE Date = ? AND DiningHall = ? AND MealName = ?'''
        params = (Date, DiningHall, MealName)
    else:
        sql = f'''SELECT * from DiningHallMenus 
            WHERE Date = ? AND DiningHall = ?'''
        params = (Date, DiningHall)
    cur = connection.cursor()
    cur.execute(sql, params)
    return(cur.fetchall())
