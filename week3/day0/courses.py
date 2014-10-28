import requests
import random
import json


def get_students():
    try:
        students = requests.get('https://hackbulgaria.com/api/students/', verify=False)
        return students
    except students.exceptions.RequestException as e:
        print(e)
        sys.exit(1)




def get_courses():
    students = get_students()
    courses = []
    for course in range(len(students.json())):
        for name in range(len(students.json()[course]["courses"])):
            courses.append(students.json()[course]["courses"][name]["name"])
    courses = list(set(courses))
    return courses


def print_get_courses():

    for number, name_of_course in enumerate(get_courses()):
        print("[" + str(number) + "] " + name_of_course)


def match_teams(course_id, team_size, group_time):
    students = get_students()
    all_students_of_a_course = []
    courses = get_courses()
    for course in range(len(students.json())):
        for name in range(len(students.json()[course]["courses"])):
            if students.json()[course]["courses"][name]["name"] == courses[course_id] and students.json()[course]["courses"][name]["group"] == group_time:
                if students.json()[course]["available"] is True:
                    all_students_of_a_course.append(students.json()[course]["name"])

    while len(all_students_of_a_course) > 0:
        print("========================================")
        for i in range(team_size):
            if len(all_students_of_a_course) > 0:
                random_number = random.randrange(len(all_students_of_a_course))
                print(all_students_of_a_course[random_number])
                all_students_of_a_course.remove(all_students_of_a_course[random_number])
        print("========================================")
    return True


def console():
    print("Hello, you can use one the the following commands:")
    print("list_courses - this lists all the courses that are available now.")
    print("exit - quit the program")
    print("match_teams <course_id>, <team_size>, <group_time>")
    while True:
        command = input("Enter command>")
        if command == "list_courses":
            print_get_courses()
        elif command.split()[0] == "match_teams":
            command = command.split()
            match_teams(int(command[1]), int(command[2]), int(command[3]))
        elif command == "exit":
            break
        else:
            print("Please enter one of the two options")

if __name__ == '__main__':
    console()
