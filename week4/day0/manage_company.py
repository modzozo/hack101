import sqlite3

class ManageCompany():

    def __init__(self):
        self.connect = sqlite3.connect("company.db")
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()


    def list_employees(self):

        exe = self.cursor.execute('''SELECT id,name, position FROM employees''')
        for row in exe:
            print("{}. {} - {}".format(row["id"], row["name"], row["position"]))


    def monthly_spending(self):

        exe = self.cursor.execute('''SELECT SUM(monthly_salary) FROM employees''')
        print(list(exe.fetchone()))

    def yearly_spending(self):
        exe = self.cursor.execute('''SELECT SUM(yearly_spending) FROM employees''')
        print(list(exe.fetchone()))

    def add_employee(self):
        name = input("name> ")
        monthly_salary = input("monthly_salary> ")
        yearly_bonus = input("yearly_bonus> ")
        position = input("position> ")
        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?);''',
            (name, monthly_salary, yearly_bonus, position))

        self.connect.commit()

    def update_employee(self, id):
        name = input("name> ")
        monthly_salary = input("monthly_salary> ")
        yearly_bonus = input("yearly_bonus> ")
        position = input("position> ")
        self.cursor.execute('''UPDATE employees SET name = ?,
            monthly_salary = ?, yearly_bonus = ?, position = ?
            WHERE id = ?;''', (name, monthly_salary, yearly_bonus, position, id))

        self.connect.commit()

    def delete_employee(self,id):
        self.cursor.execute('''DELETE FROM employees WHERE id = ?''',(id))

        self.connect.commit()


    def console(self):
        while True:
            reply = input("\nYour choice: ")
            if reply == 'exit':
                break
            else:
                reply = reply.split()  # make list of arguments
                if reply[0] == "list_employees":
                    self.list_employees()
                elif reply[0] == "monthly_spending":
                    self.monthly_spending()
                elif reply[0] == "yearly_spending":
                    self.yearly_spending()
                elif reply[0] == "add_employee":
                    self.add_employee()
                elif reply[0] == "update_employee" and len(reply) == 2:
                    self.update_employee(reply[1])
                elif reply[0] == "delete_employee" and len(reply) == 2:
                    self.delete_employee(reply[1])
                else:
                    print("Wrong command! Try again.")


def main():
    ManageCompany().console()

if __name__ == '__main__':
    main()
