import streamlit as st
import secrets
import string

def init_session_state():
    """Initializes default session variables"""
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'cart' not in st.session_state:
        st.session_state.cart = {}
    if 'page' not in st.session_state:
        st.session_state.page = 'login'

def generate_secure_password() -> str:
    """Generates a secure password"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(20))
