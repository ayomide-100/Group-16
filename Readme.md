# 🛍️ E-Commerce Web App

A **modular Python + Streamlit** application simulating an e-commerce platform with:

- Secure user authentication  
- Product browsing & cart system  
- Wallet funding  
- Account management

Designed with a **dark-themed UI**, optimized for **clarity, reusability, and scalability**.

##  Features

###  User Authentication
- Sign up & log in securely  
- Strong password validation (16+ chars with mixed character types)  
- Optional secure password generation

###  Shopping Dashboard
- Search & browse inventory  
- Add products to cart  
- View & manage cart items  
- Checkout with balance verification

###  Wallet Management
- Quick-select funding options  
- Persistent balance stored in file

###  Account Settings
- Change username, email, or password  
- Reset wallet balance

###  Custom Streamlit UI
- Dark theme styling with CSS  
- Sidebar and dropdowns styled for contrast & accessibility

---

##  Project Structure
ecomm/
├── main.py               # App entry point
├── models/               # Core backend logic
│   ├── file_manager.py
│   ├── user.py
│   └── inventory.py
├── ui/                   # UI components
│   ├── css.py
│   ├── login.py
│   ├── dashboard.py
│   ├── shop.py
│   ├── cart.py
│   ├── wallet.py
│   └── account.py
├── utils/
│   └── helpers.py        # Session state & utilities
└── data/
    


## Contributors
Ayomide Adegoke – [aadegoke100@gmail.com](mailto:aadegoke100@gmail.com)
Lauretta Omekam - 
Abdullahi Fahad Tukura - [abdullahifahad223@gmail.com](mailto:abdullahifahad223@gmail.com)


Contributions welcome! Feel free to fork, improve, and submit pull requests.


