def getResolution():
    url= yt_link.get() #getting link from the user
    resolutions = set() #set that holds the resolutions available
    try:
    yt = YouTube(url) #creating the object that stores information about the video
    for stream in yt.streams.filter(type="video"): # Only look for video streams
    resolutions.add(stream.resolution) #Adding all resolutions available
    resolutions=list(resolutions) #list containing all resolutions
    except Exception as e:
    mb.showerror('Error',e)
    return
#creating a new window
wn = Tk()
wn.title("Youtube Video Downloader by ProjectGurukul")
wn.geometry('700x500')
wn.config(bg='honeydew2')
# Heading label
Label(wn, text="Youtube Video Downloader by ProjectGurukul", font=('Courier', 15), fg='grey19').place(x=100,y=15)
Label(wn, text="The available resolutions are checkable. \n Please choose one of the resolutions and click on the download button",
font=('Courier', 10), fg='grey19').place(x=20,y=50)
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