from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calm Buddy")
root.geometry("350x200")
root.resizable(0,0)

# Dictionary of predefined questions and answers
chatbot_responses = {
    "Hi there": "Hello! How are you feeling today?",
    "I'm feeling quite stressed out": "I'm sorry to hear that. Stress can be tough. What has been causing you stress lately?",
    "Work has been overwhelming, having difficulties with time management and it is affecting my sleep": "I see. Work-related stress can impact sleep. Have you tried any relaxation techniques or spoken to someone about how you're feeling?",
    "I haven't tried anything yet": "It might be beneficial to explore relaxation methods like deep breathing or meditation. Also, talking to a friend, family member, or a professional can offer valuable support.",
    "I'm not sure if I'm ready to talk about it": "It's okay to feel uncertain. Speaking with a professional can be very helpful. I can also provide resources or information on managing stress if you'd like.",
    "That would be helpful, thanks." : "Absolutely! Here are some stress management techniques you might find beneficial: deep breathing exercises, regular physical activity, maintaining a healthy diet, and setting aside time for enjoyable activities.",
    "I'll try some of those. Thanks for the suggestions!": "You're welcome! Taking care of your mental health matters. If you ever feel overwhelmed or need further assistance, consider reaching out to a mental health professional. I'm here to support you whenever you need it.",
    "Goodbye": "Goodbye! Have a great day!"
}

def get_response():
    user_message = chatbot_entry.get()
    response = chatbot_responses.get(user_message, "I'm sorry, I don't understand that.")
    messagebox.showinfo("CalmBuddyBot", response)

Label(root, text="A simple chatbot", font=("Timeroman 15 bold"), fg="black").pack()

frame1 = Frame(root)
Label(frame1, text="I'm here to help!: ", font=("timeroman 12 bold"), fg='black').pack(side=LEFT)
chatbot_entry = Entry(frame1, width="38", borderwidth=6, font=("timeroman 10 bold"))
chatbot_entry.pack()
frame1.pack(pady=10)


send_button = Button(root, text="Message Me ❤︎ ", borderwidth=6, font=('timeroman 8 bold'), command=get_response)
send_button.pack(pady=20)

root.mainloop()
