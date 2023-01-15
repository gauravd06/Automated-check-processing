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
    
def select_quality():
    pass

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

#select path for saving the file
path_lable = Label(screen, text="select path for Download",font=("Arial",15))
select_btn = Button(screen, text="select", command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_lable)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window
canvas.create_window(250, 170, window=link_lable)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File", command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)
screen.mainloop()
