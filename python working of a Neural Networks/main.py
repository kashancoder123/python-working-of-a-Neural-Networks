import tkinter as tk

# Simple responses for the chatbot
responses = {
    "hi": "Hello! How can I help you today?",
    "how are you?": "I'm just a program, but thanks for asking!",
    "what is your name?": "I'm a simple chatbot created with Tkinter and Python.",
    "what can you do?": "I can chat with you and answer simple questions!",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "who created you?": "I was created by a Python programmer using Tkinter.",
    "thank you": "You're welcome! Happy to help!",
    "bye": "Goodbye! Have a great day!", 
}

# Function to handle sending messages
def send_message():
    user_input = entry.get().lower().strip()
    chat_window.config(state=tk.NORMAL)

    # Show user message
    chat_window.insert(tk.END, "You: " + user_input + "\n")

    # Chatbot reply
    if user_input in responses:
        reply = responses[user_input]
    elif user_input == "bye":
        reply = "Goodbye! Have a great day! 👋"
    else:
        reply = "I'm sorry, I don't understand that. Can you ask something else?"
    
    chat_window.insert(tk.END, "BuddyBot: " + reply + "\n\n")

    chat_window.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Tkinter window
window = tk.Tk()
window.title("BuddyBot Chatbot")
window.geometry("400x500")
window.config(bg="#FFEAA7")

# Chat display box
chat_window = tk.Text(window, bg="#FFF5D1", fg="black", font=("Arial", 12))
chat_window.config(state=tk.DISABLED)
chat_window.pack(pady=10)

# Input box
entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Send button
send_button = tk.Button(window, text="Send", font=("Arial", 12, "bold"), bg="#FFB142", command=send_message)
send_button.pack(pady=5)

# Run the app 
window.mainloop()