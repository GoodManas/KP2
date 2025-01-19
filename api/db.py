import sqlite3

db = sqlite3.connect('db/time_tracking.db')
cursor = db.cursor()

if __name__ == "__main__":
	db.execute('''
CREATE TABLE "users" (
	"id_users"	INTEGER,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"dol"	INTEGER DEFAULT 1,
	"start_day"	TEXT,
	"end_day"	TEXT,
	PRIMARY KEY("id_users"),
	FOREIGN KEY("dol") REFERENCES "dol"("id")
); 
''')  
  
  
	db.execute('''
   CREATE TABLE "dol" (
	"id"	INTEGER,
	"dol"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);        
''')
  
  
	dol = [
    ('1','admin'),
    ('2','rabotnik'),
    ('3','manager')
]
	cursor.executemany('''
INSERT INTO dol (id, dol) 
VALUES (?, ?);
''', dol)            

db.commit()