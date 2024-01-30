import csv
def input1():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    age = int(input("How old are you?"))
    grade = int(input("What grade are you in?"))
    gpa = float(input("What is your GPA?"))
    inp = {"first_name":first_name, "last_name":last_name, "age":age, "grade":grade, "gpa":gpa}
    return inp

def input2(file_path):
    team_name = input("What is the name of your favorite sports team?")
    city = input("What city is your team from?")
    num_champ = int(input("How many championships does your team have?"))
    year_found = int(input("What year was the team founded?"))
    last_year = int(input("what year was the last time the team won a championship?"))
    fieldnames = ["favorite sports team name", "name of city", "number of championships", "year founded", "last year championship won"]
    inp = {"favorite sports team name":team_name, "name of city":city, "number of championships":num_champ, "year founded":year_found, "last year championship won":last_year}
    with open(file_path, "w") as fileName:
        writer = csv.DictWriter(fileName, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow(inp)
    return inp

def read_csv_as_dict(file_path):
    data_list = []
    
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            data_list.append(dict(row))
            
    return data_list

def main():
    inp = {}
    inp = input1()
    print(inp)
    input2("file.csv")
    print(read_csv_as_dict("file.csv"))

main()