
import os
os.environ["OPENAI_API_KEY"] = "sk-mNqq4D8fFDb_2DzHx6op3WohrOgXh1q0RSxgQwFmvUT3BlbkFJCBGm1rMv-RGZhPCgftobM4CCJC9wsCauiFEqaaB7MA"

from langchain_openai import ChatOpenAI


# chatbot_logic.py

def chatbot_response(user_message):
    """
    Generates a chatbot response based on user input.
    Replace this logic with your actual chatbot's code.
    """
    if "hello" in user_message.lower():
        return "Hi there! How can I assist you today?"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you rephrase?"


















llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
our_query = "where can i find tech jobs ?"
completion = llm(our_query)
print(completion)