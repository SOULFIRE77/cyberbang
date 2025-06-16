import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_campaign(topic):
    prompt = f"Generate a marketing campaign outline for the game Cyberbang focusing on {topic}."
    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
    print(resp.choices[0].message.content)

if __name__ == "__main__":
    generate_campaign("Telegram airdrop event")
