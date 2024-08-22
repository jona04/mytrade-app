from langchain.prompts import Prompt
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    load_dotenv()
    print_hi("PyCharm")


    summary_template = """
        given the price dada below, please give me recommendations:
        close: {close}
        RSI: {rsi}
        ADX: {adx}
    """

    summary_prompt_template = PromptTemplate(input_variables=["close", "rsi", "adx"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3.1")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"close": 1232, "rsi": 32, "adx": 25})

    print(res)