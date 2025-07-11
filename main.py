from models.file_manager import FileManager
from utils.helpers import init_session_state
from ui.css import inject_custom_css
from ui.login import show_login_page
from ui.dashboard import show_dashboard
import streamlit as st

def main():
    FileManager().initialise_storage()
    init_session_state()
    inject_custom_css()
    
    if st.session_state.user is None:
        show_login_page()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()
