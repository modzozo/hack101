import sqlite3

class ManageCompany():

    def __init__(self):
        self.connect = sqlite3.connect("company.db")
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()


    def list_employees(self):

        exe = self.cursor.execute('''SELECT name, position FROM employees''')
        for row in exe:
            print("{} - {}".format(row["name"], row["position"]))


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

    def update_employee(self):
        pass
    def delete_employee(self):
        pass


    def console(self):
        while True:
            command = input("\nEnter command>")

            if command == "list_employees":
                self.list_employees()
            elif command ==  "monthly_spending":
                self.monthly_spending()
            elif command == "add_employee":
                self.add_employee()
            elif command == "update_employee":
                self.update_employee()
            elif command == "delete_employee":
                self.delete_employee()
            elif command == "exit":
                break
            else:
                print("Wrong command. Try again")


def main():
    ManageCompany().console()

if __name__ == '__main__':
    main()
