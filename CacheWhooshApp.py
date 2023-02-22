# Cache Whoosh App
# @Hoccyy
# January 10, 2022
#
# Version: 0.0.1
#
#
#
# Various Pyqt5 imports needed for the app to work
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget, QFileDialog, \
QGridLayout, QMessageBox 
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# Imports subprocess
import subprocess
import webbrowser as wb
import time

# Checks operation timing
start = time.time()
# App initalization
app = QApplication (sys.argv)

# Window and grid initalized
window = QWidget()
grid = QGridLayout ()
window.setLayout (grid)

# Dictionary for widgets
widgets = {
    utton[
}

# Creates a button that clears cache
def cacheCLearButton (text, row, column):
    button = QPushButton (text)
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';}"
    )

    # Changes cursor on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # adds to dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column, 1, 1)
    # Does the function on click
    button.clicked.connect (clearCache1)

# Makes button to clear the recycling bin
def binCLearButton (text, row, column):
    button = QPushButton (text)
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';}"
    )

    # Changes cursor on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # adds to dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column, 1, 1)
    # Clears recycling bin on click
    button.clicked.connect (clearRec_bin)

# Makes the button to clear the secondary caches (in harddrive/windows/temp)
def cache2CLearButton (text, row, column):
    button = QPushButton (text)
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';}"
    )

    # Changes cursor on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # adds to dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column, 1, 1)
    # Activates the secondary cache clear function
    button.clicked.connect (clearCache2)

# Creates a button to give the user information
def InfoButt (text, row, column):
    button = QPushButton (text)
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';}"
    )
    # Changes cursor on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # Adds button to dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column, 1, 1)
    # Creates a pop up window on click, to give the user information
    button.clicked.connect (infDial)

# Function to create labels
def label_maker (text, row, column):
    label = QLabel (text)
    label.setStyleSheet (
        "*{color: 'white';" +
        "font-size: 35px;}" +
        "*:hover{color: 'grey';}"
    )
    label.setAlignment (QtCore.Qt.AlignCenter)
    label.setWordWrap (True)
    # adds button to dictionary
    widgets["Labels"].append (label)
    #                                       R     C
    grid.addWidget (widgets["Labels"][-1], row, column)

# Class to create windows
class mainWindow:
    # Uses parameters to set window specs
    def __init__ (self, width, height, title, style, icon):
        self.width = window.setFixedWidth (width)
        self.height = window.setFixedHeight (height)
        self.title = window.setWindowTitle (title)
        self.style = window.setStyleSheet (style)
        self.icon = window.setWindowIcon (icon)
    
    # Gets the directory for the windows/temp folder
    def temp2_directory ():
        # Prompts the user to enter the folder directory
        folderpath = QFileDialog.getExistingDirectory ()
        
        # Checks drive name with a loop
        x = 0
        # Temporary array
        drive_Name = []
        while folderpath[x] != ":":
            print (folderpath[x])
            # Adds the drive name to an array
            drive_Name.append (folderpath[x])
            x += 1
        # Ends the array with a colon
        drive_Name.append (':')

        # To prevent user error
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Shows drivename in the console
        # Variables to prevent the user from deleting VERY important folders accidentally
        # or for other nefarious purposes
        sys32_Preventer = (''.join (drive_Name) + "\Windows\System32")
        windows_Preventer = (''.join (drive_Name) + "\Windows")
        sxs_Preventer = (''.join (drive_Name) + "\Windows\WinSxS")
        program_Preventer = (''.join(drive_Name) + "\Program Files")


        # Checks folderpath length                                                              Just incase you accidentally click on system32 
        if ( len(folderpath) != 0) or (folderpath != "" ) or ((len(folderpath) != 1 )) or (folderpath != sys32_Preventer) or (folderpath != windows_Preventer) or (folderpath != sxs_Preventer) or (folderpath != program_Preventer):
            with open ('second_temp_folder_delete0.bat', 'w') as f:
                f.write ("Echo batch file delete folder\n@RD /S /Q " + "\"" + folderpath + "\"")
                f.close
        # In case the folderpath is too short or invalid, it repeats
        else: 
            folderpath = QFileDialog.getExistingDirectory ()

        # Shows the folderpath in the console
        print ("Temp folderpath here " +folderpath)
        
    # Information dialog for the new user
    def infDial2 ():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This is a one time check!")
        msg.setInformativeText("\nThis will open the temp folder! \n\nCheck if this is the correct folder!")
        msg.setWindowTitle("Temp Folder check")
        msg.setDetailedText("The details are as follows:\n\nThis is the first temp folder and this is checking the directory!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        retval = msg.exec_()
        print ("value of pressed message box button:", retval)

    # Information dialog for the new user
    def infDial ():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Important! This is a one time folder selection")
        msg.setInformativeText("\nPlease open your harddrive (\"example C:\"), the windows folder and then your temp folder")
        msg.setWindowTitle("Folder Setup")
        msg.setDetailedText("The details are as follows:\nGoogle if you are unsure because this will delete the folder!\nSpecify its the temp because this is just cache")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
        retval = msg.exec_()
        print ("value of pressed message box button:", retval)

    # Shows the user their temp folder for only the first use
    def view_Temp ():
        subprocess.call ( [r'temp_opener_cache99.bat'] )

    # Checks if the user is new to the program
    with open ('NewUserCheck.bat', 'r') as f:
        new_to_this = f.read()
        print (new_to_this)
    
    # If statement to check condition and carry out functions for a new user
    if new_to_this == '0':
        # Runs the information dialog and lets the user select their directory for temp 2
        infDial ()
        temp2_directory()
        
        # Checks the first temp folder so the user can check its validity
        infDial2  ()
        view_Temp ()

        # Updates the user to an existing user (remove if you'd like to test)
        with open ('NewUserCheck.bat', 'w') as f:
            f.write ('1')

# The function for clearing the cache
def clearCache1 ():
    cache1_time = time.time ()
    subprocess.call ( [r'cache_cleaner_batch_file.bat'] )
    cache1_time_end = time.time ()
    print ("Cache clear time" + str (cache1_time_end-cache1_time))

# The function for emptying the recycling bin
def clearRec_bin ():
    bin_time = time.time ()
    subprocess.call ( [r'Recycling_bin_cleaner_batchfile_.bat'] )
    bin_end = time.time ()
    print ("\nBin clear time" + str (bin_end-bin_time))

# Function to clear the secondary cache
def clearCache2 ():
    subprocess.call ( [r'second_temp_folder_delete0.bat'] )


# Information dialog available during runtime from info/help button 
def infDial ():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText("This is an application to clear cache and memory.")
   msg.setInformativeText("It clears cache on your PC and some memory too")
   msg.setWindowTitle("Helpful User Info")
   msg.setDetailedText("The details are as follows:\n\nClear cache 2 clears the secondary temp which can be cleared maybe weekly or so.\n The first button clears the cache and recycling bin")
   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	
   retval = msg.exec_()
   print ("value of pressed message box button:", retval)

# Creates and adds the icon to the grid
def iconMaker (location, height, width, row, column):
    image = QPixmap (location)
    logo = QLabel ()
    logo.setPixmap (image)

    logo.setMaximumSize (height, width)
    logo.setStyleSheet (
        "*{border: 15px;" +
        "margin-left: 30px;" +
        "margin: 30px;}"
    )
    # Adds logo widget to the widgets dictionary
    grid.addWidget (logo, row, column)

# Adds github logo to the grid
def gitMaker (location, height, width, row, column):
    image = QPixmap (location)
    logo = QLabel ()
    logo.setPixmap (image)

    # sets the logo's size using the predefined parameters
    logo.setMaximumSize (height, width)
    logo.setStyleSheet (
        "*{border: 15px;" +
        "margin: 30px;}"
    )
    # Adds the widget to the grid
    grid.addWidget (logo, row, column)

# Creates a button that opens my github page (for support)
def gitButt (text, row, column):
    button = QPushButton (text)

    # Sets styling of the button
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';" +
        "background: 'green';" +
        "color: 'red';}"
    )
    # Changes the cursor type on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # Adds the button to the widget dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column)
    
    # Opens github page on click
    button.clicked.connect (urlOpen)


# Used to open creator's github page in a browser
def urlOpen():
    # Link to my github
    urlLink = "https://github.com/Hoccyy"
    wb.open (urlLink)

# Exit button to close the application easier
def exitButt (text, row, column):
    button = QPushButton (text)
    # Styling of the exit button
    button.setStyleSheet (
        "*{ background: '#091433' ;" +
        "font-size: 35px;" +
        "border: 4px solid 'black';" +
        "border-radius: 25px;" +
        "color: 'white';}" +
        "*:hover{background: '#0B1A3F';" +
        "background: 'green';" +
        "color: 'red';}"
    )
    # Changes the cursor type on hover
    button.setCursor (QCursor(QtCore.Qt.PointingHandCursor))
    # Adds the button widget to the widget dictionary
    widgets["Buttons"].append (button)
    #                                        R     C
    grid.addWidget (widgets["Buttons"][-1], row, column)
    # Closes the application when clicked
    button.clicked.connect (window.close)

# Edit to your suited dimensions
# Frames                 w     h
def frame0 ():
    # Creates the frame with the main window class
    frame = mainWindow (1000, 700, "Cache Whoosh", "*{background: '#091433';}", QtGui.QIcon ("cleaner.ico"))
    # Creates a label to give the user information
    label_maker ("Clear the cache, or empty your recycling bin!\n\nThis can help lag or increase storage", 0, 2)

    # Adds operational buttons to the frame to clear cache and recycling bin
    cacheCLearButton ("Clear Cache", 0, 0)
    binCLearButton ("Recycling bin", 1, 0)
    cache2CLearButton ("Clear Cache 2", 2, 0)


    # Adds the information button to the screen
    InfoButt("Info/help", 3, 0)

    # Images                 hight width R C

    # Adds the logo to the screen
    iconMaker ("cleaner.ico", 370, 300, 0, 1)
    # Adds a Github logo to the screen
    gitMaker ("gitlogo.png", 360, 360, 2, 2)

    # Adds Github button and exit button, respectively
    gitButt ("Support me", 3, 2)
    exitButt ("Exit", 4,2)


# Runtime code that displays the first frame
frame0()

# Displays the window
window.show()

# Checks entire time to run
end = time.time()
print ("\nEntire run time :" + str(end-start))
# Ends the application
sys.exit (app.exec())
