import streamlit as sl

##App Name
sl.title('Fitness Imbalance Tracker') 

#Welcome options
menu = ['Login', 'Register']
choice = sl.sidebar.selectbox('Menu', menu)

##Login Option
if choice == 'Login':
    sl.subheader = ('Login')

    ##Input Username and Password
    username = sl.text_input("Username")
    password = sl.text_input("Password", type = "password")

    if sl.button('Login'):
        #Example Check
        if username == 'sruthi' and password == 'password123':
            sl.success(f"Welcome, {username}!")
        else:
            sl.error("Invalid Login. Please check username and/or password.")

##Register Option
if choice == "Register":
    sl.subheader = ('Register')

    ##Select Username and Password
    new_username = sl.text_input("Username")
    new_password = sl.text_input("Password", type = "password")
    confirm_password = sl.text_input("Confirm Password", type = "password")

    if sl.button("Register"):
        if new_password != confirm_password:
            sl.error("Passwords do not match.")
        elif new_username == "":
            sl.error("Please choose a username.")
        else:
            sl.success("Thank you for creating an account!")
            sl.info("Proceed to the Login Page to sign in.")



    