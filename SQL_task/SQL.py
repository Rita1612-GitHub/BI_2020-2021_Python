import sqlite3
from pprint import pprint

connection = sqlite3.connect('C:/Users/Рита/Database.db')
cursor = connection.cursor()

cursor.execute('''
PRAGMA foreign_keys=ON
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Table_1 (SubjectID INT NOT NULL PRIMARY KEY, Subject TEXT UNIQUE, LecturerName TEXT)
''')

cursor.execute('''
INSERT OR IGNORE INTO Table_1(SubjectID, Subject, LecturerName)
VALUES
(1, 'Python', 'Alexander'),
(2, 'R', 'Lavrentii'),
(3, 'Practicum', 'Michail')
''')

connection.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Table_2 (
StudentID INT NOT NULL PRIMARY KEY, FirstNme TEXT, LastName TEXT, Subject TEXT, Score INT, SubjectID INT,
FOREIGN KEY (SubjectID) REFERENCES Table_1(SubjectID) ON DELETE CASCADE
FOREIGN KEY (Subject) REFERENCES Table_1(Subject) ON UPDATE CASCADE
)
''')

table_2_data = [
    (1, 'Alexander', 'Andreev', 'Python', 84, 1),
    (2, 'Daria', 'Andreeva', 'Python', 76, 1),
    (3, 'Kristina', 'Gainova', 'Python', 76, 1),
    (4, 'Grigoriy', 'Gladkov', 'Python', 79, 1),
    (5, 'Ekaterina', 'Daniyko', 'Python', 85, 1),
    (6, 'Alexander', 'Andreev', 'R', 251, 2),
    (7, 'Daria', 'Andreeva', 'R', 229, 2),
    (8, 'Kristina', 'Gainova', 'R', 232, 2),
    (9, 'Grigoriy', 'Gladkov', 'R', 245, 2),
    (10, 'Ekaterina', 'Daniyko', 'R', 278, 2),
    (11, 'Alexander', 'Andreev', 'Practicum', 10, 3),
    (12, 'Daria', 'Andreeva', 'Practicum', 9, 3),
    (13, 'Kristina', 'Gainova', 'Practicum', 8, 3),
    (14, 'Grigoriy', 'Gladkov', 'Practicum', 10, 3),
    (15, 'Ekaterina', 'Daniyko', 'Practicum', 10, 3)
]

cursor.executemany('''
INSERT OR IGNORE INTO Table_2(StudentID, FirstNme, LastName, Subject, Score, SubjectID)
VALUES (?,?,?,?,?,?)
''', table_2_data)

connection.commit()

cursor.execute('''UPDATE Table_1 SET Subject = 'ML' WHERE SubjectID = 2''')
connection.commit()
cursor.execute('''DELETE FROM Table_1 WHERE SubjectID = 3''')
connection.commit()
cursor.execute('''SELECT * from Table_2''')
pprint(cursor.fetchall())

connection.close()
