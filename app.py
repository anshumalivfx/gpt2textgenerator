import streamlit as st
from aitextgen import aitextgen
st.set_page_config(page_title="Anshumali's AI Paragraph Generator", page_icon="🤖", layout="centered", initial_sidebar_state="expanded")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

ai = aitextgen()

st.title("AI Paragraph Generator")
# prompt_text = "I Hate My Life"
form = st.form(key='my_form')
prompt_text = form.text_input(label="Enter your prompt text: ", value="")
submit_button = form.form_submit_button(label='Submit')

with st.spinner("AI is Generating response..."):
    gpt_text = ai.generate_one(prompt=prompt_text,
                max_length=500
                )
st.success("AI Paragraph Successfully Generated")
st.balloons()
print(gpt_text)
st.text(gpt_text)
