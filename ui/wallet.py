import streamlit as st
from models.user import User

def show_wallet_page():
    st.header("💳 Wallet Management")
    user = st.session_state.user

    st.markdown(f"""
    <div class="wallet-balance">
        <h3>Current Balance</h3>
        <h1>₦{user['balance']:,.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.subheader(" Add Funds to Your Wallet")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>💡 Quick Funding Options</h4>
            <p>Select an amount to instantly add funds to your wallet</p>
        </div>
        """, unsafe_allow_html=True)

        funding_options = {
            "₦10,000": 10000,
            "₦20,000": 20000,
            "₦50,000": 50000,
            "₦100,000": 100000
        }

        selected_amount = st.selectbox("💰 Choose amount:", list(funding_options.keys()))

        if st.button("💳 Fund Wallet", use_container_width=True):
            amount = funding_options[selected_amount]
            user['balance'] += amount
            User().update_user_balance(user)
            st.session_state.user = user
            st.success(f"✅ Funded with {selected_amount}!")
            st.balloons()
            st.rerun()

    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>💳 Payment Methods</h4>
            <p>• Bank Transfer ✅</p>
            <p>• Credit/Debit Card ✅</p>
            <p>• Mobile Money ✅</p>
            <p>• USSD Banking ✅</p>
        </div>
        """, unsafe_allow_html=True)
