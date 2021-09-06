# Programmer - python_scripts (Abhijith Warrier)
#
# PYTHON GUI TO Zip And unZip FILES USING zipfile() LIBRARY OF PYTHON
#
# The ZIP file format is a common archive and compression standard. This module provides tools
# to create, read, write, append, and list a ZIP file.
# This module does not currently handle multi-disk ZIP files. It can handle ZIP files that use
# the ZIP64 extensions.
#
# The zipfile module is an inbuilt module in Python

# Importing necessary packages
import os
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox, filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    selectlabel = Label(root, text="FILES TO ZIP : ", bg="plum4")
    selectlabel.grid(row=0, column=0, padx=5, pady=5)

    root.zipFilesEntry = Text(root, height=4, width=39)
    root.zipFilesEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    zipBrowseButton = Button(root, text="BROWSE", width=15, height=1, command=ZipFileBrowse)
    zipBrowseButton.grid(row=0, column=3, padx=5, pady=5)

    zipNamelabel = Label(root, text="ZIPPED LOCATION : ", bg="plum4")
    zipNamelabel.grid(row=1, column=0, padx=5, pady=5)

    root.zipFolderEntry = Entry(root, width=30, textvariable=zipFileName)
    root.zipFolderEntry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    zipSaveBrowse = Button(root, text="BROWSE", width=15, height=1, command=ZipSaveBrowse)
    zipSaveBrowse.grid(row=1, column=3, padx=5, pady=5)

    ZipButton = Button(root, text="ZIP", width=20, command=ZipFiles)
    ZipButton.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

    unzipFilelabel = Label(root, text="FILE TO UNZIP : ", bg="plum4")
    unzipFilelabel.grid(row=3, column=0, padx=5, pady=5)

    root.unzipFilesEntry = Text(root, height=4, width=39)
    root.unzipFilesEntry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    unZipBrowseButton = Button(root, text="BROWSE", width=15, command=unZipFileBrowse)
    unZipBrowseButton.grid(row=3, column=3, padx=5, pady=5)

    unzipFileNamelabel = Label(root, text="UNZIPPED LOCATION: ", bg="plum4")
    unzipFileNamelabel.grid(row=4, column=0, padx=5, pady=5)

    root.unzipFolderEntry = Entry(root, width=30, textvariable=unzipFolderName)
    root.unzipFolderEntry.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    unzipSaveBrowse = Button(root, text="BROWSE", width=15, command=unZipSaveBrowse)
    unzipSaveBrowse.grid(row=4, column=3, padx=5, pady=5)

    unZipButton = Button(root, text="unZIP", width=15, command=unZipFiles)
    unZipButton.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

# Defining ZipBrowse() to select the files to Zip
def ZipFileBrowse():
    # Prompting to select the files to zip and storing the list in zipFileSelection variable
    # Setting initialdir argument is optional
    root.zipFileSelection = filedialog.askopenfilenames(initialdir = "YOUR DIRECTORY PATH")
    # Looping through the list and displaying the file name in the zipSelectEntry widget
    for files in root.zipFileSelection:
        root.files = os.path.basename(files)
        root.zipFilesEntry.insert('2.0',root.files+"\n")
    root.zipFilesEntry.config(state=DISABLED)

# Defining unZipBrowse() to select the ZIP file to UnZip
def unZipFileBrowse():
    # Prompting to select zipped file to unzip & storing name in unZipFileSelection variable
    root.unzipFileSelection = filedialog.askopenfilename(initialdir = "YOUR DIRECTORY PATH")
    # Displaying the file name in the zipSelectEntry widget
    # Fetching only the file's name from the path
    root.files = os.path.basename(root.unzipFileSelection)
    root.unzipFilesEntry.insert('1.0',root.files+"\n")
    root.unzipFilesEntry.config(state=DISABLED)

# Defining the ZipSaveBrowse() to select the location to save zipped folder
def ZipSaveBrowse():
    # Prompting to select the location and name to save the zipped file
    zipSaveDestination = filedialog.asksaveasfilename(initialdir = "YOUR DIRECTORY PATH")
    # Setting the tkinter variable to the zipSaveDestination Value
    zipFileName.set(zipSaveDestination)
    # Displaying the zipSaveDestination Value in the zipFolderEntry
    root.zipFolderEntry.config(text=zipSaveDestination)

# Defining the unZipSaveBrowse() to select the location to save unzipped folder
def unZipSaveBrowse():
    # Prompting to select the location and name to save the zipped file
    unZipSaveDestination = filedialog.asksaveasfilename(initialdir = "YOUR DIRECTORY PATH")
    # Setting the tkinter variable to the unZipSaveDestination Value
    unzipFolderName.set(unZipSaveDestination)
    # Displaying the unZipSaveDestination Value in the unzipFolderEntry
    root.unzipFolderEntry.config(text=unZipSaveDestination)

# Defining ZipFiles() function to zip files
def ZipFiles():
    # Opening the user-entered zipped folder name in write mode with zip_file as file object
    with ZipFile(zipFileName.get(), 'w') as zip_file:
        # Looping through each file in the root.zipFileSelection list
        for file in root.zipFileSelection:
            # Writing the file into the zipped folder using write() method of ZipFile class
            # 1st argument files - file with path
            # 2nd argument os.path.basename(files) - Selecting only file after removing path
            zip_file.write(file,os.path.basename(file))
    messagebox.showinfo("SUCCESS","FILES ZIPPED SUCCESSFULLY")

# Defining unZipFiles() function to unzip files
def unZipFiles():
    # Creating folder with user-input name into which files are to be extracted
    os.makedirs(unzipFolderName.get())
    # Opening the zipped file in read mode with unzip_file as file object
    with ZipFile(root.unzipFileSelection, 'r') as unzip_file:
        # Extracting files from zipped folder into created folder using extractall() of
        # ZipFile class
        unzip_file.extractall(unzipFolderName.get())
    messagebox.showinfo("SUCCESS",'FILES UNZIPPED SUCCESSFULLY')

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color disabling the resizing property
root.title("PythonZipperUnzipper")
root.config(background = "plum4")

# Creating tkinter variables
zipFileName = StringVar()
unzipFolderName = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
