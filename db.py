import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price integer)
        """)
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows


    def insert(self, part, customer, retailer, price):
        self.cur.execute("""
        INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)
        """, (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("""
        DELETE FROM parts where id=?
        """, (id,))
        self.conn.commit()

    def delete(self):
        self.cur.execute('DELETE FROM parts')
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("""
        UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? Where id = ?
        """, (part, customer, retailer, price, id))
    
    def __del__(self):
        self.conn.close()


# db = Database('store.db')
# db.delete()
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")



# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["store"]
# col = db["items"]
# sample
# sample = { "name": "Mercurial", "customer": "Ibouelezz", "retailer": "Nike", "price": "250" }
# x = col.insert_one(sample)