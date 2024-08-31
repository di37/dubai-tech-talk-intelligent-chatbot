import os
from dotenv import load_dotenv

# Langchain Libraries
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Firebase Libraries
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory

# Gradio - UI
import gradio as gr

# Loading Environment Variables
_ = load_dotenv()

## Firestore Database initialization
PROJECT_ID = os.getenv("PROJECT_ID")
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)


llm = ChatOpenAI(temperature=1.0, model="gpt-4o", streaming=True)

if chat_history.messages == []:
    chat_history.add_message(SystemMessage(content="You are a helpful assistant."))
    print("System message added")

def predict(message):
    # Add only the new message to the chat history
    chat_history.add_user_message(message)

    partial_message = ""
    for chunk in llm.stream(chat_history.messages):
        partial_message += chunk.content
        yield partial_message

    # After generating the complete response, add it to the chat history
    chat_history.add_ai_message(partial_message)


gr.ChatInterface(predict).launch()
