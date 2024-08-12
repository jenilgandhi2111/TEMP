import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("profiles.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY,
                link TEXT,
                score INTEGER
            )''')
        self.connection.commit()
    
    def setProfile(self,profileUrl,score):
        try:
            self.cursor.execute('''INSERT INTO profiles (link,score) VALUES (?,?)''',(profileUrl,int(score)))
            self.connection.commit()
            return True
        except Exception as E:
            print(E)
            return False
    def getProfile(self,profileUrl):
        try:
            if len(self.cursor.execute('''SELECT * FROM profiles WHERE link = ? ''',(str(profileUrl),)).fetchall()) == 0:
                return False
            return True
            
        except Exception as E:
            print(E)
            return False
        
# # # # Example usage
# db = Database()
# result = db.setProfile("http://example.com/profile", 100)
# print(result)
# profile = db.getProfile("http://exampasdasdale.com/profile")
# print(profile)