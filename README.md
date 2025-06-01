# pure-python-qa-agent
# 🤖 Pure Python Q&A Agent

A lightweight, terminal-based assistant that answers your questions using GPT-4.  
Short-term memory included. No frameworks. Just Python.

---

## 🧠 What It Is

This project is part of the **Pure Python AI Agent** series and demonstrates how to build a Q&A assistant using:

- A prompt loop
- Short-term conversation memory
- The OpenAI API (official Python SDK)
- Absolutely no frameworks like LangChain or AutoGen

---

## 🔍 What It Does

- Accepts user questions via the terminal
- Sends them to GPT-4 for accurate, helpful responses
- Maintains short-term memory across ~5 user-agent exchanges
- Clears memory automatically when the limit is reached

Perfect for learning how multi-turn logic works in plain Python.

---

## 📂 File Structure

pure-python-qa-agent/
├── main.py # Core agent loop with memory slicing
├── config.py # Loads the OpenAI API key from the environment
├── requirements.txt # Dependency list (just openai)
└── README.md # You are here

## 🛠️ Setup

1. Clone this repo:

```bash
git clone https://github.com/your-username/pure-python-qa-agent
cd pure-python-qa-agent
