import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
        page_title="Portfolio",page_icon=":tada:"
        )
#call the lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/b23c7375-536a-4f39-a60d-6f4dec2a27cf/ycaFW9Asyu.json")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

cv_path = "pages/cv.pdf"

def download_cv():
    with open(cv_path, "rb") as file:
        file_content = file.read()
        st.download_button("Download CV", file_content, file_name='cv.pdf')
 
def open_linkedin():
    webbrowser.open(git_linkedin)
st.markdown("<h2 color: white;'>Working on this...</h2>", unsafe_allow_html=True)

st_lottie(lottie_coding, height=400, key="coding")

st.markdown("<h3> In the meantime visit my: </h3>", unsafe_allow_html=True)


with st.container():
    left_column, center_column = st.columns(2)
    with left_column:
        st.markdown(":point_right:[GitHub Page...](https://github.com/Sergi0-0liveira)")

    with center_column:
        st.markdown(":point_right: [LinkedIn Page...](https://www.linkedin.com/in/sergio-oliveira-headofpeople/)")


### contact form ###
st.write("---")
st.markdown("<h3 style='text-align: center; color: white;'> Get In Touch With Me! </h1>", unsafe_allow_html=True)


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
