import streamlit as st
from PIL import Image
import os

st.set_page_config(
        page_title="Experience",page_icon=":man_in_business_suit_levitating:"
        )


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Define the app title
st.title('Experience')
st.write("---")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(" **Since:** 2021")
        st.write("**Company:** bolttech")
        st.write(" **Role:** Group Organizational Development Lead""")

    with right_column:
        image = Image.open('bolttech.png')
        st.image(image)

st.write("---")
st.markdown(""" 
            As a Development Lead, my focus is crafting and implementing impactful development programs aimed at empowering individuals while ensuring future-readiness for the company. 
            I'm particularly intrigued by the evolving role of AI in talent development, constantly exploring ways to integrate technology seamlessly into our learning initiatives.
        
            By leveraging my expertise in organizational development and my curiosity about AI's potential, 
            I strive to design strategies that bridge skill gaps and equip our workforce for an ever-evolving landscape. 
            Through tailored programs encompassing leadership development, technical skill enhancement, and a keen eye on AI's influence, 
            I'm dedicated to cultivating a workforce that not only adapts but excels in embracing the future.
            """)
st.write("---")
st.markdown(" ### Previous Experience and roles ### ")
st.write("---")
st.write(""" 
            With over 10 years of experience in global companies I've garnered extensive expertise in diverse People Partner roles, supporting the establishment of HR functions and implementing strategies that harmonize across cultures and geographies. 
            Key aspects of my experience include:
            
            * Global People Partner Expertise:  Contributing to the establishment and enhancement of HR functions on an international scale.
            * Cross-Cultural HR Strategy: Proficient in developing and aligning HR strategies within multinational environments, while ensuring alignment with global business objectives.
            * Setup & Optimization of HR Functions: Led the inception and optimization of HR frameworks from scratch within global organizations, fostering inclusive work cultures while adapting practices to resonate effectively across various regions. 
            * Data-Driven HR Insights: Leveraged data  to measure the impact of HR initiatives across global teams, providing insights that contribute significantly to the achievement of organizational goals on an global scale. 
            """)

st.write("---")

if st.button("Download CV"):
        os.startfile(r"Sérgio__Oliveira_-DevelopmentLead.pdf")



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
