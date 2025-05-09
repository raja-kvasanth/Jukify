from tkinter import*
import pygame
from tkinter import filedialog
root=Tk()
root.title("Music Player")
root.geometry("400x600")
root.configure(bg="#B03060")
lbl=Label(root,text="🎶playlist🎶",bg="#B03060",fg="#F3EAD3",font=("ROG Fonts",24))
lbl.pack()

#initialize pygame mixer
pygame.mixer.init()

#add song function
def addsong():
    song=filedialog.askopenfilename(initialdir="audios/",title="Choose a song",filetypes=(("MP3 File","*MP3"),))
    #replace the song info to get the exact song name
    song=song.replace("D:/Python/PYTHON/Project-Music player/audios/","")
    song=song.replace(".mp3","")
    #add song to the listbox
    songbox.insert(END,song)

#add songs to playlist
def addsongs():
    songs=filedialog.askopenfilenames(initialdir="audios/",title="select songs",filetypes=(("MP3 File","*MP3"),))
    for song in songs:
        song=song.replace("D:/Python/PYTHON/Project-Music player/audios/","")
        song=song.replace(".mp3","")
        songbox.insert(END,song)
        

#add play function
def play():
    song=songbox.get(ACTIVE)
    song=f"D:/Python/PYTHON/Project-Music player/audios/{song}.mp3"
   # song=
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#add stop function
def stop():
    pygame.mixer.music.stop()
    songbox.selection_clear(ACTIVE)

def forward():
    nextsong=songbox.curselection()
    nextsong=nextsong[0]+1
    song=songbox.get(nextsong)
    song=f"D:/Python/PYTHON/Project-Music player/audios/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0,END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong,last=None)

def previous():
    nextsong=songbox.curselection()
    nextsong=nextsong[0]-1
    song=songbox.get(nextsong)
    song=f"D:/Python/PYTHON/Project-Music player/audios/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0,END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong,last=None)
    

#create menu
mymenu=Menu(root)
root.configure(menu=mymenu)

#add (Add song) menu
addsongmenu=Menu(mymenu)
mymenu.add_cascade(label="Add song",menu=addsongmenu)
#addsongmenu.add_command(label="Add a song to playlist",command=addsong)
addsongmenu.add_command(label="Add songs",command=addsongs)

#create playlist box
songbox=Listbox(root,bg="#F3EAD3",fg="black",width=40,height=26,selectbackground="#d98294",selectforeground="black")
songbox.pack(pady=20)

#create player control frame
controlsframe=Frame(root,bg="#B03060")
controlsframe.pack()

#create player control buttons
prebutton=Button(controlsframe,text="|<",bg="#F3EAD3",fg="black",font=("ROG Fonts",13,"bold"),command=previous)
playbutton=Button(controlsframe,text="▶",bg="#F3EAD3",fg="black",font=("Verdana",13,"bold"),command=play)
pausebutton=Button(controlsframe,text="🔳",bg="#F3EAD3",fg="black",font=("ROG Fonts",13,"bold"),command=stop)
nextbutton=Button(controlsframe,text=">|",bg="#F3EAD3",fg="black",font=("ROG Fonts",13,"bold"),command=forward)

prebutton.grid(row=7,column=0,padx=8,pady=20)
playbutton.grid(row=7,column=1,padx=8,pady=20)
pausebutton.grid(row=7,column=2,padx=8,pady=20)
nextbutton.grid(row=7,column=3,padx=8,pady=20)

root.mainloop()

