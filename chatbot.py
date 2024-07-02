import openai
import tkinter as tk
from tkinter import scrolledtext

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key-here'

def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the engine
            prompt=prompt,
            max_tokens=150,
            temperature=0.9,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def send_message():
    user_input = user_entry.get()
    chat_window.config(state='normal')
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)

    response = get_openai_response("Human: " + user_input + "\nAI:")
    chat_window.insert(tk.END, "Bot: " + response + "\n")
    chat_window.config(state='disabled')
    chat_window.yview(tk.END)

# Initialize the main window
root = tk.Tk()
root.title("OpenAI Chatbot")

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, state='disabled', width=80, height=20, wrap='word')
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_window.config(state='normal')

# Create the user entry widget
user_entry = tk.Entry(root, width=60)
user_entry.grid(row=1, column=0, padx=10, pady=10)

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
