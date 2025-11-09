import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid

st.title("Mitra AI")

#*****************Utility Functions******************

def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)
        
def load_conversation(thread_id):
    state=chatbot.get_state(config={'configurable':{'thread_id':thread_id}})
    return state.values.get('messages',[])

#****************Session State***********************

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()
    
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=[]

add_thread(st.session_state['thread_id'])

#*****************SideBar UI**************************

st.sidebar.title("Mitra AI")
if st.sidebar.button("New Chat"):
    reset_chat()
st.sidebar.header("My Conversations")

# st.sidebar.button(str(st.session_state['thread_id']))

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_conversation(thread_id)
        
        temp_messages=[]
        
        for msg in messages:
            if isinstance(msg,HumanMessage):
                role='user'
            else:
                role='assistant'
            
            temp_messages.append({'role':role,'content':msg.content})
        
        st.session_state['message_history']=temp_messages

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
    
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
CONFIG={'configurable':{'thread_id':st.session_state['thread_id']}}

if user_input:
    
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.markdown(user_input)
        
    # response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    
    # ai_message=response['messages'][-1].content
    with st.chat_message('assistant'):
        ai_message=st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        )
    )
    
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})  