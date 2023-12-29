import requests
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser

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
            
#function to open gitpage
git_page_url = "https://github.com/Sergi0-0liveira"

button_clicked = st.button("Visit GitHub Page")

if button_clicked:
    st.markdown(f'<a href="{git_page_url}" target="_blank"> <input type="button" value="GitHub Page"> </a>', unsafe_allow_html=True)

#function to open gitpage
git_linkedin = "https://www.linkedin.com/in/sergio-oliveira-headofpeople/"

def open_linkedin():
    webbrowser.open(git_linkedin)
st.markdown("<h2 color: white;'>Working on this...</h2>", unsafe_allow_html=True)

st_lottie(lottie_coding, height=400, key="coding")

st.markdown("<h3> In the meantime visit my: </h3>", unsafe_allow_html=True)


with st.container():

    left_column, center_column, right_column = st.columns(3)
    with left_column:
        st.button(" GitHub Page  "):
            
    with center_column:
        if st.button(" LinkedIn Page "):
            open_linkedin()

    with right_column:
        download_cv()


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
