import streamlit as st
from datetime import datetime
import pandas as pd

# Initialize session state to store orders
if 'orders' not in st.session_state:
    st.session_state.orders = []

def home():
    st.title("Aldecoa Coffee Internal Ordering System")
    st.write("Welcome to the Aldecoa Coffee ordering system. Please use the sidebar to navigate.")

def place_order():
    st.sidebar.header("Place Your Order")

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
    confirmation_code = f"CONF-{len(st.session_state.orders) + 1:03d}"

    if st.sidebar.button("Submit Order"):
        order = {
            "Name": name,
            "Department": department,
            "Coffee Types": ', '.join(coffee_type),
            "Pickup Date": pickup_date,
            "Order Time": current_datetime,
            "Confirmation Code": confirmation_code,
            "Picked Up": False
        }
        st.session_state.orders.append(order)
        st.success(f"Order received! Confirmation code: {confirmation_code}")

def view_orders():
    st.title("View Orders")
    if st.session_state.orders:
        df = pd.DataFrame(st.session_state.orders)
        st.dataframe(df)
    else:
        st.write("No orders placed yet.")

def picked_up_orders():
    st.title("Picked Up Orders")
    if st.session_state.orders:
        df = pd.DataFrame([order for order in st.session_state.orders if order["Picked Up"]])
        st.dataframe(df)
    else:
        st.write("No orders picked up yet.")

def track_order():
    st.title("Track Order")
    confirmation_code = st.text_input("Enter Confirmation Code")
    if st.button("Track Order"):
        for order in st.session_state.orders:
            if order["Confirmation Code"] == confirmation_code:
                st.write(f"Order found: {order}")
                return
        st.error("Order not found!")

def mark_picked_up():
    st.title("Mark Order as Picked Up")
    confirmation_code = st.text_input("Enter Confirmation Code to Mark as Picked Up")
    if st.button("Mark as Picked Up"):
        for order in st.session_state.orders:
            if order["Confirmation Code"] == confirmation_code:
                order["Picked Up"] = True
                st.success(f"Order {confirmation_code} marked as picked up!")
                return
        st.error("Order not found!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page:", ["Home", "Place Order", "View Orders", "Picked Up Orders", "Track Order", "Mark as Picked Up"])

    if page == "Home":
        home()
    elif page == "Place Order":
        place_order()
    elif page == "View Orders":
        view_orders()
    elif page == "Picked Up Orders":
        picked_up_orders()
    elif page == "Track Order":
        track_order()
    elif page == "Mark as Picked Up":
        mark_picked_up()

if __name__ == "__main__":
    main()
