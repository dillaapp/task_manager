# =====importing libraries===========
import copy
from datetime import datetime


# ####################### FUNCTIONS START ##################################


##### Reading and writing on files functions START ############
def read_file(file_name):
    """
     read_file, function that reads external file  and stores them as a list
     Values in each line is seen as one list element
     Input = file name """

    input_file = open(file_name, 'r+', encoding='utf-8')  # Open the file
    input_lines = input_file.readlines()  # reading lines and storing them in a list
    return input_lines  # returns the list
    input_file.close()  # Close files


def write_On_file(OFile_name, write_values):
    """
     write_On_file, function that writes values in each line of an output file
     inputs = output file name and Value you want to write
     output = writes a line of value onto output file """

    output_file = open(OFile_name, 'a')  # Opening the output file
    output_file.write(write_values)  # writing values into output file
    # Closing the file once done
    output_file.close()


##### Reading and writing on files functions END ############


##### Dealing with user text file functions START ###########
def get_user_list(file_name):
    """
     get_user_list, function to get the list of all users from user.txt file
     input: file_name
     output: List of users """

    # Opening user_txt reading it and storing contents in variable called user_lines
    user_lines = read_file(file_name)

    # Declaring empty list to store list of usernames
    username_list = []

    # looping through user_lines list
    for user_line in user_lines:
        user_line = user_line.strip()
        user_line = user_line.split(", ")
        username_i = user_line[0].strip(",")

        # Adding values to username_list
        username_list.append(username_i)
    # print(username_list)
    return username_list


def get_user_login_details_dict(file_name):
    """
     get_user_login_details_dict, function to get a dictionary of user login details from the user.txt file
     input: file_name
     output: dictionary of user login details """

    # Opening user_txt reading it and storing contents in variable called user_lines
    user_lines = read_file(file_name)

    # Declaring empty dictionary to store login details
    loginDetail_dic = {}

    # Looping through the lines and storing user and password in dic format for letter login validation
    for user_line in user_lines:
        user_line = user_line.strip()
        user_line = user_line.split(", ")

        username_i = user_line[0].strip(",")
        password_i = user_line[1]

        # Adding values to loginDetail_dic
        loginDetail_dic[username_i] = password_i

    # print(loginDetail_dic)
    return loginDetail_dic


def verify_username(user_file_name, username_):
    valid_username = ""
    if username_ in get_user_list(user_file_name):
        valid_username = username_
        return valid_username
    else:
        while username_ not in get_user_list(user_file_name):
            print("\nPlease Enter a valid username!")
            username_ = input("Username: ")
            if username_ in get_user_list("user.txt"):
                valid_username += username_
                break
        return valid_username




def verify_password(file_name, username_):
    """
     verify_password, function to verify if user name and password is correct
     inputs: file name and username
     output: requests for password from the user (if username is correct), returns login_success true if
     password is also correct """

    # Get user login detail dictionary
    loginDetail_dic = get_user_login_details_dict(file_name)

    # Requesting password from the user
    password = input("Password: ")

    # Doing password validation here
    # Getting expected password for the user from loginDerail dictionary
    # This value will be used to compare it with the password that user enters
    expected_password = loginDetail_dic[username_]


    # Loop while expected password is equal to password entered return login_success = Ture
    # Otherwise request for valid password
    while expected_password != password:
        print("\nPlease enter correct password.")
        # Requesting password from the user again
        password = input("Password: ")
        if expected_password == password:
            login_success = True
            return login_success
            print("\nSuccessfully logged in!\n")
    else:
        login_success = True
        return login_success
        print("\nSuccessfully logged in!\n")


def menu(username_):
    """
     menu, function to display menu to users depending on if they are admin or just another user
     input: username
     output: menu details """

    if username_ == "admin":  # admin user can register a new user or see stats
        admin_menu = input('''\nSelect one of the following Options below:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
        return admin_menu
    else:  # Other users can not register a new user or see stats
        user_menu = input('''\nSelect one of the following Options below:
a - adding a task
va - view all tasks
vm - view my task
e - exit
: ''').lower()
        return user_menu


def register_new_user(user_file_name):
    """
     register_new_user, function to register new users
     input: new username and password
     output: new user successfully registered , user.txt updated """

    # Request the user to register a new user
    print("\nRegister new user and assign password to this new user.")
    username_new = input("Enter new username: ")

    # First make sure the new username is not taken
    # If new username is already taken do the following
    # Display username is taken message
    # and ask the user for a different username
    username_list = get_user_list(user_file_name)
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
            # Formatting text before writing it on the file
            newUserDetail = "\n" + username_new + ", " + password_new
            write_On_file(user_file_name, newUserDetail)  # writing new user login detail into user.txt file

            print("\nSuccessfully registered a new user and password!\n")


##### Dealing with user text file functions END ###########

##### Dealing with task file functions START ######

def get_busy_users_list(user_file_name, tasks_file_name):
    """
     get_busy_users_list, function to get a list of users are are assigned with task
     inputs: user file name and tasks file name
     output: usernames that have tasks assigned to them """

    # Open and read tasks.txt and store the contents in a list called task_lines
    tasks_lines = read_file(tasks_file_name)
    # print(tasks_lines)

    # We run "get_user_list" function to get username list form users.txt
    username_list = get_user_list(user_file_name)

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
    return set(busy_users)


def view_all_tasks(file_name):
    """
     view_all_tasks, function to display all tasks from tasks.txt file
     input: file name
     output: prints tasks in a user friendly way  ; if there is no task, it will display no tasks
    """

    # Open and read tasks.txt and store the contents in a list called task_lines
    tasks_lines = read_file(file_name)
    # print(tasks_lines)

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
            tasks_line = tasks_line.split(", ")  # i.e ['admin', ' Register Users with taskManager.py',....,
            # ' 20 Oct 2019', ' No']

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


def get_my_tasks(tasks_file_name, username_):
    """
    get_my_task, function will fitch only tasks assigned to particular user and return a list of those tasks
    input: tasks file name and username
    output: a list of tasks assigned the particular user
    """
    # Read tasks.txt fine
    tasks_lines = read_file(tasks_file_name)

    my_tasks = []  # empty my_tasks list
    for task_line in tasks_lines:
        # Only deal will lines of data where the username is == to the current username
        # Split the line where there is comma and space.

        if (username_ + ",") in task_line:
            task_line = task_line.strip()
            my_tasks.append(task_line)
    # print(my_tasks)
    return my_tasks


def view_my_tasks(tasks_file_name, username_):
    """
      view_my_tasks, function to display all my tasks from tasks.txt file
      input: file name, username
      output: prints my tasks in a user friendly way ; if there is no task, it will display no tasks """

    # Fetch the user's tasks
    my_tasks = get_my_tasks(tasks_file_name, username_)
    print(username_)

    # First check if the user that is logged in now has tasks assigned to them or not
    if len(my_tasks) == 0:
        print("\n-------------------------------------------------------------------------------------------\n")
        print("You have no task assigned to you, yet!")
        print("\n-------------------------------------------------------------------------------------------\n")
    # If there is data to display do the following.
    else:
        for task, task_index in zip(my_tasks, range(len(my_tasks))):
            # Split the line where there is comma and space.
            task = task.strip()
            # print(task)
            task = task.split(", ")
            # print(task)

            # Printing dotted lines between each task details
            print("\n-------------------------------------------------------------------------------------------\n")
            # Then using index we going to print the necessary strings out
            # We make the output more readable.
            print("Task " + str((task_index + 1)) + ":                       \t", task[1])
            print("Assigned to:                   \t", task[0])
            print("Date assigned:                 \t", task[3])
            print("Due date:                      \t", task[4])
            print("Task Complete?                 \t", task[5])
            print("Task description: \n", task[2])
            print("\n-------------------------------------------------------------------------------------------\n")


def edit_task_in_tasks_file(tasks_file_name, task_to_update, index_num, update_value):
    """
    This function edits tasks in task file
    :param task_to_update: a line (in a list format) task to updated
    :param index_num:  the index of the list element we want to change
    :param update_value:  The value we want to add instead of the old one
    :return: edits the task_file with the changes
    """
    edited_task = copy.deepcopy(task_to_update)
    edited_task[index_num] = update_value
    # print(edited_task)
    # print(task_to_update)
    join_after_edit = ", ".join(edited_task)
    # print(join_after_edit)
    join_selected_task = ", ".join(task_to_update)
    # print(join_selected_task)

    # Getting all the tasks from task.txt file
    tasks_lines = read_file(tasks_file_name)
    all_tasks = []
    for tasks_line in tasks_lines:
        # Going through each line and putting the strings in a list format
        tasks_line = tasks_line.strip()
        all_tasks.append(tasks_line)

    all_tasks

    # print(all_tasks)
    # Removing the old task detail
    all_tasks.remove(join_selected_task)
    # Adding the edited task detail
    all_tasks.append(join_after_edit)
    # print(all_tasks)
    # First clear the tasks file
    open(tasks_file_name, "w").close()
    # Updating the task.txt file for later use
    for task in all_tasks:
        write_On_file(tasks_file_name, str(task) + "\n")


def mark_complete(tasks_file_name, user_file_name, username_, selected_task):
    """
    marks a task complete or not complete
    :param tasks_file_name: tasks.txt file
    :param user_file_name:  user.txt file
    :param username_:    username of the user that is logged in
    :param selected_task:  The selected list (task detail in a list format)
    :return: updates the task status based on the user input (yes or no) by running edit_task_in_tasks_file function
    """
    # If user selects mt to mark task complete
    # Require input(Yes/No) from the user and store the value in a variable called complete
    complete = input("\nIs your task complete? \"Yes\" or \"No\" (Enter \"stp\" to exit):  ").lower()

    while complete != "stp":
        # If user inputs yes or no run the function "edit_task_in_tasks_file
        if complete == "yes" or complete == "no":
            # 5 is the index of the due date element in task list
            edit_task_in_tasks_file(tasks_file_name, selected_task, 5, complete)

            # After editing give users another selection
            select_task_num(tasks_file_name, user_file_name, username_)
            break
        # If user selects stp exit the loop
        elif complete == "stp":
            exit()
        else:
            # If user inputs invalid selection ...ask the user to put a valid selection
            print("\nEnter valid selection")
            complete = input("\nIs your task complete? \"Yes\" or \"No\" (Enter \"stp\" to exit):  ").lower()


def edit_due_data_and_username(user_file_name, tasks_file_name, selected_task, username_):
    """
    Edits the due date and username of a task that is not complete
    :param selected_task: The selected list (task detail in a list format)
    :param tasks_file_name: tasks.txt file
    :param user_file_name:  user.txt file
    :param username_:  username of the user that is logged in
    :return: updated the due date and username based on the user input and running edit_task_in_tasks_file function
    """
    # If user selects "et" to edit username and due date of the task
    # First check if the task is complete. If the task is complete we display task can not be edited
    if "yes" in selected_task:
        print("\nThis task is complete. It can not be edited.")
        select_task_num(tasks_file_name, user_file_name, username_)

    else:
        # If the task is not complete
        # Require input (select between "usn" for username and "dd" for due data)
        edit_task_content = input(
            "\nEnter \"usn\" to edit the \"username\" or enter \"dd\" to edit the \"due date\" (Enter \"stp\" to exit): ")

        while edit_task_content != "stp":
            # If user selects "usn"
            if edit_task_content == "usn":
                # Request username from the username list
                username_ = input("Enter new username: ")

                # Run "get_user_list' function to get the list of usernames
                username_list = get_user_list(user_file_name)

                # If the new username is not in the username list
                # display "please enter valid username" and ask the user to try another time

                valid_username = verify_username(user_file_name, username_)
                # 0 is the index of the due date element in task list
                edit_task_in_tasks_file(tasks_file_name, selected_task, 0, valid_username)
                """
                while username_ not in username_list:
                    print("\nPlease enter valid username.")
                    username_ = input("Enter new username: ")

                    # If the new username is in the list run "edit_task_in_tasks_file" function
                    if username_ in username_list:
                        # 0 is the index of the due date element in task list
                        edit_task_in_tasks_file(tasks_file_name, selected_task, 0, username_)
                        break"""
                # After editing give users another selection
                select_task_num(tasks_file_name, user_file_name, username_)
                break

            elif edit_task_content == "dd":
                # If user selects "dd" to edit the due date
                # Request for new due date from the user
                due_date = input("\nEnter the new due date: ")

                # Then run the "edit_task_in_tasks_file" function
                # 4 is the index of the due date element in task list
                edit_task_in_tasks_file(tasks_file_name, selected_task, 4, due_date)
                # After editing give users another selection
                select_task_num(tasks_file_name, user_file_name, username_)
                break

            elif edit_task_content == "stp":
                # If  user selects "stp" exit loop
                exit()

            else:
                # If user inputs invalid selection display message ask the user to try another time
                print("\nSelect valid selection.")
                edit_task_content = input(
                    "Enter \"usn\" to edit the \"username\" or enter \"dd\" to edit the \"due date\" (Enter \"stp\" to exit): ")


def edit_task(tasks_file_name, user_file_name, username_, task_num):
    """
    runs functions "mark_complete" and "edit_due_data_and_username" based on user's selection
    :param tasks_file_name: tasks.txt file
    :param user_file_name:  user.txt file
    :param username_:  username of the user that is logged in
    :param task_num: the task number of the task you want to edit
    :return: calls the right function depending on the user input
    """
    # Get a list of task related to that user
    my_tasks = get_my_tasks(tasks_file_name, username_)

    selected_index = task_num - 1  # to account for list index starting from 0 not 1

    # The task to edit
    selected_task = my_tasks[selected_index]
    # print(selected_task)

    # To edit some part of the selected task we will split them store them in list format in variable called selected_task
    selected_task = selected_task.split(", ")
    # print(selected_task)

    select_edit_type = input(
        "\nEnter \"mt\" to update task status or enter \"et\" to edit the task (Enter \"stp\" to go back):-\nEnter here: ").lower()

    while select_edit_type != "stp":
        if select_edit_type == "mt":
            mark_complete(tasks_file_name, user_file_name, username_, selected_task)
            break

        elif select_edit_type == "et":
            edit_due_data_and_username(user_file_name, tasks_file_name, selected_task, username_)
            break

        elif select_edit_type == "stp":
            return select_task_num(tasks_file_name, user_file_name, username_)
            break

        else:
            print("\nSelect valid selection.")
            select_edit_type = input(
                "\nEnter \"mt\" to update task status or enter \"et\" to edit the task (Enter \"stp\" to go back):-\nEnter here: ").lower()


def select_task_num(tasks_file_name, user_file_name, username_):
    """This function is to select with task number the user wants to edit. User inputs -1 to exit"""
    # display tasks that are assigned to the user
    # view_my_tasks(tasks_file_name, username_)   # i didnt go through with it becuase it wasn't make sense in UI terms

    task_num = int(input("\nThe task number you want to edit (Enter -1 to exit): "))
    while task_num != -1:
        edit_task(tasks_file_name, user_file_name, username_, task_num)
        break
        if task_num == -1:
            break


def generate_task_overview_report(tasks_file_name):
    """This function is to generate task_overview report and store it on task_overview txt file
    input: task file name
    output: report generated on task_overview.txt file"""

    # All tasks in list format stored in variable called tasks
    tasks = read_file(tasks_file_name)

    task_overview_print = "Task overview report:\n"
    # Total number of tasks
    total_num_tasks = len(tasks)
    total_num_tasks_print = "\nTotal number of tasks: " + str(total_num_tasks) + "\n"

    # Write the results on teas file called task_overview
    # First clear the file
    open("task_overview.txt", "w").close()
    write_this_1st = task_overview_print + total_num_tasks_print
    write_On_file("task_overview.txt", write_this_1st)

    complete_tasks = []
    incomplete_tasks = []
    overdue_task_incomplete = []
    for task in tasks:
        if ", yes" in task:
            task = task.strip()
            complete_tasks.append(task)
        else:
            task = task.strip()
            incomplete_tasks.append(task)
            task = task.split(", ")
            due_date = task[4]
            if datetime(int(due_date[6:]), int(due_date[3:5]), int(due_date[:2])) < datetime.now():
                overdue_task_incomplete.append(task)
    # Total number of completed tasks
    total_num_complete_task = len(complete_tasks)
    total_num_complete_task_print = "Total number of completed tasks: " + str(total_num_complete_task) + "\n"

    # Total number of incompleted tasks
    total_num_incomplete_task = len(incomplete_tasks)
    total_num_incomplete_task_print = "Total number of incomplete tasks: " + str(total_num_incomplete_task) + "\n"

    # Total number of uncompleted tasks and that are overdue
    total_num_overdue_tasks = len(overdue_task_incomplete)
    total_num_overdue_tasks_print = "Total number of overdue tasks: " + str(total_num_overdue_tasks) + "\n"

    # the percentage of tasks that are incomplete
    incomplete_tasks_percent = round((total_num_incomplete_task / total_num_tasks) * 100, 2)
    incomplete_tasks_percent = "The percentage of tasks that are incomplete: " + str(incomplete_tasks_percent) + " %\n"

    # the percentage of tasks that are overdue
    overdue_tasks_percent = round((total_num_overdue_tasks / total_num_tasks) * 100, 2)
    overdue_tasks_percent = "The percentage of tasks that are overdue: " + str(overdue_tasks_percent) + " %\n"

    # Write the results on text file called task_overview
    write_this_2nd = total_num_complete_task_print + total_num_incomplete_task_print + total_num_overdue_tasks_print + incomplete_tasks_percent + overdue_tasks_percent
    write_On_file("task_overview.txt", write_this_2nd)


def generate_user_overview_report(user_file_name, tasks_file_name):
    """This function is to generate user_overview report and store it on user_overview txt file
        input: user file name and tasks file name
        output: report generated on user_overview.txt file"""
    # All users details in list format stored in variable called users
    users = read_file(user_file_name)

    # All tasks in list format stored in variable called tasks
    tasks = read_file(tasks_file_name)

    user_overview_print = "User overview report:\n"
    # print(user_overview_print)

    # The total number of users registered with task_managers.py
    total_num_users = len(users)
    total_num_users_print = "\nTotal number of users registered: " + str(total_num_users) + "\n"

    # The total number of tasks that have been generated and tracked using task_manager.py
    total_num_tasks = len(tasks)
    total_num_tasks_print = "Total number of tasks: " + str(total_num_tasks) + "\n"

    # Write the results on text file called user_overview
    # First clear the file
    open("user_overview.txt", "w").close()
    write_this_1st = user_overview_print + total_num_users_print + total_num_tasks_print
    write_On_file("user_overview.txt", write_this_1st)

    # for each user
    # The total number of tasks assigned to that user
    # First a list of all users assigned with tasks
    usernames_with_task_list = get_busy_users_list(user_file_name, tasks_file_name)

    for username_ in usernames_with_task_list:
        my_tasks = []  # empty my_tasks list
        for task in tasks:
            # Only deal will lines of data where the username is == to the current username
            # Split the line where there is comma and space.

            if (username_ + ",") in task:
                task = task.strip()
                my_tasks.append(task)
        # print(my_tasks)

        # Print username
        username_print = "\nFor username, " + username_ + " :- \n"
        #print(username_print)

        # Total number of tasks assigned to per use
        task_by_user = "Total tasks assigned: " + str(len(my_tasks)) + "\n"
        # print(task_by_user)

        # The percentage of the total number of tasks that have been assigned to that user
        task_percent_by_user = round((len(my_tasks) / total_num_tasks) * 100, 2)
        task_percent_by_user = "Percentage of the total tasks assigned: " + str(task_percent_by_user) + " %\n"
        # print(task_percent_by_user)

        # completed my_task
        my_tasks_complete = []
        my_tasks_incomplete = []
        overdue_task_incomplete = []
        for task in my_tasks:
            if ", yes" in task:
                task = task.strip()
                my_tasks_complete.append(task)
            else:
                task = task.strip()
                my_tasks_incomplete.append(task)
                task = task.split(", ")
                due_date = task[4]
                if datetime(int(due_date[6:]), int(due_date[3:5]), int(due_date[:2])) < datetime.now():
                    overdue_task_incomplete.append(task)

        # The percentage of tasks assigned to that user that must still be completed
        incomplete_task_percent = round((len(my_tasks_incomplete) / total_num_tasks) * 100, 2)
        incomplete_task_percent = "Percentage of incomplete tasks: " + str(incomplete_task_percent) + " %\n"

        # The percentage of tasks assigned to that user that completed
        complete_task_percent = round((len(my_tasks_complete) / total_num_tasks) * 100, 2)
        complete_task_percent = "Percentage of complete tasks: " + str(complete_task_percent) + " %\n"

        # The percentage of incomplete tasks that are not complete
        overdue_incomplete_task_percent = round((len(overdue_task_incomplete) / len(my_tasks_incomplete)) * 100, 2)
        overdue_incomplete_task_percent = "Percentage of incomplete tasks that are overdue is: " + str(
            overdue_incomplete_task_percent) + " %\n"


        # Write on user_overview txt file
        write_this_2nd = username_print + task_by_user + task_percent_by_user + incomplete_task_percent + complete_task_percent + overdue_incomplete_task_percent
        write_On_file("user_overview.txt", write_this_2nd)

     # The following users have zero task assigned to them
    zero_user_print = "\nThe following users have no task assigned to them:\n"
    write_On_file("user_overview.txt", zero_user_print)

    # Finding users with zero tasks
    users_with_task = usernames_with_task_list
    all_users = get_user_list(user_file_name)
    for user in all_users:
        if user not in users_with_task:
            user = user + "\n"
            write_On_file("user_overview.txt", user)



def get_stats(user_overview_file_name, task_overview_file_name):
    """
    get_stats, function will display the contents of user_overview and task_overview text files
    inputs: task_overview file name and user_overview file name
    output: prints the contents of the file for the user
    """
    # Printing task_overview contents
    task_overview_list = read_file(task_overview_file_name)
    # print(task_overview_list)

    print("-----------------------------------------------------------------")  # printing a line on the top
    for task_overview in task_overview_list:
        task_overview = task_overview.strip()
        print(task_overview)

    # Printing user_overview contents
    print("\n-----------------------------------------------------------------\n")  # printing a line in the middle
    user_overview_list = read_file(user_overview_file_name)
    # print(user_overview_list)
    for user_overview in user_overview_list:
        user_overview = user_overview.strip()
        print(user_overview)

    print("-----------------------------------------------------------------")  # printing a line on the bottom



# assign_task, function to add and assign task to users
def assign_task(user_file_name, tasks_file_name):
    """
    Request for the following:
    Input: username (only from existing username list) from the user
    The tile of the task, A description of the task and the due date of the task.
    Also include current date and Status of the task (complete or not).
    After successfully adding a task open and read tasks.txt file and update tasks_lines list for later use
    by va - view all tasks and s - view statistics """
    # Request username from existing users
    username_a = input("\nAdd a task and assign it to a user\nUsername: ")

    # First check the username is valid;
    # if invalid username is entered ask for a valid username again.
    username_list = get_user_list(user_file_name)
    while username_a not in username_list:
        print("Please enter a valid username.")
        username_a = input("Enter username: ")
    # If valid username is entered continue to do the following
    else:
        # Request for the following
        # The tile of the task
        task_title = input("Task title: ")

        # A description of the task
        task_description = input("Description of the task: ")

        # And the due date of the task
        due_date = input("What is the due date (day/month/year): ")

        # Other inputs
        # Current date
        current_date = datetime.today().strftime(
            '%d/%m/%y')  # https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

        # Status of the task Default "NO"
        task_status = "No"

        # Formatting the input before writing them into task.txt
        task_detail = "\n" + username_a + ", " + task_title + ", " + task_description + ", " + str(
            current_date) + ", " + due_date + ", " + task_status
        # print(taskDetail)

        # writing tasks detail into tasks.txt file
        write_On_file(tasks_file_name, task_detail)

        print("\nSuccessfully added a task!\n")


##### Dealing with task file functions START ######

# ####################### FUNCTIONS END ##################################


# ====Login Section====
# Requesting username and storing it in a variable called username
username = input("Username: ").lower()

# validating if username is already registered
valid_username = verify_username("user.txt", username)

# Validate login details
# Run "verify_password" function store the outcome(Ture) on variable called login_success
login_success = verify_password("user.txt", valid_username)

# When login is successful do the following
while login_success == True:
    # Presenting the customized menu to the user
    # menu content will be different based on the user
    menu_ = menu(valid_username)

    # If user selects "r" for registering new user
    if menu_ == "r":
        # run "register_new_user function
        register_new_user("user.txt")

    # If user selects "a" for adding and assigning a task
    elif menu_ == "a":
        # Run "assign_task" function
        assign_task("user.txt", "tasks.txt")

    # If user selects "va" for viewing all tasks
    elif menu_ == "va":
        # run "view_all_tasks" function
        view_all_tasks("tasks.txt")

    # If user selects "vm" for viewing only tasks assigned to them
    elif menu_ == "vm":
        # run "view_my_tasks" function
        view_my_tasks("tasks.txt", valid_username)
        # run select_task_num
        select_task_num("tasks.txt", "user.txt", valid_username)

    # If user selects "gr" generate report on task_overview and user_overview files
    elif menu_ == "gr":
        # Run generate user and task overview reports
        generate_task_overview_report("tasks.txt")
        generate_user_overview_report("user.txt", "tasks.txt")
        print("\nYou have successfully generated user and task overview report!\n"
              "Go to user_overview and task_overview txt files to see.\nYou can also "
              "select \"ds\" on the menu to view the report under the stats.\n")

    # If user selects "s" for viewing stats
    elif menu_ == "ds":
        # First generate the reports in case the reports are not generated
        generate_task_overview_report("tasks.txt")
        generate_user_overview_report("user.txt", "tasks.txt")
        # Then run "get_stats" function
        get_stats("user_overview.txt", "task_overview.txt")

    # When users selects "e" display "Goodbye" message and exit loop
    elif menu_ == 'e':
        print('\nGoodbye!!!')
        exit()

    # If they enter the wrong selection display this
    # Expected selections (r, a, va, vm, s and e) for admin
    # and (a, va, vm and e) for other users
    else:
        print("\nYou have made a wrong choice, Please Try again\n")