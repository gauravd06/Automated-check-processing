from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import*
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Functions
def select_path():
    #allows user to select the path from the explorer
    path = filedialog.askdirectory()
    path_lable.config(text=path)
    
def getResolution():
    
    url= link_field.get() #getting link from the user
    resolutions = set() #set that holds the resolutions available

    try:
        yt = YouTube(url) #creating the object that stores information about the video

        for stream in yt.streams.filter(type="video"): # Only look for video streams
            resolutions.add(stream.resolution) #Adding all resolutions available

        resolutions=list(resolutions) #list containing all resolutions

    except Exception as e:
        mb.showerror('Error',e)
    return






#Creating a radio button for each resolution
R1 = Radiobutton(wn, text='144p', variable=res, value='144p')
R1.place(x=100,y=100)
R1.deselect()
R2=Radiobutton(wn, text='240p', variable=res, value='240p')
R2.place(x=100,y=130)
R2.deselect()
R3=Radiobutton(wn, text='360p', variable=res, value='360p')
R3.place(x=100,y=160)
R3.deselect()
R4=Radiobutton(wn, text='480p', variable=res, value='480p')
R4.place(x=100,y=190)
R4.deselect()
R5=Radiobutton(wn, text='720p', variable=res, value='720p')
R5.place(x=100,y=220)
R5.deselect()
R6=Radiobutton(wn, text='1080p', variable=res, value='1080p')
R6.place(x=100,y=250)
R6.deselect()
R7=Radiobutton(wn, text='2016p', variable=res, value='2016p')
R7.place(x=100,y=280)
R7.deselect()

#disabling those radio buttons that are not available in the video
if('144p' not in resolutions):
R1.config(state = DISABLED)
elif('240p' not in resolutions):
R2.config(state = DISABLED)
elif('360p' not in resolutions):
R3.config(state = DISABLED)
elif('480p' not in resolutions):
R4.config(state = DISABLED)
elif('720p' not in resolutions):
R5.config(state = DISABLED)
elif('1080p' not in resolutions):
R6.config(state = DISABLED)
elif('2016p' not in resolutions):
R7.config(state = DISABLED)


downloadBtn = Button(wn, text='Download', font=7, fg='grey19',
command=downloadVideo).place(x=100,y=350)

quitBtn = Button(wn, text='Quit', font=7, fg='grey19',
command=wn.destroy).place(x=350,y=350)

def download_file():
     #get user path
    get_link = link_field.get()
    #get_selected path
    user_path = path_lable.cget("text")
    screen.title("Downloading......")
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Download Another File...")
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete! Download Another File...")
screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file="download.png")
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_lable =Label(screen, text="Enter Download Link:", font=("Arial", 15))

#select Quality
Quality_lable = Label(screen,text="select Quality",font=("Arial",15))
Quality_btn = Button(screen,text="select Quality",command = select_quality)

#select path for saving the file
path_lable = Label(screen, text="select path for Download",font=("Arial",15))
select_btn = Button(screen, text="select", command=select_path)
#Add to window
canvas.create_window(250, 330, window=path_lable)
canvas.create_window(250, 360, window=select_btn)

#Add to window
canvas.create_window(250, 250, window=Quality_lable)
canvas.create_window(250, 280, window=Quality_btn)

#Add widgets to window
canvas.create_window(250, 170, window=link_lable)
canvas.create_window(250, 200, window=link_field)


#Download btns
download_btn = Button(screen, text="Download File", command=download_file)
#add to canvas
canvas.create_window(250, 410, window=download_btn)
screen.mainloop()
