import streamlit as st
import pandas as pd
import os

# Excel file name
FILE_NAME = "registration_data.xlsx"

# Function to load existing data or create a new one
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME, usecols=["Name", "Mobile Number", "Batch", "College", "Year"])
    else:
        return pd.DataFrame(columns=["Name", "Mobile Number", "Batch", "College", "Year"])

# Function to save data
def save_data(data):
    data.to_excel(FILE_NAME, index=False)

# Streamlit UI
st.title("TRUST Level Prize Money Registration Form")

name = st.text_input("Name")
mobile_number = st.text_input("Mobile Number")
batch = st.text_input("Batch")
college = st.text_input("College")
year = st.text_input("Year")

if st.button("Register"):
    if name and mobile_number and batch and college and year:
        if not mobile_number.isdigit() or len(mobile_number) < 10:
            st.error("Enter a valid mobile number (at least 10 digits).")
        else:
            df = load_data()

            # Check if the name already exists
            if not df[df["Name"].str.lower() == name.lower()].empty:
                st.error("This name is already registered!")
            else:
                new_entry = pd.DataFrame([[name, mobile_number, batch, college, year]], columns=df.columns)
                df = pd.concat([df, new_entry], ignore_index=True)
                save_data(df)
                st.success("Registration Successful!")
    else:
        st.warning("Please fill in all fields.")

# Show registered users
if st.checkbox("Show Registered Users"):
    df = load_data()
    st.dataframe(df)
