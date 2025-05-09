import sqlite3
file = 'veterinize.db'
connection = sqlite3.connect(file)
print(connection)
cursor = connection.cursor() 
class veterinize:
    def createTables(self):
        query = """
        create table if not exists customers (
            Uid integer primary key autoincrement,
            fname tinytext,
            lname tinytext,
            phone bigint,
            email tinytext,
            address tinytext,
            city tinytext, 
            postalcode tinytext);
        """
        cursor.execute(query)

        q2 = """
        create table if not exists pets (
            Pid integer primary key autoincrement,
            name tinytext,
            type tinytext,
            breed tinytext,
            birthdate tinytext,
            ownerID int);
        """
        cursor.execute(q2)

        q3 = """
        create table if not exists visits (
            Vid integer primary key autoincrement,
            ownerid int,
            petid int,
            details text,
            cost float(16,2),
            paid float(16,2));
        """
        cursor.execute(q3)
    def program(self):
        print("="*34)
        end = False
        while end == False:
            option = input("What would you like to do?\nExit --------------------------- 0\nAdd new customer --------------- 1\nSearch for a customer ---------- 2\nEdit existing customer info ---- 3\n> ")
            if option == "0":
                end = True
            elif option == "1":
                print("Please enter relevant customer information:")
                fname = input("First Name: ")
                lname = input("Last Name: ")
                phone = int(input("Phone Number (no spaces): "))
                email = input("Email: ")
                address = input("Address: ")
                city = input("City: ")
                postalcode = input("Postal Code: ")
                query = f"insert into customers (fname,lname,phone,email,address,city,postalcode) values ('{fname}','{lname}','{phone}','{email}','{address}','{city}','{postalcode}');"
                print("Customer added")
                cursor.execute(query)
                connection.commit()
            elif option == "2":
                print("-"*34)
                userInfo = ["Uid", "fname", "lname", "phone", "email", "address", "city", "postalcode"]
                decision = int(input("Search for existing customer by:\nUid ---------------------------- 1\nFirst Name --------------------- 2\nLast Name ---------------------- 3\nPhone Number ------------------- 4\nEmail -------------------------- 5\nAddress ------------------------ 6\nCity --------------------------- 7\nPostal Code -------------------- 8\nExit --------------------------- 0\n> "))
                if int(decision) == 0:
                    end = True
                elif 1 <= int(decision) <= 8:
                    Uinfo = input("Please enter the corresponding info (ex. if you chose name, enter name):\n> ")
                    cursor.execute(f"select * from customers where {userInfo[decision-1]}='{Uinfo}'")
                    print(cursor.fetchall())
                else:
                    print("That is not a valid input.")
            elif option == "3":
                Done = False
                userInfo = ["Uid", "fname", "lname", "phone", "email", "address", "city", "postalcode"]
                id = int(input("Enter Uid of the customer whose info you would like to edit:\n> "))
                if id >= 1:
                    while Done == False:
                        cursor.execute(f"select * from customers where Uid ='{id}'")
                        print(cursor.fetchall())
                        changeType = input("What information would you like to change?\nFirst Name: 1\nLast Name: 2\nPhone Number: 3\nEmail: 4\nAddress: 5\nCity: 6\nPostal Code: 7\nExit: 0\n> ")
                        if str(changeType) == "0":
                            Done = True
                        elif 7 >= int(changeType) >= 1:
                            changedInfo = input("Please enter appropriate updated information: ")
                            cursor.execute(f"update customers set {userInfo[int(changeType)]}='{changedInfo}' where Uid='{id}'")
                        else: 
                            print("That is not a valid input.")
                        connection.commit()
                else:
                    print("That is not a valid input.")
            else:
                print("That is not a valid input.")
run = veterinize()
run.createTables()
run.program()
print("="*34)

