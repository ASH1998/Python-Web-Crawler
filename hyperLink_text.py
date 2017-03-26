from tkinter import *
import webbrowser

string_links = ''
i = 1

def openBrowser(event):
    selected_link = T.selection_get()
    print(selected_link)
    webbrowser.open(selected_link)

fopen = open('animeshow/queue.txt', 'r').readlines()


for links in fopen:
    string_links += str(i) + '. ' + links
    i+=1

root = Tk()
s = Scrollbar(root)
T = Text(root, height=40, width=80, fg='blue', cursor='hand2')
s.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
T.bind('<Button-1>', openBrowser)
s.config(command=T.yview)
T.insert(END, string_links)
T.config(yscrollcommand=s.set, state=DISABLED)
mainloop()

