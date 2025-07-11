import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        .stSidebar {
            background-color: #2a2a2a !important;
            color: #ffffff !important;
        }

        .stSelectbox > div > div > select,
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            background-color: #3a3a3a !important;
            color: #ffffff !important;
            border: 1px solid #888 !important;
        }

        .stButton > button {
            background-color: #2196f3 !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
        }

        .stButton > button:hover {
            background-color: #1976d2 !important;
        }

        .stRadio > div {
            color: #ffffff !important;
        }

        .wallet-balance {
            background-color: #444 !important;
            border: 2px solid #fff;
            color: #ffffff !important;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .product-card, .cart-item {
            background-color: #3a3a3a !important;
            color: #ffffff !important;
            border: 1px solid #777;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
        }

        .product-price {
            color: #03a9f4 !important;
            font-size: 1.3em !important;
            font-weight: bold;
        }

        .info-box, .success-box, .error-box {
            background-color: #2f2f2f;
            border-left: 5px solid #03a9f4;
            padding: 15px;
            border-radius: 8px;
            color: #ffffff !important;
        }
    </style>
    """, unsafe_allow_html=True)
