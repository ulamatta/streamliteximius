import streamlit as st
from datetime import datetime

# Set the title
st.title("Aldecoa Coffee Internal Ordering System")

# Add a sidebar header
st.sidebar.header("Place Your Order")

# Input fields
name = st.sidebar.text_input("Name")
department = st.sidebar.text_input("Department")
coffee_type = st.sidebar.multiselect("Select Coffee Types", [
    "Aldecoa Whole Bean Mexico",
    "Aldecoa Whole Bean Colombia",
    "Aldecoa Whole Bean Brazil",
    "Aldecoa K-Cup Variety Pack, 80 Count",
    "Aldecoa K-Cup Intense, 80 Count",
    "Aldecoa Ethiopia Single-Origin K-Cup, 12 Count",
    "Ald. K-Cup Sumatra Lintong 12ct",
    "Ald. K-Cup Costa Rica Tarazu 12ct",
    "Ald. K-Cup Colombia Narino 12ct",
    "Aldecoa K-Cup Intense 12ct/10g",
    "Aldecoa K-Cup Colombia Decaf",
    "Aldecoa K-Cup Nina",
    "Aldecoa K-Cup Mexico",
    "Aldecoa Nespresso Capsules Variety Pack",
    "Ald Nespresso Cap Intense 10",
    "Ald Nespresso Cap Smooth 10",
    "Ald Nespresso Cap Dcf 10",
    "Ald Nespresso Cap Mexico 10",
    "Ald Nespresso Cap Colombian 10",
    "Ald Nespresso Cap Costa Rica 10",
    "Ald Nespresso Cap Brazil 10",
    "2 LB Ald Colombia Whole Bean",
    "2 LB Ald Costa Rica Whole Bean",
    "2 LB Ald Sumatra WB",
    "2 LB Ald Ethiopia WB",
    "2 LB Ald Nina Whole Bean",
    "2 LB Ald Mexico Whole Bean",
    "2 LB Ald Brasil Whole Bean",
    "Cappio Cold Brew Concentrate Coffee",
    "Cappio Cold Brew Filter Pack"
])

pickup_date = st.sidebar.date_input("Pickup Date", datetime.now())
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Button to submit the order
if st.sidebar.button("Submit Order"):
    st.write(f"Order received on {current_datetime}!")
    st.write(f"Name: {name}")
    st.write(f"Department: {department}")
    st.write(f"Coffee Types: {', '.join(coffee_type)}")
    st.write(f"Pickup Date: {pickup_date}")

    # Here you would add code to log the order to a database or send it somewhere
