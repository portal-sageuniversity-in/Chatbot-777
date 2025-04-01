import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Page setup
st.set_page_config(
    page_title="Financial Advisor AI",
    page_icon="💰"
)

# Basic styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header
st.title("💰 Financial Advisor AI")
st.markdown("Ask me anything about finance!")

# Chat function
def get_ai_response(prompt):
    text = f'''You are a financial expert AI assistant. Your task is to provide insightful responses 
    to the following user query related to finance: {prompt} 
    For any other topic, respond with "I'm sorry, I can only provide advice about financial topics."'''
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": text}],
            model="deepseek-r1-distill-llama-70b",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Display chat history
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.write("You: " + message["content"])
        else:
            st.write("AI: " + message["content"])

# User input
user_input = st.text_input("Your question:", key="input")
if st.button("Ask"):
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get AI response
        ai_response = get_ai_response(user_input)
        
        # Add AI response to history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        # Rerun to update chat
        st.rerun()

# Footer
st.markdown("---")
st.markdown("*Ask questions about investments, budgeting, savings, and more!*")