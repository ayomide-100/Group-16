import streamlit as st
from models.inventory import Inventory
from models.user import User

def show_cart_page():
    if st.session_state.get("payment_success"):
        st.success("✅ Payment successful! Thank you for shopping with us!")
        st.balloons()
        del st.session_state["payment_success"]

    st.header("🛍️ Your Shopping Cart")

    if not st.session_state.cart:
        st.markdown("""
        <div class="info-box">
            <h3>🛒 Your cart is empty</h3>
            <p>Start shopping to add items to your cart!</p>
        </div>
        """, unsafe_allow_html=True)
        return

    inventory_manager = Inventory()
    inventory = inventory_manager.load_inventory()
    st.subheader("📋 Items in Your Cart")
    total = 0

    for i, (item, quantity) in enumerate(st.session_state.cart.items()):
        if item in inventory:
            price = inventory[item]
            subtotal = price * quantity
            total += subtotal

            st.markdown(f"""
            <div class="cart-item">
                <h4>🛍️ {item}</h4>
                <p><strong>Quantity:</strong> {quantity}</p>
                <p><strong>Price:</strong> ₦{price:,} each</p>
                <p><strong>Subtotal:</strong> ₦{subtotal:,}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([2, 1, 1])
            with col2:
                if st.button(f"➖ Remove 1", key=f"remove_{i}"):
                    if st.session_state.cart[item] > 1:
                        st.session_state.cart[item] -= 1
                    else:
                        del st.session_state.cart[item]
                    st.rerun()
            with col3:
                if st.button(f"🗑️ Remove All", key=f"remove_all_{i}"):
                    del st.session_state.cart[item]
                    st.rerun()

    st.divider()
    st.markdown(f"""
    <div class="info-box">
        <h3>💰 Cart Summary</h3>
        <h2>Total Amount: ₦{total:,}</h2>
        <p>Current Balance: ₦{st.session_state.user['balance']:,}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader(" Cart Actions")
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("🧹 Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.success("Cart cleared!")
            st.rerun()

    with col2:
        if st.button(" Continue Shopping", use_container_width=True):
            st.info("Use the sidebar to return to Shop")

    with col3:
        if st.button(" Checkout", use_container_width=True, type="primary"):
            user = st.session_state.user
            if user['balance'] >= total:
                user['balance'] -= total
                User().update_user_balance(user)
                st.session_state.user = user
                st.session_state.cart = {}
                st.session_state.payment_success = True  
                st.rerun()
            else:
                st.error("❌ Insufficient balance. Please fund your wallet first.")
