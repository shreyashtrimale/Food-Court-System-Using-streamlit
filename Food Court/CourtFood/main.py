import streamlit as st
import time
import random
import qrcode
import io
import requests


st.set_page_config(page_title="Food Court App", page_icon="🍽️")

st.title("WELCOME TO FOOD COURT")  
st.header("Order Your Favourite Food Here")

st.write('Please select your food items')

# -------- MENU SELECTION --------
menu = st.selectbox(
    "What You Like To Taste",
    ['Indian','Chinese','Italian','Beverages','Desserts & Sweets']
)

selected_item = None

if menu == 'Indian':
    indian = st.selectbox(
        "Select Your Favourite Indian Dish",
        ['Biryani','Paneer Butter Masala','Dal Makhani','Chole Bhature','Butter Naan']
    )
    selected_item = indian

elif menu == 'Chinese':
    chinese = st.selectbox(
        "Select Your Favourite Chinese Dish",
        ['Noodles','Fried Rice','Manchurian','Spring Rolls','Dumplings']
    )
    selected_item = chinese

elif menu == 'Italian':
    italian = st.selectbox(
        "Select Your Favourite Italian Dish",
        ['Pizza','Pasta','Lasagna','Risotto','Tiramisu']
    )
    selected_item = italian

elif menu == 'Beverages':
    beverages = st.selectbox(
        "Select Your Favourite Beverage",
        ['Coffee','Tea','Lemonade','Smoothie','Soda']
    )
    selected_item = beverages

elif menu == 'Desserts & Sweets':
    desserts = st.selectbox(
        "Select Your Favourite Dessert",
        ['Ice Cream','Brownie','Cheesecake','Cupcake','Pudding']
    )
    selected_item = desserts

# Quantity
quantity = st.number_input("Enter Quantity", min_value=1, max_value=10, step=1)

# -------- CART --------
if "cart" not in st.session_state:
    st.session_state.cart = []

if st.button("Add To Cart"):
    if selected_item:
        st.session_state.cart.append({"item": selected_item, "qty": quantity})
        st.success(f"✅ {selected_item} (x{quantity}) has been added to cart!")

# -------- ORDER PLACEMENT --------
if st.button("Place Order"):
    with st.spinner("Cooking your food... 🍲"):
        time.sleep(3)
    st.success("Order Ready!")

# -------- ORDER SUMMARY --------
st.subheader("🧾 Order Summary")
if st.session_state.cart:
    total_amount = len(st.session_state.cart) * 199  # demo pricing
    order = {
        "id": f"ORDER-{random.randint(1000,9999)}",
        "amount": total_amount,
        "currency": "INR",
        "items": [f"{c['item']} (x{c['qty']})" for c in st.session_state.cart]
    }

    st.write(f"Order ID: {order['id']}")
    st.write(f"Amount: ₹{order['amount']}")
    st.write("Items:")
    for it in order["items"]:
        st.write("-", it)

    # -------- PAYMENT OPTIONS --------
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Pay with GPay"):
            with st.spinner("Starting Google Pay..."):
                time.sleep(2)
            st.success("✅ Google Pay: Payment successful!")

    with col2:
        if st.button("Pay with PhonePe"):
            with st.spinner("Redirecting to PhonePe checkout..."):
                time.sleep(2)
            st.success("✅ PhonePe: Payment successful (simulated)")

    with col3:
        if st.button("Pay with Razorpay"):
            with st.spinner("Opening Razorpay checkout..."):
                time.sleep(2)
            st.success("✅ Razorpay: Payment successful (simulated)")

    col4, col5 = st.columns(2)
    with col4:
        if st.button("Pay with Stripe"):
            with st.spinner("Creating Stripe Checkout session..."):
                time.sleep(2)
            st.success("✅ Stripe: Payment successful (simulated)")

    with col5:
        if st.button("Pay with Paytm"):
            with st.spinner("Initializing Paytm..."):
                time.sleep(2)
            st.success("✅ Paytm: Payment successful (simulated)")

    st.markdown("---")
    if st.checkbox("Show debug info (simulation)"):
        st.json(order)

else:
    st.info("🛒 Your cart is empty. Please add items to see order summary.")





        