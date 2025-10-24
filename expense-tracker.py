import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Daily Expense Tracker", page_icon="💰", layout="centered")
st.title("💰 Daily Expense Tracker")

# CSV file to store expenses
DATA_FILE = "expenses.csv"

# Load existing expenses
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["name", "amount", "category"])

# Add new expense
with st.form("expense_form"):
    name = st.text_input("Expense Name")
    amount = st.number_input("Amount ($)", min_value=0.0, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    submitted = st.form_submit_button("Add Expense")
    if submitted and name and amount > 0:
        new_expense = {"name": name, "amount": amount, "category": category}
        df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("Expense added!")

# Display expenses
if not df.empty:
    st.subheader("Your Expenses")
    st.table(df)

    # Summary by category
    st.subheader("Summary by Category")
    category_summary = df.groupby("category")["amount"].sum().reset_index()
    st.bar_chart(category_summary.rename(columns={"amount": "Amount"}).set_index("category"))

    # Total
    st.write(f"**Total Spent:** ${df['amount'].sum():.2f}")
else:
    st.info("No expenses added yet. Use the form above to add your daily expenses.")
