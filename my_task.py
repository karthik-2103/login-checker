import streamlit as st
import pandas as pd
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="karthik",database="py")
res = con.cursor()

rad = st.sidebar.radio("Navigator", ["Register", "Login", "User Detials"])

if rad == "Register":
    st.title("Register")
    
    first, last = st.columns(2)
    first_name = first.text_input("First Name")
    last_name = last.text_input("Last Name")
    
    mail, no = st.columns([3, 1])
    email_id = mail.text_input("Mail Id")
    phone_num = no.text_input("Mobile Number")
    
    us, pw, pw1 = st.columns(3)
    user_name = us.text_input("User Id")
    user_password = pw.text_input("Password", type="password")
    user_password_reenter = pw1.text_input("Reenter the Password", type="password")
    
    check = st.checkbox("I agree")
    button = st.button("Submit")


    if button:
        if user_password == user_password_reenter:
            qry = "INSERT INTO task (first_name, last_name, email_id, phone_num, user_name, user_password) VALUES (%s, %s, %s, %s, %s, %s)"
            user = (first_name, last_name, email_id, phone_num, user_name, user_password)
            res.execute(qry, user)
            con.commit()
                
            st.success("Register successful!")
            st.balloons()
        else:
            st.error("Passwords do not match")

if rad == "Login":
        st.title("Login Page")
        user_name = st.text_input("User Id")
        users_lists = []
        qry = "select user_name from task"
        res.execute(qry)
        data = res.fetchall()
        for i in data:
            users_lists.append(i[0])
        if user_name in users_lists:
            user_password = st.text_input("Password", type="password")
            qry1 = "select user_password from task where user_name = %s"
            value = (user_name,)
            res.execute(qry1,value)
            data = res.fetchall()
            password_ch = data[0][0]
            if user_password == password_ch:
                st.success("login successfully")
                st.balloons()
            else:
                st.error("Invalid password")
        else:
            st.error("Invalid username")

if rad == "User Detials":
    st.title("User Details")
    user_name = st.text_input("Enter your user name")
    user_lt = []
    qry = "select user_name from task"
    res.execute(qry)
    data = res.fetchall()
    for i in data:
        user_lt.append(i[0])
    if user_name in user_lt:
        st.success("User details found")
        st.success("Go to login page to access")
        st.balloons()
    else:
        st.error("User details not found ")
        st.error("Go to Register page and Register your details")
