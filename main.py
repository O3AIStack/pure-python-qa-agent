# main.py

import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

# Define system prompt for Q&A role
system_prompt: ChatCompletionMessageParam = {
    "role": "system",
    "content": (
        "You are a factual Q&A assistant. "
        "Answer user questions clearly and concisely. "
        "If you don’t know, say so."
    )
}

# Short-term memory (conversation log)
MAX_MEMORY_MESSAGES = 10  # 5 user-assistant turns
conversation: list[ChatCompletionMessageParam] = [system_prompt]

print("🤖 Q&A Assistant is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in {"exit", "quit"}:
        print("Agent: Goodbye!")
        break

    # Add user input to conversation
    conversation.append({"role": "user", "content": user_input})

    # Trim memory if it exceeds the max (keep system + recent messages)
    if len(conversation) > MAX_MEMORY_MESSAGES + 1:
        conversation = [system_prompt] + conversation[-MAX_MEMORY_MESSAGES:]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        reply = response.choices[0].message.content
        print("Agent:", reply)

        # Add assistant response to conversation
        conversation.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Agent Error:", str(e))
