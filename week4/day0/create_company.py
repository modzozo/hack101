import sqlite3

def open_connection(database):
    db = sqlite3.connect(database)
    return db

def create():
    #TODO check if schema exists, if yes drop and re-create

    db = open_connection('company.db')
    cursor = db.cursor()

    db.execute('''DROP TABLE employees''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY,
            name TEXT, monthly_salary TEXT, yearly_bonus TEXT,
            position TEXT)''')
    db.commit()
    db.close()

def insert():
    db = open_connection('company.db')
    cursor = db.cursor()

    cursor.execute('''INSERT INTO
        employees(name, monthly_salary, yearly_bonus, position)
        VALUES("Ivan Ivanov", 5000, 10000, "Software Developer");''')

    cursor.execute('''INSERT INTO
        employees(name, monthly_salary, yearly_bonus, position)
        VALUES("Rado Rado", 500, 0, "Technical Support Intern");''')

    cursor.execute('''INSERT INTO
        employees(name, monthly_salary, yearly_bonus, position)
        VALUES("Ivo Ivo", 10000, 100000, "CEO");''')

    cursor.execute('''INSERT INTO
        employees(name, monthly_salary, yearly_bonus, position)
        VALUES("Petar Petrov", 3000, 1000, "Marketing Manager");''')

    cursor.execute('''INSERT INTO
        employees(name, monthly_salary, yearly_bonus, position)
        VALUES("Maria Georgieva", 8000, 10000, "COO");''')

    db.commit()
    db.close()





if __name__ == '__main__':
    create()
    insert()

