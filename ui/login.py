import streamlit as st
from models.user import User
from utils.helpers import generate_secure_password

def show_login_page():
    st.title("🛍️ E-Commerce App")
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

    with tab1:
        st.header("Welcome Back!")

        with st.form("login_form"):
            st.markdown("### Enter Your Credentials")
            username_email = st.text_input("Username or Email", max_chars=50)
            password = st.text_input("Password", type="password", max_chars=50)
            login_button = st.form_submit_button("Sign In", use_container_width=True)

            if login_button:
                if username_email and password:
                    user_manager = User()
                    user = user_manager.authenticate(username_email, password)
                    if user:
                        st.session_state.user = user
                        st.session_state.page = 'dashboard'
                        st.success("✅ Login successful! Welcome back!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials. Please try again.")
                else:
                    st.error("⚠️ Please fill in all fields.")

    with tab2:
        st.header("Create New Account")

        with st.form("signup_form"):
            st.markdown("### Create Your Account")
            new_username = st.text_input(" Username", max_chars=30)
            new_email = st.text_input(" Email Address", max_chars=50)

            password_option = st.radio(" Password Setup", ["Enter manually", "Generate secure password"])

            if password_option == "Enter manually":
                new_password = st.text_input(" Password", type="password", max_chars=50)
                st.caption(" Password must be 16+ characters with uppercase, lowercase, number, and symbol")
            else:
                if st.button(" Generate Secure Password"):
                    st.session_state.generated_password = generate_secure_password()

                if 'generated_password' in st.session_state:
                    st.markdown("** Your Generated Password:**")
                    st.code(st.session_state.generated_password)
                    st.caption(" Please save this password securely!")
                    new_password = st.session_state.generated_password
                else:
                    new_password = ""

            signup_button = st.form_submit_button(" Create Account", use_container_width=True)

            if signup_button:
                if new_username and new_email and new_password:
                    user_manager = User()
                    if user_manager.is_existing_user(new_username, new_email):
                        st.error("❌ Username or email already exists.")
                    elif not user_manager.is_valid_password(new_password):
                        st.error("❌ Password does not meet security requirements.")
                    else:
                        if user_manager.create_account(new_username, new_email, new_password):
                            st.success(" Account created! Please sign in.")
                            st.balloons()
                        else:
                            st.error("❌ Failed to create account.")
                else:
                    st.error("⚠️ Please fill in all required fields.")
