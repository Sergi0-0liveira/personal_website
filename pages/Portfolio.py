import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit import button, markdown
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
 
def open_linkedin():
    webbrowser.open(git_linkedin)
st.markdown("<h2 color: white;'>Working on this...</h2>", unsafe_allow_html=True)

st_lottie(lottie_coding, height=400, key="coding")

st.markdown("<h3> In the meantime visit my: </h3>", unsafe_allow_html=True)


with st.container():

    left_column, center_column, right_column = st.columns(3)
    with left_column:

        # Get your GitHub repository URL from Streamlit Share Cloud
        repo_url = "https://github.com/Sergi0-0liveira"

        # Create a button to open your GitHub page
        btn_open_github = button('Open GitHub Page')
        
        # When the button is clicked, open the GitHub page in a new browser tab
        @st.experimental_button_callback
        def open_github_page():
            import webbrowser
            webbrowser.open_new_tab(repo_url)

# Display the button in your app
st.markdown(f"**Open GitHub Page:**")
st.button(btn_open_github)
    with center_column:
        st.markdown("[LinkedIn Page...](https://www.linkedin.com/in/sergio-oliveira-headofpeople/)")

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
