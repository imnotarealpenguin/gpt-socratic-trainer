# scripts/socratic_session.py

"""
Launch a Socratic dialogue session powered by GPT-4.
GPT asks deep questions. You answer. It follows up.
"""

import openai

openai.api_key = "YOUR-OPENAI-API-KEY"  # Replace with your own

# Get the topic
with open("input/topic.txt", "r") as file:
    topic = file.read().strip()

# Define the system prompt
system_prompt = """
You are a Socratic tutor.
Your job is to teach by asking questions — not giving answers.
Ask 1 question at a time and follow up based on the student's reply.
"""

# Initialize conversation
print("🧠 GPT Socratic Trainer")
print(f"Topic: {topic}\n")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"I want to understand: {topic}"}
]

while True:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    
    question = response["choices"][0]["message"]["content"]
    print(f"GPT: {question}")
    
    user_reply = input("You: ")
    messages.append({"role": "assistant", "content": question})
    messages.append({"role": "user", "content": user_reply})
