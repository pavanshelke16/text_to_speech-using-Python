import streamlit as st
import pyttsx3

def talk(text):
    speech = pyttsx3.init()
    speech.say(text)
    speech.runAndWait()

def main():
    st.title("Text-to-Speech App")

    # Get user input
    user_input = st.text_area("Enter the text you want the app to speak:")
    
    if st.button("Speak"):
        if user_input:
            talk(user_input)
        else:
            st.warning("Please enter some text.")

if __name__ == '__main__':
    main()
