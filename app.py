# import streamlit as st
import pickle
import torch


# Load your model (replace with the actual code to load your model)
# For example:
# from your_model_module import load_model
# model = load_model()


# Dummy load model function (replace this with your actual model loading code)
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Define a function to load your model and tokenizer
def load_model_and_tokenizer(model_path):
    model = AutoModelForCausalLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer



# Load the model and tokenizer
model_path = "C:\\Users\\user\\Pictures\\YEAR 2 SEMESTER 2\\Introduction to AI\\AI_Final_Project"  # Path to the directory with your model files
model, tokenizer = load_model_and_tokenizer(model_path)

# Health-conscious color scheme
primaryColor = "#6B8E23"  # Olive green
backgroundColor = "#F5FFFA"  # Mint cream
secondaryBackgroundColor = "#98FB98"  # Pale green
textColor = "#556B2F"  # Dark olive green
font = "sans-serif"

# Streamlit app layout
st.set_page_config(
    page_title="Health-Conscious Meal Planner Chatbot",
    page_icon=":leafy_green:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set CSS for health-conscious colors
st.markdown(f"""
    <style>
    .reportview-container {{
        background: {backgroundColor};
    }}
    .sidebar .sidebar-content {{
        background: {secondaryBackgroundColor};
    }}
    .st-bb {{
        color: {textColor};
    }}
    .st-at {{
        color: {textColor};
    }}
    .st-bx {{
        color: {textColor};
    }}
    .css-1d391kg {{
        font-family: {font};
    }}
    </style>
    """, unsafe_allow_html=True)


# Title of app
#st.title('AI Nutritionist')
st.write("Welcome! Ask me about meal plans, nutritional advice, and more.")

# Adds nutritionist model to app's session state (stores persistent data of app)
#if 'model' not in st.session_state:
  #st.session_state['model'] = 's'

# Adds messages list to app's session state to keep user and chatbot messages
if 'messages' not in st.session_state:
  st.session_state.messages = []

# Enables user input and chatbot responses to be stored in messages
for message in st.session_state.messages:
  with st.chat_message(message['role']):
    st.markdown(message['content'])

# Receives user input
if prompt := st.chat_input('Enter prompt'):
  st.session_state.messages.append({'role': 'user', 'content': prompt}) # Adds input as part of content entered in user part of messages
  with st.chat_message('user'):
    st.markdown(prompt)

  # Generating the model response
  with st.chat_message('dietitian'):
    output = generate_response(st.session_state.messages[-1]['content'])
    response = st.write(output)
    st.session_state.messages.append({'role': 'dietitian', 'content': response})