import streamlit as st
from ui.shop import show_shop_page
from ui.cart import show_cart_page
from ui.wallet import show_wallet_page
from ui.account import show_account_page

def show_dashboard():
    user = st.session_state.user

    with st.sidebar:
        st.title(f"Welcome, {user['username']}!")

        st.markdown(f"""
        <div class="wallet-balance">
            <h3>💰 Wallet Balance</h3>
            <h2>₦{user['balance']:,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio("Navigation", ["🛒 Shop", "🛍️ Cart", "💳 Wallet", "👤 Account", "🚪 Logout"])

        if page == "🚪 Logout":
            st.session_state.user = None
            st.session_state.cart = {}
            st.session_state.page = 'login'
            st.rerun()

    if page == "🛒 Shop":
        show_shop_page()
    elif page == "🛍️ Cart":
        show_cart_page()
    elif page == "💳 Wallet":
        show_wallet_page()
    elif page == "👤 Account":
        show_account_page()
