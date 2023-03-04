import datetime
import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='arlind1234!',
         host='127.0.0.1',
         )

cursor=conn.cursor()
#cursor.execute('create database taxi')
cursor.execute('use taxi')
#cursor.execute('CREATE TABLE cars (id INT PRIMARY KEY AUTO_INCREMENT,model VARCHAR(255),year INT,registration_plate VARCHAR(20))')
#cursor.execute('CREATE TABLE drivers (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255),surname VARCHAR(255),datelindja DATE,car_id INT,FOREIGN KEY (car_id) REFERENCES cars(id))')

def insert_data_cars(model,year ,registration_plate):
    query = f"INSERT INTO cars (model, year,registration_plate) VALUES ('{model}', {year},'{registration_plate}')"
    cursor.execute(query)
    conn.commit()
    st.success("Data inserted successfully")

def insert_driver(name, surname, birthdate, car_id):
    query = "INSERT INTO drivers (name, surname, datelindja, car_id) VALUES (%s, %s, %s, %s)"
    values = (name, surname, birthdate, car_id)
    cursor.execute(query, values)
    conn.commit()
    st.success("Data inserted successfully")

def delete_data(id):
    query = "DELETE FROM drivers WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    st.success("Data deleted successfully")


def update_car(id,model, year,registration_plate):

    query = f"UPDATE cars SET model = '{model}', year = {year}, registration_plate = '{registration_plate}' WHERE id = {id}"
    cursor.execute(query)
    conn.commit()
    st.success("Data updated successfully")

def read_driver():
    cursor.execute("SELECT * FROM drivers")
    result = cursor.fetchall()
    return result

def read_car():
    cursor.execute("SELECT * FROM cars")
    result = cursor.fetchall()
    return result


def home():
    st.title("taxi app ")
    menu = ["read car",'read driver', "Insert Data car",'insert data driver' ,"Update Data", "Delete Data"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "read car":
        st.subheader("all Data for cars")
        data = read_car()
        st.table(data)
    elif choice == "read driver":
        st.subheader("all Data for driver")
        data = read_driver()
        st.table(data)

    elif choice == "Insert Data car":
        st.subheader("Insert Data car")
        year=st.number_input("enter year")
        registrationplate = st.number_input("registration plate")
        model = ['bmw','audi']
        model = st.selectbox('Select location:', model)
        if st.button("Insert"):
            insert_data_cars(model,year,registrationplate)

    elif choice == "insert data driver":
        st.subheader("insert data driver")
        name=st.text_input("enter name")
        surname=st.text_input("enter surnname")
        birthdate=st.date_input("enter date")
        car_id=st.number_input("enter id")
        if st.button('insert'):
            insert_driver(name,surname,birthdate,car_id)
    elif choice == "Update Data":

        st.subheader("Update Data")
        id = st.number_input("Enter id")
        year=st.number_input('enter year')
        registrationplate=st.text_input('registration pplate')
        model = ['bmw', 'audi']
        model = st.selectbox('Select model:', model)
        if st.button("Update"):
            update_car(id,model,year,registrationplate)

    elif choice == "Delete Data":
        st.subheader("Delete Data")
        id = st.number_input("Enter id")
        if st.button("Delete"):
            delete_data(id)


home()
conn.commit()