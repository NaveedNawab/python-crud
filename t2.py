import json

# Add a New Record


def add_new_record():
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    if type(data) is dict:
        data = [data]
    name = input("Enter Your name")
    email = input("Enter you email")
    team = {"name": name, "email": email}
    with open('data.json', 'w') as data_file:
        data.append(team)
        json.dump(data, data_file)


# Update a Record

def update_record():
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
    while True:
        print("press 1 to update your name")
        print("press 2 update your email")
        print("Press 3 to exit update record session")
        update_data = int(input(""))
        if update_data == 1:
            old_name = input("Enter your old name to Update data")
            for element in data:
                if element['name'] == old_name:
                    nam = element
                    print(nam)
                    for item in nam:
                        print(item, nam[item])
                        if nam[item] == old_name:
                            new_name = input("Enter your new name")
                            nam[item] = new_name
                            break
        if update_data == 2:
            old_email = input("enter your old email")
            for element in data:
                if element['email'] == old_email:
                    nam = element
                    print(nam)
                    for item in nam:
                        print(item, nam[item])
                        if nam[item] == old_email:
                            new_email = input("Enter your new Email")
                            nam[item] = new_email
        elif update_data == 3:
            break
    with open('data.json', 'w') as data_file:
        data = json.dump(data, data_file)

# View all Records


def view_all_records():
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
    for element in data:
        print(element)
    with open('data.json', 'w') as data_file:
        data = json.dump(data, data_file)


# View a  single Record

def view_single_record():
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
    name = input("Enter name to view a single recordl")
    for element in data:
        if element['name'] == name:
            nam = element
            print(nam)
    with open('data.json', 'w') as data_file:
        data = json.dump(data, data_file)


# Delete a Record

def deleterecord():
    print("function")


# Calling Functions
while(True):
    print("Press 1 to Add a new record")
    print("Press 2 to Update a record")
    print("Press 3 to View all records")
    print("Press 4 to View a single record")
    print("Press 5 to Exit ")

    number = int(input(""))
    if number == 1:
        add_new_record()
    elif number == 2:
        update_record()
    elif number == 3:
        view_all_records()
    elif number == 4:
        view_single_record()
    elif number == 5:
        break
