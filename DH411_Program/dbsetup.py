import sqlite3


def CreateMenuDB():
    connection = sqlite3.connect('DHmenus.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS DiningHallMenus
                  (Date TEXT, DiningHall TEXT, MealName TEXT, Eggs INT, Fish INT, GF INT, Dairy INT, Peanuts INT, Soy INT, TreeNuts INT, Vegan INT, Vegetarian INT, Pork INT, Beef INT, Halal INT, Shellfish INT)''')
    connection.commit()
    connection.close()

def AddMenuItem(Date, DiningHall, MealName, MealTime, Eggs, Fish, GF, Dairy, Peanuts, Soy, TreeNuts, Vegan, Vegetarian, Pork, Beef, Halal, Shellfish):
    #try to connect to database
    #if it doesnt connect create the database
    connection = None
    try:
        connection = sqlite3.connect('DHmenus.db')
    except:
        CreateMenuDB()

    #Generate SQL Query and insert Data
    sql = f''' INSERT INTO DiningHallMenus(Date, DiningHall, MealName, MealTime, Eggs, Fish, GF, Dairy, Peanuts, Soy, TreeNuts, Vegan, Vegetarian, Pork, Beef, Halal, Shellfish)
                  VALUES({Date},{DiningHall},{MealName},{MealTime},{Eggs},{Fish},{GF},{Dairy},{Peanuts},{Soy},{TreeNuts},{Vegan},{Vegetarian},{Pork},{Beef},{Halal},{Shellfish}) '''
    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()
    connection.close()
