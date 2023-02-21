#=====importing libraries===========
from datetime import datetime


# Opening user_txt reading it and storing the content in variable called user_lines
usertxt_file = open('user.txt', 'r+', encoding='utf-8')  # Open the user txt file
user_lines = usertxt_file.readlines()        # reading lines and storing them in a list
# print(lines)
usertxt_file.close()  # Close files


#Opening tasks_txt, reading it and storing the content in variable called tasks_line
taskstxt_file = open('tasks.txt', 'r+', encoding='utf-8')  # Open the tasks txt file
tasks_lines = taskstxt_file.readlines()  # reading lines and storing them in a list
# print(lines)
taskstxt_file.close()  # Close files



# Declaring empty dictionary to store login details
loginDetail_dic = {}

# Declaring empty list to store list of usernames
username_list = []

# Looping through the lines and storing user and password in dic format for letter login validation
for user_line in user_lines:
    user_line = user_line.strip()
    user_line = user_line.split(", ")
    username_i = user_line[0].strip(",")
    password_i = user_line[1]

    # Adding values to loginDetail_dic
    loginDetail_dic[username_i] = password_i

    # Adding values to username_list
    username_list.append(username_i)

loginDetail_dic
username_list
# print(loginDetail_dic)
# print(username_list)



# ====Login Section====

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your username and password.
'''
# Requesting username and storing it in a variable called username
username = input("Username: ")

login_success = ""  # This empty variable will store "True" or "False" depending of login success

# Checking if username input is valid first
# if username is not in username list, request for another valid username
# if username is valid then ask for password
while username not in username_list:
    print("\nPlease enter valid username.")
    username = input("Username: ")
else:
    # Requesting password from the user
    password = input("Password: ")

    # Doing password validation here
    # Getting expected password for the user from loginDerail dictionary
    # This value will be used to compare it with the password that user enters
    expected_password = loginDetail_dic[username]
    # print(expected_password)

    # Loop while expected password is equal to password entered return login_success = Ture
    # Otherwise request for valid password
    while expected_password != password:
        print("\nPlease enter correct password.")
        # Requesting password from the user again
        password = input("Password: ")
        if expected_password == password:
            login_success = True
            print("\nSuccessfully logged in!\n")
    else:
        login_success = True
        print("\nSuccessfully logged in!\n")


# When login is successful do the following
while login_success == True:
    # Presenting the menu to the user and
    # making sure that the user input is converted to lower case.

    # Displaying different menu items to the admin vs the rest of the users
    if username == "admin":   # admin user can register a new user or see stats
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - View statistics
e - Exit
: ''').lower()
    else:         # Other users can not register a new user or see stats
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        # Request the user to register a new user
        print("\nRegister new user and assign password to this new user.")
        username_new = input("Enter new username: ")

        # First make sure the new username is not taken
        # If new username is already taken do the following
        # Display username is taken message
        # and ask the user for a different username
        while username_new in username_list:
            print("This username is taken. Please enter a different username.")
            username_new = input("\nEnter new username: ")

        # If username is unique do the following
        # Ask the user to input a password and confirm password
        else:
            # Requesting inputs(password and confirm_password)
            password_new = input("Assign password for the new username: ")
            confirm_password = input("Confirm the password: ")

            # Confirming if new password and confirm password are the same
            # If passwords don't match display passwords didn't match message
            # Otherwise print user registration successful and
            # write the new user login info into user.txt file
            # Then open and read the user.txt file and update the username_list value for later use
            while password_new != confirm_password:
                # If password and confirm_password don't match
                print("\nPasswords didn't match! Please try again.")
                password_new = input("Assign password for the new username: ")
                confirm_password = input("Confirm the password: ")
            else:
                # If password and confirm_password match
                # opening/creating a file called user.txt
                ofile = open('user.txt', 'a')

                # Formatting text before writing it on the file
                newUserDetail = "\n" + username_new + ", " + password_new

                ofile.write(newUserDetail)  # writing new user login detail into user.txt file

                # Closing the file once done
                ofile.close()
                print("\nSuccessfully registered a new user and password!\n")

                '''
                 After successfully registering a new user and password. To include the newly added user, 
                 we will open and read the user.txt again and update the username_list value. This will be very 
                 helpful when the user is trying to assign a task to the new user they just registered.
                '''
                # Opening user_txt, reading it and storing the content in variable called user_line
                usertxt_file = open('user.txt', 'r+', encoding='utf-8')  # Open the user txt file
                user_lines = usertxt_file.readlines()  # reading lines and storing them in a list
                # print(lines)
                usertxt_file.close()  # Close files

                # Declaring empty list to store list of usernames
                username_list = []
                for user_line in user_lines:
                    user_line = user_line.strip()
                    user_line = user_line.split(", ")
                    username_i = user_line[0].strip(",")

                    # Adding values to username_list
                    username_list.append(username_i)

                username_list
                # print(username_list)

    elif menu == 'a':
        '''
         Request for the following: 
         Input: username (only from existing username list) from the user
         The tile of the task, A description of the task and the due date of the task.
         Also include current date and Status of the task (complete or not). 
         After successfully adding a task open and read tasks.txt file and update tasks_lines list for later use
         by va - view all tasks and s - view statistics
         '''
        # Request username from existing users
        username_a = input("\nAdd a task and assign it to a user\nUsername: ")

        # First check the username is valid;
        # if invalid username is entered ask for a valid username again.
        while username_a not in username_list:
            print("Please enter a valid username.")
            username_a = input("Enter username: ")
        # If valid username is entered continue to do the following
        else:
            # Request for the following
            # The tile of the task
            task_title = input("Task title: ")

            # A description of the task
            descriptionOf_task = input("Description of the task: ")

            # And the due date of the task
            due_date = input("What is the due date (day/month/year): ")

            # Other inputs
            # Current date
            current_date = datetime.today().strftime(
                '%d/%m/%y')  # https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

            # Status of the task Default "NO"
            statusOf_task = "No"

            # opening a file called tasks.txt
            taskfile = open('tasks.txt', 'a')

            # Formatting the input before writing them into task.txt
            taskDetail = "\n" + username_a + ", " + task_title + ", " + descriptionOf_task + ", " + str(
                current_date) + ", " + due_date + ", " + statusOf_task
            # print(taskDetail)

            # writing tasks detail into tasks.txt file
            taskfile.write(taskDetail)

            # Closing the file once done
            taskfile.close()
            print("\nSuccessfully added a task!\n")

            '''
             After successfully adding a task and assigning it to a valid user. To include the newly added task in the
             following actions, will open and read the tasks.txt again. This wil be very helpful when displaying 
             "all tasks" and "stats". It will be updated right after successfully adding a task
            '''
            # Opening tasks_txt, reading it and storing the content in variable called tasks_line
            taskstxt_file = open('tasks.txt', 'r+', encoding='utf-8')  # Open the tasks txt file
            tasks_lines = taskstxt_file.readlines()  # reading lines and storing them in a list
            # print(lines)
            taskstxt_file.close()  # Close files



    elif menu == 'va':
        # First check if there is a data to display. If there is none, print "No task to show"
        if len(tasks_lines) == 0:
            print("\n-------------------------------------------------------------------------------------------\n")
            print("No task to show")
            print("\n-------------------------------------------------------------------------------------------\n")
        # If there is data to display do the following.
        else:
            # Looping through the lines and getting values from each line
            # Split the line where there is comma and space.
            for tasks_line in tasks_lines:
                # Going through each line and putting the strings in a list format
                tasks_line = tasks_line.strip()  # i.e  admin, Register Users with taskManager.py,..., No
                tasks_line = tasks_line.split(", ")  # i.e ['admin', ' Register Users with taskManager.py',....,  ' 20 Oct 2019', ' No']

                # Printing dotted lines between each task details
                print("\n-------------------------------------------------------------------------------------------\n")
                # Then using index we going to print the necessary strings out
                # We make the out put more readable.
                print("Task:                    \t", tasks_line[1])
                print("Assigned to:             \t", tasks_line[0])
                print("Date assigned:           \t", tasks_line[3])
                print("Due date:                \t", tasks_line[4])
                print("Task Complete?           \t", tasks_line[5])
                print("Task description: \n", tasks_line[2])
                print("\n-------------------------------------------------------------------------------------------\n")


    elif menu == 'vm':
        '''
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print output'''

        for tasks_line in tasks_lines:
            # Only deal will lines of data where the username is == to the current username
            # Split the line where there is comma and space.
            if username in tasks_line:
                # print(tasks_line)
                tasks_line = tasks_line.strip()
                # print(tasks_line)
                tasks_line = tasks_line.split(", ")
                # print(tasks_line)

                # Printing dotted lines between each task details
                print("\n-------------------------------------------------------------------------------------------\n")
                # Then using index we going to print the necessary strings out
                # We make the output more readable.
                print("Task:                    \t", tasks_line[1])
                print("Assigned to:             \t", tasks_line[0])
                print("Date assigned:           \t", tasks_line[3])
                print("Due date:                \t", tasks_line[4])
                print("Task Complete?           \t", tasks_line[5])
                print("Task description: \n", tasks_line[2])
                print("\n-------------------------------------------------------------------------------------------\n")


        # If the user has no task display "no task message"
        # empty variable list to put users that are assigned with task
        busy_users = []

        # Looping through all the valid users
        for user in username_list:
            # Looping through each line in tasks.txt file
            for tasks_line in tasks_lines:
                # Check if user in username_list is assigned with task
                if user in tasks_line:
                    # If true we add the user into the empty list: busy_users
                    busy_users.append(user)

        # Then we identify unique users in the busy_users list
        set(busy_users)
        # check if the user that is logged in now has tasks assigned to them or not
        if username not in busy_users:
            print("\n-------------------------------------------------------------------------------------------\n")
            print("You have no task assigned to you, yet!")
            print("\n-------------------------------------------------------------------------------------------\n")


    elif menu == 's':
        print("\nTasks and users Statistics: \n")
        print("\n-------------------------------------------------------------------------------------------\n")

        # Total number of tasks
        totalNumberOf_tasks = len(tasks_lines)

        # Total number of users
        totalNumberof_users = len(user_lines)

        # Total number of users that are and are not assigned with any task
        busy_users = []  # empty variable list to put users that are assigned

        # Looping through all the valid users
        for user in username_list:
            # Looping through each line in tasks.txt file
            for tasks_line in tasks_lines:
                # Check if user in username_list is assigned with task
                if user in tasks_line:
                    # If true we add the user into the empty list: busy_users
                    busy_users.append(user)

        # Then we count only the unique users in the busy_users list
        busy_users = len(set(busy_users))
        # Here we minus busy users number from the total users
        idle_users = totalNumberof_users - busy_users

        # printing some stats
        print("Details of tasks\n")
        print("Total number of tasks: " + str(totalNumberOf_tasks)+"\n")
        print("\n-------------------------------------------------------------------------------------------\n")

        print("Details of users\n")
        print("Total number of users: " + str(totalNumberof_users))

        print("Total number of idle users: " + str(idle_users))
        print("Total number of busy users: " + str(busy_users))

        print("\n-------------------------------------------------------------------------------------------\n")


    # When users selects "e" display "Goodbye" message and exit loop
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    # If they enter the wrong selection display this
    # Expected selections (r, a, va, vm, s and e) for admin
    # and (a, va, vm and e) for other users
    else:
        print("\nYou have made a wrong choice, Please Try again\n")


