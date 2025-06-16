import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quest(name_seed):
    prompt = f"Generate a detailed game quest description for Cyberpunk-themed game with seed '{name_seed}'. Include objectives, rewards, difficulty level."
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content

if __name__ == "__main__":
    print(generate_quest("Tutorial"))
