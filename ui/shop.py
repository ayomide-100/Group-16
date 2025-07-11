import streamlit as st
from models.inventory import Inventory

def show_shop_page():
    st.header("🛒 Shop Products")
    inventory_manager = Inventory()
    inventory = inventory_manager.load_inventory()

    st.subheader("🔍 Search Products")
    search_query = st.text_input("Enter product name or brand:", placeholder="e.g., iPhone, Samsung")

    if st.button("Search Products", use_container_width=True):
        st.session_state.search_performed = True

    if search_query:
        filtered_items = inventory_manager.search_inventory(search_query, inventory)
    else:
        filtered_items = list(inventory.keys())

    if not filtered_items:
        st.info("No products found matching your search.")
        return

    st.subheader(f" Available Products ({len(filtered_items)} items)")

    for i, item in enumerate(filtered_items):
        st.markdown(f"""
        <div class="product-card">
            <h4>🛍️ {item}</h4>
            <p class="product-price">₦{inventory[item]:,}</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])
        with col1:
            quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1, key=f"qty_{i}")
        with col2:
            if st.button(f"🛒 Add to Cart", key=f"add_{i}", use_container_width=True):
                if item in st.session_state.cart:
                    st.session_state.cart[item] += quantity
                else:
                    st.session_state.cart[item] = quantity
                st.success(f"✅ Added {quantity} x {item} to cart!")
                st.rerun()
        st.divider()
