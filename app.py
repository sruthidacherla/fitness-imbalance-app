import streamlit as sl
from modules.login import register_users, check_user
from modules.assessment import run_assessment
from modules.exercises import run_shoulder, run_arms, run_back, run_chest, run_hips
from modules.home import home

if "login_success" not in sl.session_state:
    sl.session_state.login_success = False

#Menu Sidebar
menu = ['Home', 'Login', 'Register', 'Assessment', 'Shoulder', 'Arms', 'Back', 'Chest', 'Hips', 'Legs']
choice = sl.sidebar.selectbox('Menu', menu)

#Home Option
if choice == 'Home':
    home()

#Login Option
if choice == 'Login':
    ##App Name
    sl.title('Muscle Imbalance Tracker')   

    sl.subheader = ('Login')

    #Input Username and Password
    username = sl.text_input("Username")
    password = sl.text_input("Password", type = "password")

    if sl.button('Login'):
        #Example Check
        if check_user(username, password):
            sl.success(f"Welcome, {username}!")
            sl.session_state.login_success = True
        else:
            sl.error("Invalid Login. Please check username and/or password.")

#Register Option
elif choice == "Register":
    ##App Name
    sl.title('Muscle Imbalance Tracker') 

    sl.subheader = ('Register')

    #Select Username and Password
    new_username = sl.text_input("Username")
    new_password = sl.text_input("Password", type = "password")
    confirm_password = sl.text_input("Confirm Password", type = "password")

    if sl.button("Register"):
        if new_password != confirm_password:
            sl.error("Passwords do not match.")
        elif new_username == "":
            sl.error("Please choose a username.")
        else:
            if register_users(new_username, new_password):
                sl.success("Thank you for creating an account!")
                sl.info("Proceed to the Login Page to sign in.")
                sl.session_state.login_success = True
            else:
                sl.error("Username is taken.")

#Assessment Option
elif choice == 'Assessment': 
    run_assessment(choice)

##Exercises

#Shoulder 
elif choice == 'Shoulder':
    run_shoulder()

#Arm
elif choice == 'Arms':
    run_arms()

#Back
elif choice == 'Back':
    run_back()

#Chest
elif choice == 'Chest':
    run_chest()

#Hips
elif choice == 'Hips':
    run_hips()

#Legs
elif choice == 'Legs':
    run_legs()

