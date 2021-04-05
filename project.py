from tkinter import *
import hashlib
from tkinter import filedialog
root=Tk()
root.geometry("300x200")
root.configure(bg="blue")
def MD5():
    path = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.txt")])
    data=open(path,"r").read()
    result=hashlib.md5(data.encode())
    try:
        f = open(path.split("/")[-1].split(".txt")[0]+"-MD5.txt", "r+")
        f.truncate(0)
    except:
        pass
    print(result.hexdigest())
    f = open(path.split("/")[-1].split(".txt")[0]+"-MD5.txt", "a")
    f.write(result.hexdigest())
    f.close()
def SHA256():
    path = filedialog.askopenfilename(title="Select file",filetypes=[("Text Files", "*.txt")])
    data=open(path,"r").read()
    result=hashlib.sha256(data.encode())
    print(result.hexdigest())
    try:
        f = open(path.split("/")[-1].split(".txt")[0]+"-SHA256.txt", "r+")
        f.truncate(0)
    except:
        pass
    f = open(path.split("/")[-1].split(".txt")[0]+"-SHA256.txt", "a")
    f.write(result.hexdigest())
    f.close()
Button_MD5=Button(root,text="Apply MD5",bg="gold",relief=FLAT,command=MD5)
Button_MD5.place(relx=0.3,rely=0.5,anchor=CENTER)
Button_SHA256=Button(root,text="Apply SHA256",bg="gold",relief=FLAT,command=SHA256)
Button_SHA256.place(relx=0.7,rely=0.5,anchor=CENTER)
root.mainloop()
