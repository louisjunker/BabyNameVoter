# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget
import sqlite3
import pandas as pd
import numpy as np
import sys


# Importing Data
#df_name1 = pd.read_excel("data/beggedele.xlsx")
#df_name2 = pd.read_excel("data/drengenavne.xlsx")
#df_name3 = pd.read_excel("data/pigenavne.xlsx")
#df_name = pd.concat([df_name1, df_name2, df_name3], ignore_index=True)
#df_name.replace({'Ja': 1, 'Nej': 0}, inplace=True)
#df_name = df_name.rename(columns={'Navn' : 'Name', 'Drengenavn' : 'Male', 'Pigenavn':'Female'})
#df_name.to_csv('data/Names_officialVersion.csv') #Be careful changing this!!!

# Setting up global gender choice.
boy = 1
girl = 1
user_name = ""
name = ""
votes = pd.DataFrame()
names_df = pd.DataFrame()
names_df_voted = pd.DataFrame()
names_df_notvoted = pd.DataFrame()
path = "data/Names_officialVersion.csv"

# Creating SQL database or connecting to it
conn = sqlite3.connect("db/data.db")
# Creating cursor for database
c = conn.cursor()
# Create a tables
c.execute("""CREATE TABLE if not exists users(username text)""")
c.execute("""CREATE TABLE if not exists names(Name text, Male integer, Female integer)""")
c.execute("""CREATE TABLE if not exists votes(Name text, Username text, Vote integer)""")

# Commit changes
conn.commit()
# Close Database 
conn.close()





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 720, 410))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")


#### PAGE: 0 Main 
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
    # Header_title
        self.header_title = QtWidgets.QLabel(self.page_login)
        self.header_title.setGeometry(QtCore.QRect(40, 10, 631, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setItalic(False)
        font.setUnderline(False)
        self.header_title.setFont(font)
        self.header_title.setLineWidth(2)
        self.header_title.setAlignment(QtCore.Qt.AlignCenter)
        self.header_title.setObjectName("header_title")
    # Write initials label
        self.write_initials = QtWidgets.QLabel(self.page_login)
        self.write_initials.setGeometry(QtCore.QRect(150, 100, 420, 120))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        font.setUnderline(False)
        self.write_initials.setFont(font)
        self.write_initials.setLineWidth(2)
        self.write_initials.setAlignment(QtCore.Qt.AlignCenter)
        self.write_initials.setObjectName("write_initials")
    # Box for inputing intials
        self.initials = QtWidgets.QLineEdit(self.page_login)
        self.initials.setGeometry(QtCore.QRect(230, 180, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        font.setUnderline(False)
        self.initials.setFont(font)
        self.initials.setInputMask("")
        self.initials.setText("")
        self.initials.setAlignment(QtCore.Qt.AlignCenter)
        self.initials.setObjectName("initials")
        regex=QtCore.QRegExp("[a-z-A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)
        self.initials.setValidator(validator)
    # Button for saving username
        self.button_login = QtWidgets.QPushButton(self.page_login)
        self.button_login.setGeometry(QtCore.QRect(290, 280, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        font.setUnderline(False)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.stackedWidget.addWidget(self.page_login)
        self.button_login.clicked.connect(self.login)

#### PAGE: 1 Menu
        self.page_menu = QtWidgets.QWidget()
        self.page_menu.setObjectName("page_menu")
        self.label_menu = QtWidgets.QLabel(self.page_menu)
        self.label_menu.setGeometry(QtCore.QRect(150, 40, 420, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_menu.setFont(font)
        self.label_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu.setObjectName("label_menu")
    # Button for choosing vote
        self.button_choosevote = QtWidgets.QPushButton(self.page_menu)
        self.button_choosevote.setGeometry(QtCore.QRect(250, 140, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        font.setUnderline(False)
        self.button_choosevote.setFont(font)
        self.button_choosevote.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Denmark))
        self.button_choosevote.setObjectName("button_choosevote")
        self.button_choosevote.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    # Button for choosing search
        self.button_choosesearch = QtWidgets.QPushButton(self.page_menu)
        self.button_choosesearch.setGeometry(QtCore.QRect(250, 230, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        font.setUnderline(False)
        self.button_choosesearch.setFont(font)
        self.button_choosesearch.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Denmark))
        self.button_choosesearch.setObjectName("button_choosesearch")
        self.stackedWidget.addWidget(self.page_menu)
        self.button_choosesearch.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))


#### PAGE: 2 Search
        self.page_search = QtWidgets.QWidget()
        self.page_search.setObjectName("page_search")
        self.label_search = QtWidgets.QLabel(self.page_search)
        self.label_search.setGeometry(QtCore.QRect(0, 60, 720, 40))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_search.setFont(font)
        self.label_search.setAlignment(QtCore.Qt.AlignCenter)
        self.label_search.setObjectName("label_search")
        self.search_name = QtWidgets.QLineEdit(self.page_search)
        self.search_name.setGeometry(QtCore.QRect(200, 170, 320, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(False)
        font.setUnderline(False)
        self.search_name.setFont(font)
        self.search_name.setAlignment(QtCore.Qt.AlignCenter)
        self.search_name.setObjectName("search_name")
        self.button_search = QtWidgets.QPushButton(self.page_search)
        self.button_search.setGeometry(QtCore.QRect(300, 270, 120, 40))
        self.button_search.setStyleSheet("background-color:#e5ea93;\n"
"color:black")
        self.button_search.setObjectName("button_search")
        self.button_search.clicked.connect(self.clicked_search)
        self.stackedWidget.addWidget(self.page_search)


#### PAGE: 3 Gender
        self.page_gender = QtWidgets.QWidget()
        self.page_gender.setObjectName("page_gender")
        self.label_whatgender = QtWidgets.QLabel(self.page_gender)
        self.label_whatgender.setGeometry(QtCore.QRect(125, 70, 470, 45))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_whatgender.setFont(font)
        self.label_whatgender.setObjectName("label_whatgender")
    # Button for boy
        self.button_boy = QtWidgets.QPushButton(self.page_gender)
        self.button_boy.setGeometry(QtCore.QRect(250, 150, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.button_boy.setFont(font)
        self.button_boy.setStyleSheet("background-color:#99c8ec;\n"
"color:black")
        self.button_boy.setObjectName("button_boy")
        self.button_boy.clicked.connect(self.clicked_boy)
    # Button for girl
        self.button_girl = QtWidgets.QPushButton(self.page_gender)
        self.button_girl.setGeometry(QtCore.QRect(250, 220, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.button_girl.setFont(font)
        self.button_girl.setStyleSheet("background-color:#f6b8c1;\n"
"color:black")
        self.button_girl.setObjectName("button_girl")
        self.button_girl.clicked.connect(self.clicked_girl)
    # Button for unknown gender
        self.button_unknowngender = QtWidgets.QPushButton(self.page_gender)
        self.button_unknowngender.setGeometry(QtCore.QRect(250, 290, 220, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button_unknowngender.setFont(font)
        self.button_unknowngender.setStyleSheet("background-color:#e1c8ea;\n"
"color:black")
        self.button_unknowngender.setObjectName("button_unknowngender")
        self.stackedWidget.addWidget(self.page_gender)
        self.button_unknowngender.clicked.connect(self.clicked_unknown)

#### PAGE: 4 Vote for Name 
        self.page_votename = QtWidgets.QWidget()
        self.page_votename.setObjectName("page_votename")
    # Label with question
        self.LikeTheName = QtWidgets.QLabel(self.page_votename)
        self.LikeTheName.setGeometry(QtCore.QRect(0, 50, 720, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setItalic(False)
        font.setUnderline(False)
        self.LikeTheName.setFont(font)
        self.LikeTheName.setAlignment(QtCore.Qt.AlignCenter)
        self.LikeTheName.setObjectName("LikeTheName")
    # Label with Name
        self.label_name = QtWidgets.QLabel(self.page_votename)
        self.label_name.setGeometry(QtCore.QRect(0, 140, 720, 60))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
    # Button with Yes
        self.button_yes = QtWidgets.QPushButton(self.page_votename)
        self.button_yes.setGeometry(QtCore.QRect(180, 260, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_yes.setFont(font)
        self.button_yes.setStyleSheet("background-color:#77DD77;\n""color:black")
        self.button_yes.setObjectName("button_yes")
        self.button_yes.clicked.connect(self.clicked_yes)
        self.button_yes.setToolTip('Use "Y" as shortcut') 
    # Button with No
        self.button_no = QtWidgets.QPushButton(self.page_votename)
        self.button_no.setGeometry(QtCore.QRect(420, 260, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_no.setFont(font)
        self.button_no.setStyleSheet("background-color:#ff6961;\n"
"color:black")
        self.button_no.setObjectName("button_no")
        self.button_no.setToolTip('Use "N" as shortcut') 
        self.button_no.clicked.connect(self.clicked_no)
        self.stackedWidget.addWidget(self.page_votename)
        

#### Page: Main window
    # Username
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.username.setObjectName("username")
        self.button_gomenu = QtWidgets.QPushButton(self.centralwidget)
        self.button_gomenu.setGeometry(QtCore.QRect(610, 10, 100, 30))
        self.button_gomenu.clicked.connect(self.clicked_gomenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    # Menubar Button - New Session; Delete old data
        self.actionNewSession = QtWidgets.QAction(MainWindow)
        self.actionNewSession.setObjectName("actionNewSession")
        self.actionNewSession.triggered.connect(self.clicked_delete)
    # Menubar Button - Load new name file
        self.actionLoadName = QtWidgets.QAction(MainWindow)
        self.actionLoadName.setObjectName("actionLoadName")
    # Menubar Button - Log out
        self.actionLog_out = QtWidgets.QAction(MainWindow)
        self.actionLog_out.setObjectName("actionLog_out")
        self.actionLog_out.triggered.connect(self.clicked_logout)

        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
    # Menubar Button - Export Data
        self.actionExportData = QtWidgets.QAction(MainWindow)
        self.actionExportData.setObjectName("actionExportData")
        self.actionExportData.triggered.connect(self.clicked_export)

        self.menuFile.addAction(self.actionNewSession)
        self.menuFile.addAction(self.actionLoadName)
        self.menuFile.addAction(self.actionLog_out)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuExport.addAction(self.actionExportData)
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_title.setText(_translate("MainWindow", "Welcome to the Name Voter"))
        self.write_initials.setText(_translate("MainWindow", "Please enter your initials below:"))
        self.initials.setPlaceholderText(_translate("MainWindow", "Type initials here"))
        self.button_login.setText(_translate("MainWindow", "Log in"))
        # self.button_login.setShortcut(_translate("MainWindow", "Enter"))
        self.label_menu.setText(_translate("MainWindow", "What would you like to do?"))
        self.button_choosevote.setText(_translate("MainWindow", "Vote on Names"))
        self.button_choosesearch.setText(_translate("MainWindow", "Search for a Name"))
        self.label_search.setText(_translate("MainWindow", "Search for a name here:"))
        self.search_name.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.label_whatgender.setText(_translate("MainWindow", "What is the babys gender?"))
        self.button_boy.setText(_translate("MainWindow", "Boy"))
        self.button_girl.setText(_translate("MainWindow", "Girl"))
        self.button_unknowngender.setText(_translate("MainWindow", "Unknown gender"))
        self.LikeTheName.setText(_translate("MainWindow", "Do you like the name: "))
        self.label_name.setText(_translate("MainWindow", "NAME ?"))
        self.button_yes.setText(_translate("MainWindow", "Yes"))
        self.button_yes.setShortcut(_translate("MainWindow", "Y"))
        self.button_no.setText(_translate("MainWindow", "No"))
        self.button_no.setShortcut(_translate("MainWindow", "N"))
        self.username.setText(_translate("MainWindow", "User: "))
        self.button_gomenu.setText(_translate("MainWindow", "Go to Menu"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.actionNewSession.setText(_translate("MainWindow", "Delete all stored votes, and start new session"))
        self.actionNewSession.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionLoadName.setText(_translate("MainWindow", "Load new names - Delete old names"))
        self.actionLog_out.setText(_translate("MainWindow", "Log out"))
        self.actionExportData.setText(_translate("MainWindow", "Export Voting Data"))




    def login(self):
        global user_name
        user_name = self.initials.text().upper()
        # Connecting to SQL database
        conn = sqlite3.connect("db/data.db")
        # Creating cursor for database
        c = conn.cursor()

        # Grabbing usernames
        c.execute("SELECT * FROM users")
        tuples = c.fetchall()
        users = pd.DataFrame(tuples, columns=['username'])
        if (users['username'].eq(user_name)).any():
            self.stackedWidget.setCurrentIndex(1)
            self.username.setText("User: " + user_name)
        else: 
            c.execute("INSERT INTO users VALUES (:user_name)",
                      {
                          'user_name': user_name,
                      })
            self.stackedWidget.setCurrentIndex(1)
            self.username.setText("User: " + user_name)

        # Commit changes AND close database
        conn.commit()
        conn.close()

    def set_name(self):
        global name
        self.label_name.setText(name.capitalize())

    # Saving gender choice
    def clicked_boy(self):
        global boy, girl
        boy = 1
        girl = 0
        self.name_database()
        self.random_name()
        self.stackedWidget.setCurrentIndex(4)
    def clicked_girl(self):
        global boy, girl
        boy = 0
        girl = 1
        self.name_database()
        self.random_name()
        self.stackedWidget.setCurrentIndex(4)
    def clicked_unknown(self):
        global boy, girl
        boy = 1
        girl = 1
        self.name_database()
        self.random_name()
        self.stackedWidget.setCurrentIndex(4)

    # Search for specific name
    def clicked_search(self):
        global name
        # Saving the searched name
        name = self.search_name.text().lower()
        # Going to Voting page 
        self.stackedWidget.setCurrentIndex(4)
        # Ensuring first letter i capitalized
        #self.label_name.setText(name.capitalize())
        self.set_name()
        # Connecting to SQL
        conn = sqlite3.connect("db/data.db")
        # Creating cursor for database
        c = conn.cursor()
        # Grabbing usernames
        c.execute("SELECT * FROM names")
        tuples = c.fetchall()
        df_names = pd.DataFrame(tuples, columns=['Name', 'Male', 'Female'])
        # Generating new dataline for SQL
        name_sql = (name.capitalize(), None, None)
        # Checking if name is missing or not.
        if (df_names['Name'].eq(name)).any():
            print("Exist")
        # Inserting the name into the database if missing
        else:
            sql = """INSERT INTO names (Name, Male, Female) VALUES (?, ?, ?);"""
            c.execute(sql, name_sql)
        # Comminting to database
        conn.commit()
        # Closing Connection
        conn.close()
        self.name_database()


    # Voting YES
    def clicked_yes(self):
        global name
        global user_name
        conn = sqlite3.connect("db/data.db")
        c = conn.cursor()
        votes_df = (name.capitalize(), user_name, +1)
        votes_sql = """INSERT INTO votes (Name, Username, Vote) VALUES (?, ?, ?);"""
        c.execute(votes_sql, votes_df)
        conn.commit()
        conn.close()
        self.random_name()

    # Voting NO
    def clicked_no(self):
        global name
        global user_name
        conn = sqlite3.connect("db/data.db")
        c = conn.cursor()
        votes_df = (name.capitalize(), user_name, -1)
        votes_sql = """INSERT INTO votes (Name, Username, Vote) VALUES (?, ?, ?);"""
        c.execute(votes_sql, votes_df)
        conn.commit()
        conn.close()
        self.random_name()

    # Random Name generater
    def name_database(self):
        global name
        global names_df
        global names_df_voted
        global names_df_notvoted
        #Connecting to database
        conn = sqlite3.connect("db/data.db")
        # Creating cursor for DB
        c = conn.cursor()
        # Extracting data
        c.execute("""SELECT * 
                  FROM names
                  LEFT JOIN votes
                  USING(Name)""")
        tuples = c.fetchall()
        names_df = pd.DataFrame(tuples, columns=['Name', 'Male', 'Female', 'Username', 'Vote'])
        #pd.to_numeric(names_df, errors='coerce').convert_dtypes() 
        #names_df['Male'] = pd.to_numeric(names_df['Male'])
        #names_df[['Male', 'Female']] = names_df[['Male', 'Female']].astype(str).astype(int)
        conn.commit()
        conn.close()
        # Dropping name user already voted for
        names_df = names_df[names_df['Username'] != user_name]
        names_df = names_df.drop(columns=['Username'])
        names_df['Vote'].fillna(0, inplace=True)
        #if (users['username'].eq(user_name)).any():
        names_df = names_df[names_df['Male'].eq(boy) & names_df['Female'].eq(girl)]
        names_df = names_df.groupby('Name')['Vote'].sum().reset_index()
        
        #Dividing data into positive voted and not voted (+ negative voted) Names
        names_df_voted = names_df[names_df['Vote'] > 0]
        names_df_notvoted = names_df[names_df['Vote'] <= 0]
        
    def random_name(self):
        global name
        global names_df
        global names_df_voted
        global names_df_notvoted
        # Choosing name from either voted or not voted dataaset. Always starts with positive voted.
        if len(names_df_voted['Name']) != 0: 
            name = np.random.choice(names_df_voted['Name'])
        else:
            name = np.random.choice(names_df_notvoted['Name'])
        print(name)
        self.set_name()

    # Menubar Button - Log out
    def clicked_logout(self):
        global user_name
        user_name = ""
        self.stackedWidget.setCurrentIndex(0)
        self.username.setText("User: " + user_name)


    # Menubar Button - Delete old Data
    def clicked_delete(self):
        msg_delete = QMessageBox()
        msg_delete.setWindowTitle("WARNING")
        msg_delete.setText("Are you sure you want to delete all user and vote data?")
        msg_delete.setIcon(QMessageBox.Critical)
        msg_delete.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_delete.setDefaultButton(QMessageBox.No)
        msg_delete.buttonClicked.connect(self.delete_button)

        x = msg_delete.exec_()
    def delete_button(self, i): 
        if i.text() == "&Yes":
        #Connecting to Database
            conn = sqlite3.connect("db/data.db")
        # Creating cursor for database
            c = conn.cursor()
        # Deleting all user information
            c.execute("DELETE FROM users;",) 
        # Deleting all votes information
            c.execute("DELETE FROM votes;",) 
        # Commit the changes
            conn.commit()
        # Closing Connection
            conn.close()
            msg_delete_yes = QMessageBox()
            msg_delete_yes.setWindowTitle("Data deleted")
            msg_delete_yes.setText("All data deleted succesfully")
            x = msg_delete_yes.exec_()


    # Menubar Button - Import new Names file 
    def clicked_import(self):#  NOT FINISHED
        path = ""
        conn = sqlite3.connect("db/data.db")
        c = conn.cursor()

        conn.commit()
        conn.close()

    def insert_name(self): # NOT FINISHED
        # Inserting names data to SQL
        #Connecting to database
        conn = sqlite3.connect("db/data.db")
        # Inserting data 
        df_name = pd.read_csv(path, index_col=[0])
        ## READ USER DATA AND APPEND TO THIS DATASET
        # DELETE ALL NAMES; AND ADD ALL AGAIN (NO VOTES LOST)
        #user_path = ""
        #df_name_provided = pd.read_csv(user_path)
        df_name.to_sql('names', conn, if_exists='append', index=False)
        # Commit changes
        conn.commit()
        # Close Database 
        conn.close()

    # Menubar Button - Export voting data
    def clicked_export(self):
        global votes
        # Opening FileDialog for saving file.
        fname, _ = QFileDialog.getSaveFileName(None, "Save", "", "CSV Files (*.csv)")
        #Connecting to database
        conn = sqlite3.connect("db/data.db")
        # Creating cursor for database
        c = conn.cursor()
        # Finding data from database
        c.execute("SELECT * FROM votes")
        # Extracting data
        tuples = c.fetchall()
        # Commiting and closing connection
        conn.commit()
        conn.close()
        # Grabbing usernames
        votes = pd.DataFrame(tuples, columns=['Name', 'Username', 'Vote'])
        #Saving votes to file, based on user choice of path.
        votes.to_csv(fname, index=False)
        msg_saved = QMessageBox()
        msg_saved.setWindowTitle("Data has been saved")
        msg_saved.setText("All data saved succesfully")
        x = msg_saved.exec_()

    # Button - Go back to Menu 
    def clicked_gomenu(self):
        if user_name != "":
            self.stackedWidget.setCurrentIndex(1)
        else:
            msg_login_first = QMessageBox()
            msg_login_first.setWindowTitle("Not logged in")
            msg_login_first.setText("Please login before heading to the menu.")
            x = msg_login_first.exec_()



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

