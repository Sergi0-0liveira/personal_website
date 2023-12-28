import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(
        page_title="Services ",page_icon=":rocket:"
        )
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/75f245ec-0ded-4059-991f-1cfa81b84629/IyyjfwuXFo.json")

# Use local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Define the app title
st.title('Products and Services')

# Add some introductory text
st.header('HR Services')

st.markdown(""" 
        Welcome to the HR Magic Zone! 🌟 I am your go to person for everything HR . 
        Need help with talent hunting, people vibes, or office cheerleading? Say no more! 
        🚀 From fine-tuning hiring strategy to sprinkling HR fairy dust for better vibes, I got your back. 
        Let's turn your workplace into a buzzing hive of talent and smiles! 🌈✨
        """)
st.write("---")

st.header('HR Web App Development Services ')
st.markdown(""" 
        Focusing in Streamlit and Python I can help you turn your HR data into jaw-dropping, eye-popping web apps?
        🌐✨ Whether it's data visualizations, AI-powered apps, or sleek, user-friendly interfaces you're after, I got the answer for your questions. 
        Let's make your HR Process shine! 💃🚀✨
        """)

### contact form ###
st.write("---")
st.header("Get In Touch With Me!")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
<form action="https://formsubmit.co/sergio.miguel.oliveira.87@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
