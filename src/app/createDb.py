import sqlite3
conn= sqlite3.connect('data.db')
 
# cursor object
cur = conn.cursor()
 
# Drop the GEEK table if already exists.
cur.execute("DROP TABLE IF EXISTS user")
 
# Creating table
table = """ CREATE TABLE user (
            user_id INTEGER PRIMARY KEY,
            first_name CHAR(25),
            last_name CHAR(25),
            username CHAR(25),
            password CHAR(25),
            session CHAR(25),
            balance CHAR(25),
            ordersLeftToday INTEGER,
            partState INTEGER,
            activeTradeProfit CHAR(25)
        ); """
 
cur.execute(table)
 
print("Table is Ready")

sql = '''INSERT INTO user(first_name,last_name,username,password,session,balance,ordersLeftToday,partState,activeTradeProfit)
        VALUES(?,?,?,?,?,?,?,?,?) '''
print("test1")
cur.execute(sql, ("John", "Doe", "aa", "aa", "a1", "49.00", 20, 1, "0.00"))
print("test2")
conn.commit()
print("test3")
cur.execute(sql, ("Mary", "Jane", "bb", "bb", "a2", "0.00", 20, 1, "0.00"))
print("test4")
conn.commit()
print("test5")

cur.execute("DROP TABLE IF EXISTS parts")

# Creating table
table = """ CREATE TABLE parts (
            part_id INTEGER PRIMARY KEY,
            name CHAR(25),
            img_path CHAR(25),
            price CHAR(25)
        ); """
 
cur.execute(table)

sql2 = '''INSERT INTO parts(name,img_path,price)
        VALUES(?,?,?) '''

print("part1")
# https://www.yesterdaystractors.com/cgi-bin/store/model_parts.cgi?SearchArea=Allis-Chalmers&&md=B&cat=Brakes&r=mcats
cur.execute(sql2, ("Brake Adjusting Screw", "img/brake_adjusting_screw.jpeg", "26.30"))
conn.commit()

print("part2")
cur.execute(sql2, ("Brake Band Assembly", "img/brake_band_assembly.jpg", "40.00"))
conn.commit()

print("part3")
cur.execute(sql2, ("Brake Drum", "img/brake_drum.jpg", "65.95"))
conn.commit()

print("part4")
cur.execute(sql2, ("Brake Lining", "img/brake_lining.jpeg", "12.50"))
conn.commit()

print("part5")
cur.execute(sql2, ("Brake Pivot Pin", "img/brake_pivot_pin.jpeg", "11.44"))
conn.commit()

print("test6")
# Close the connection
conn.close()
print("test7")