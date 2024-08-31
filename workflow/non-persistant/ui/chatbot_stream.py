# Langchain Libraries
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Gradio - UI
import gradio as gr

# LLM - Try with ChatGroq, ChatOllama etc
llm = ChatOpenAI(temperature=1.0, model="gpt-4o", streaming=True)

# Code from the documentation - https://www.gradio.app/guides/creating-a-chatbot-fast#a-langchain-example
def predict(message, history):
    history_langchain_format = [SystemMessage(content="You are a helpful assistant.")]

    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    history_langchain_format.append(HumanMessage(content=message))

    partial_message = ""
    for chunk in llm.stream(history_langchain_format):
        partial_message += chunk.content
        yield partial_message


gr.ChatInterface(predict).launch()
