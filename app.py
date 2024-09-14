import streamlit as st

# Set page config for dark theme
st.set_page_config(page_title="Spotify-like Interface", layout="wide", page_icon="🎵")

# Custom CSS for styling
st.markdown("""
<style>
    body {
        color: #1DB954;
        background-color: #000000;  # Changed to black
    }
    .stButton>button {
        color: #000000;  # Changed to black for contrast
        background-color: #1DB954;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1ED760;
    }
    .login-btn {
        position: fixed;
        top: 20px;
        right: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Login button
st.markdown('<div class="login-btn">', unsafe_allow_html=True)
st.button("Login")
st.markdown('</div>', unsafe_allow_html=True)

# Main content
st.title("Spotify-like Interface")

# Four buttons
col1, col2 = st.columns(2)

with col1:
    st.button("Button 1")
    st.button("Button 2")

with col2:
    st.button("Button 3")
    st.button("Button 4")