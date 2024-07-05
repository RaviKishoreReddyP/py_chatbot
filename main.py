from tkinter import *
from tkinter import scrolledtext


#define keywords for conversations

greetings=["hi","hello","namaste","hii","good morning","good evening","good afternoon"]
emotions=["how are you","how are you ?","do you like people","i love you","marry me"]
about=["what is your name ?","what is your name","who are you ?","who are you"]
dos=["what can you do","what is your capacity","what is your capabilities","how can you help me","help me"]
thanks=["thanks","thank you","thank you so much"]
bye=["goodbye","bye","see you later","see ya"]
joke=["tell me a joke","joke","tell me something","funny","comedy"]
creator=["who made you","your boss","your creator","who is your boss","who trained you"]

#add your possible conversations

#function of chat bot
def Enter():

    UserInput=input_text.get("1.0",END).strip()
    display_text.config(state=NORMAL)
    display_text.insert(END,"You: "+UserInput+"\n","user")
    UserInput=UserInput.lower()

    if any(x in UserInput for x in greetings):
        display_text.insert(END,"Bot: "+"Hi! How Can I help u?\n","bot")

    elif any(x in UserInput for x in emotions):
        display_text.insert(END, "Bot: " + "I am Bot does not have emotions\n", "bot")

    elif any(x in UserInput for x in about):
        display_text.insert(END, "Bot: " + "I'm a chatbot\n", "bot")

    elif any(x in UserInput for x in joke):
        display_text.insert(END, "Bot: " + "why do cows always wear bells ?  because their horns didn't work \n", "bot")

    elif any(x in UserInput for x in thanks):
        display_text.insert(END, "Bot: " + "welcome\n", "bot")

    elif any(x in UserInput for x in dos):
        display_text.insert(END, "Bot: " + "I can answer questions and have a chat with you\n", "bot")

    elif any(x in UserInput for x in bye):
        display_text.insert(END, "Bot: " + "Have a nice day\n", "bot")

    elif any(x in UserInput for x in creator):
        display_text.insert(END, "Bot: " + "RAVI KISHORE REDDY P\n", "bot")

    else:
        display_text.insert(END, "Bot: " + "Not sure How to Reply!\n", "bot")

    display_text.config(state=DISABLED)
    input_text.delete("1.0",END)


#chat bot interface

root= Tk()
root.title("my chat bot")
root.geometry("500x600")

header=Label(root,text="My Chat Bot",bg="Dark Blue",fg="white",font=("Georgia",24))
header.pack(fill=X,expand=True)

display_text=scrolledtext.ScrolledText(root,state=DISABLED,wrap=WORD)
display_text.pack(fill=BOTH,expand=True)

Label(text="Input:").pack()

input_text=scrolledtext.ScrolledText(root,wrap=WORD,height=3)
input_text.pack(fill=BOTH,expand=True)

#text colour
display_text.tag_config("user",foreground="Red")
display_text.tag_config("bot",foreground="Green")

enter=Button(root,text="Enter",font=("Georgia",10),command=Enter)
enter.pack()

root.mainloop()
