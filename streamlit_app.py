import streamlit as st

# Function to read the CSS file and inject it into the Streamlit app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Function to read the JavaScript file and inject it into the Streamlit app
def local_js(file_name):
    with open(file_name) as f:
        st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)

# Apply the local CSS and JavaScript files
local_css("style.css")
local_js("script.js")

# Injecting custom HTML for the header and footer
st.markdown(
    """
    <header>
        <h3>My Streamlit App Header</h3>
    </header>
    """,
    unsafe_allow_html=True
)

# Streamlit app content
st.write('This is the main content of the app.')

# Login
with st.form("Log"):
    st.write("Login")
    username = st.text_input("Username: ", placeholder="Enter your Username")
    password = st.text_input("Password: ", placeholder="Enter your Password",type="password")
    rm = st.checkbox("Remember me")
    login = st.form_submit_button("Submit")

pages = [st.Page("home.py", title="Home Page"), st.Page("about_us.py", title="About")]
navigate = st.navigation(pages=pages, position="sidebar")


# Injecting custom HTML for the footer
st.markdown(
    """
    <footer>
        <p>My Streamlit App Footer &copy; 2024</p>
    </footer>
    """,
    unsafe_allow_html=True
)
