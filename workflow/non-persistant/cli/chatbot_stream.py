from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Loading Environment Variables
_ = load_dotenv()

# LLM - Try with ChatGroq, ChatOllama etc
llm = ChatOpenAI(model="gpt-4o", temperature=0.2, max_tokens=512)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    query = input("You: ")
    if query == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    
    partial_message = ""
    print("AI: ", end="")
    for chunk in llm.stream(chat_history):
        print(chunk.content, end="", flush=True)
        partial_message += chunk.content
    print("\n")
    chat_history.append(AIMessage(content=partial_message))
