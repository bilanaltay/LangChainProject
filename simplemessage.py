from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, dotenv_values
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
model = ChatOpenAI(model="gpt-4.1",temperature=0.3) #(0,1) arası yaratıcılık oranı

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)