import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

st.markdown("""
    <style>
    /* Import a Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Change the overall font of the app */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Customize user messages */
    .stChatMessageUser {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
        background-color: #0078d4;
        border-radius: 12px;
        padding: 10px;
    }

    /* Customize bot messages */
    .stChatMessageAssistant {
        font-family: 'Poppins', sans-serif;
        color: #333333;
        background-color: #f0f2f6;
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

user_input=st.chat_input("Type Here: ")

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]
    
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
CONFIG={'configurable':{'thread_id':"thread-1"}}

if user_input:
    
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.markdown(user_input)
        
    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    
    ai_message=response['messages'][-1].content
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        st.markdown(ai_message)