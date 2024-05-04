import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests


st.set_page_config(page_title= "jonah", page_icon=":fire:", layout= "wide")

st.subheader("hi, im Jonah Cryer. ")
st.write("---")
st.title("I am a beginning coder trying to learn python.")
st.write("I think programming is a useful skill, and everyone should learn. I want to learn to program, so that is why i am making this website.")
st.write("---")
st.write("", "I think the best way to learn is to teach.", "I am using this website to teach people to program",)
st.write("---")



st.title("PROGRAMMING BASICS")
st.write("Programming is more of a way of thinking than learning meaningless random numbers and symbols.", )
st.write("If you can think like a programmer, then it becomes easy to learn the rules to write a program")
st.write("")
st.write("LETS WRITE OUR FIRST PROGRAM!", "In your favorite text editor, type this into a new folder.", )
st.write("print('hello world')")
st.write("CONGRATS! YOU JUST WROTE YOUR FIRST LINE OF CODE! try running the program and see what happens. you should see your program print, hello")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return R.json()

lottie_coding = load_lottieurl("https://lottie.host/embed/8b230fd2-1a06-4adc-92b9-fa833802462c/OJlEpwe52R.json")

