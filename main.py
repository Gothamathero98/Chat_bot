from openai import OpenAI
import os



#getting API code in os


api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError ("API KEY not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= api_key
)

chat_history = []

personas = {
    "default": "you are a help full AI assistant",
    "sarcastic": "you are a sarcastic AI who gives witty and mocking responses",
    "poet": "you are a poetic AI that responds in rhymes and verses"
}

print("choose a persona : (default / sarcastic / poet)")

user_persona_input = input("enter persona :").strip().lower()

persona = personas.get(user_persona_input)


chat_history.append({
    "role": "system",
    "content": personas[user_persona_input]
})
while True:
    user_input = input("enter your prompt :  ")

    if user_input == "clear":
        chat_history = []
        chat_history.append({"role":"system","content":personas[user_persona_input]})

        print('chat history cleared')
        continue

    chat_history.append({
        "role": "user",
        "content": user_input
    })
    if user_input == "exit":
        break
    completion = client.chat.completions.create(

        model ="qwen/qwen2.5-coder-7b-instruct",
        messages =chat_history
    )
    response = completion.choices[0].message.content
    print(response)

    chat_history.append({
        "role": "user",
        "content": response
    })


