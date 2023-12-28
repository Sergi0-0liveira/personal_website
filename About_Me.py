import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(
        page_title="Sérgio Oliveira",page_icon=":tada:"
        )
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/75f245ec-0ded-4059-991f-1cfa81b84629/IyyjfwuXFo.json")
#img_contact_form = Image.open("images/yt_contact_form.png")
#img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Define the app title
st.title('Welcome to my professional page')

# Add some introductory text
st.subheader('Hi :wave: and Welcome to my page!')

st.markdown("""  
        I'm Sérgio! 
        I've been navigating the HR world while geeking out over all things Technology and AI. 
        I love leaving a positive mark on people wherever I go—it's my thing!
        """)

st.markdown(""" 
        My journey's been a mash-up of meeting incredible folks and soaking up their wisdom. That's how I keep growing and evolving. 
        I get a real kick out of diving into new stuff—I'm all about exploring and teaching myself the ins and outs of things.
        """)
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(""" 
        I'm passionate about pioneering the fusion of AI and HR and in understanding how AI can revolutionize the HR landscape. 
        I thrive in exploring how to streamline processes, elevate talent management, and create a more people-oriented workplace. 
         """)
        st.markdown("""
        I am thrilled to carve a path where AI augments human expertise in HR.
        """)

    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")

st.write("---")
st.markdown(""" 
                Do you need help? Maybe building a web app link this? 
                I'm always up for a challenge! Whether it's tech or HR related, 
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
