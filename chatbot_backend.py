from langgraph.graph import StateGraph,START,END 
import streamlit as st
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="AIzaSyB5I_QHm08l-LrrCR6pQhputZr6GzwT9nw"
)

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    messages=state['messages']
    response=model.invoke(messages)
    return {'messages':[response]}

checkpointer=InMemorySaver()

graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)