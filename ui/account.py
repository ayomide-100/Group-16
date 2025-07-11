import streamlit as st
from models.user import User

def show_account_page():
    st.header("👤 Account Management")
    user = st.session_state.user
    tab1, tab2 = st.tabs(["Account Info", "Settings"])

    with tab1:
        st.subheader("Account Information")
        with st.expander("View Account Details", expanded=False):
            password_verify = st.text_input("Enter password to view details:", type="password")
            if st.button("Verify"):
                if password_verify == user['password']:
                    st.success("Verified!")
                    st.info(f"**Username:** {user['username']}")
                    st.info(f"**Email:** {user['email']}")
                    st.info(f"**Balance:** ₦{user['balance']:,.2f}")
                else:
                    st.error("Incorrect password.")

    with tab2:
        st.subheader("Account Settings")
        user_manager = User()

        with st.expander("Change Username"):
            new_username = st.text_input("New Username")
            confirm = st.text_input("Confirm Password", type="password", key="username_pwd")
            if st.button("Update Username"):
                if confirm == user['password'] and new_username:
                    user_manager.update_user_info(user['username'], new_username=new_username)
                    user['username'] = new_username
                    st.session_state.user = user
                    st.success("Username updated.")

        with st.expander("Change Email"):
            new_email = st.text_input("New Email")
            confirm = st.text_input("Confirm Password", type="password", key="email_pwd")
            if st.button("Update Email"):
                if confirm == user['password'] and new_email:
                    user_manager.update_user_info(user['username'], new_email=new_email)
                    user['email'] = new_email
                    st.session_state.user = user
                    st.success("Email updated.")

        with st.expander("Change Password"):
            old = st.text_input("Current Password", type="password")
            new = st.text_input("New Password", type="password")
            if st.button("Update Password"):
                if old == user['password']:
                    if user_manager.is_valid_password(new):
                        user_manager.update_user_info(user['username'], new_password=new)
                        user['password'] = new
                        st.session_state.user = user
                        st.success("Password updated.")
                    else:
                        st.error("Password must be 16+ chars with uppercase, lowercase, digit, symbol.")
                else:
                    st.error("Incorrect password.")

        with st.expander("Reset Balance"):
            st.warning("Resetting will zero your balance.")
            confirm = st.text_input("Confirm Password", type="password", key="reset_pwd")
            if st.button("Reset Balance"):
                if confirm == user['password']:
                    user['balance'] = 0.0
                    user_manager.update_user_balance(user)
                    st.session_state.user = user
                    st.success("Balance reset.")
                else:
                    st.error("Invalid password.")
