  import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Sell Crop Residue",
    page_icon="🌾",
    layout="centered"
)

# ------------------ TITLE ------------------
st.title("🌾 Sell Crop Residue")
st.write("Add your crop residue items for sale and earn profit instead of burning.")

# ------------------ SESSION STATE ------------------
if "items" not in st.session_state:
    st.session_state["items"] = []

# ------------------ ADD ITEM FORM ------------------
st.header("Add Item for Sale")

name = st.text_input("Item Name", placeholder="e.g. Rice Straw Bales")
crop = st.selectbox(
    "Crop Type",
    ["Rice", "Wheat", "Sugarcane", "Maize", "Cotton", "Other"]
)
quantity = st.number_input(
    "Quantity (tonnes)",
    min_value=0.1,
    value=1.0,
    step=0.5
)
price = st.number_input(
    "Price per tonne (₹)",
    min_value=100,
    value=2500,
    step=100
)
location = st.text_input("Location", placeholder="e.g. Karnal, Haryana")

if st.button("Add Item"):
    if name and location:
        st.session_state["items"].append({
            "name": name,
            "crop": crop,
            "qty": quantity,
            "price": price,
            "location": location
        })
        st.success(f"Added: {name} — {quantity} tonnes at ₹{price}/tonne")
    else:
        st.error("Please fill in item name and location.")

st.divider()

# ------------------ LISTED ITEMS ------------------
st.header(f"Listed Items ({len(st.session_state['items'])})")

if not st.session_state["items"]:
    st.info("No items yet. Add one above.")
else:
    for i, item in enumerate(st.session_state["items"]):
        total = item["qty"] * item["price"]

        st.subheader(item["name"])
        st.write(
            f"Crop: {item['crop']} | "
            f"Qty: {item['qty']} tonnes | "
            f"Price: ₹{item['price']:,}/tonne"
        )
        st.write(
            f"Total Value: **₹{total:,.0f}** | "
            f"Location: {item['location']}"
        )

        if st.button("Remove", key=f"rm_{i}"):
            st.session_state["items"].pop(i)
            st.rerun()

        st.divider()

# ------------------ PROFIT CALCULATOR ------------------
st.header("Profit Calculator")

calc_qty = st.number_input(
    "Quantity (tonnes)",
    min_value=0.1,
    value=5.0,
    step=0.5,
    key="cq"
)
calc_price = st.number_input(
    "Selling Price (₹/tonne)",
    min_value=100,
    value=2800,
    step=100,
    key="cp"
)
calc_cost = st.number_input(
    "Processing Cost (₹/tonne)",
    min_value=0,
    value=800,
    step=100,
    key="cc"
)

if st.button("Calculate"):
    revenue = calc_qty * calc_price
    cost = calc_qty * calc_cost
    profit = revenue - cost

    st.write(f"Revenue: ₹{revenue:,.0f}")
    st.write(f"Cost: ₹{cost:,.0f}")
    st.write(f"**Profit: ₹{profit:,.0f}**")

st.divider()
st.caption("© AGRI-Intellect")
