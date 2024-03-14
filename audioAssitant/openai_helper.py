import openai
from api_key import api_key ,openai_key

openai.api_key = openai_key

def ask_computer(prompt):

    # prompt = "What is your favorite color?"
    res = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
    )
    # print(res)
    return res["choices"][0]["text"]