import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import camperDatabase
import activityDatabase


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Camp Schedular'
        self.left = 250
        self.top = 100
        self.width = 1000
        self.height = 700
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.headerFont = QFont()
        self.headerFont.setPixelSize(28)
        self.headerFont.setBold(True)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.addCamperTab = QWidget()
        self.viewCampersTab = QWidget()
        self.addActivityTab = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.addCamperTab,"Add Camper")
        self.tabs.addTab(self.viewCampersTab,"View Campers")
        self.tabs.addTab(self.addActivityTab,"Add Activity")
        
        #ADD CAMPER
        self.addCamperTab.layout = QVBoxLayout(self)
        self.addCamperTab.setLayout(self.addCamperTab.layout)

        #Title
        self.addCamperLabel = QLabel("Add Camper:")
        self.addCamperLabel.setFont(self.headerFont)
        
        #First Name
        self.firstName = QWidget()
        self.firstName.layout = QHBoxLayout(self)
        self.firstName.setLayout(self.firstName.layout)
        self.firstNameLabel = QLabel("First Name:")
        self.firstNameEntryBox = QLineEdit()
        self.firstNameEntryBox.setMaximumWidth(300)
        self.firstName.layout.addWidget(self.firstNameLabel)
        self.firstName.layout.addWidget(self.firstNameEntryBox)

        #Last Name
        self.lastName = QWidget()
        self.lastName.layout = QHBoxLayout(self)
        self.lastName.setLayout(self.lastName.layout)
        self.lastNameLabel = QLabel("Last Name:")
        self.lastNameEntryBox = QLineEdit()
        self.lastNameEntryBox.setMaximumWidth(300)
        self.lastName.layout.addWidget(self.lastNameLabel)        
        self.lastName.layout.addWidget(self.lastNameEntryBox)

        #Level
        self.level = QWidget()
        self.level.layout = QHBoxLayout(self)
        self.level.setLayout(self.level.layout)
        self.levelLabel = QLabel("Level:")
        self.levelEntryBox = QComboBox()
        self.levelEntryBox.addItems(["Beginner","Intermediate","Advanced"])
        self.levelEntryBox.setMaximumWidth(300)
        self.level.layout.addWidget(self.levelLabel)  
        self.level.layout.addWidget(self.levelEntryBox)

        #Submit Button
        self.addCamperButton = QPushButton("Submit")
        self.addCamperButton.clicked.connect(self.addCamperFunction)

        #Add Camper Widgets
        self.addCamperTab.layout.addWidget(self.addCamperLabel)
        self.addCamperTab.layout.addStretch()
        self.addCamperTab.layout.addWidget(self.firstName)
        self.addCamperTab.layout.addStretch()
        self.addCamperTab.layout.addWidget(self.lastName)
        self.addCamperTab.layout.addStretch()
        self.addCamperTab.layout.addWidget(self.level)
        self.addCamperTab.layout.addStretch()
        self.addCamperTab.layout.addWidget(self.addCamperButton)



        #*********************************************************
        
        
        #VIEW CAMPERS
        self.viewCampersTab.layout = QVBoxLayout(self)
        self.viewCampersTab.setLayout(self.viewCampersTab.layout)

        #Title
        self.viewCampersTitle = QLabel("View Campers")
        self.viewCampersTitle.setFont(self.headerFont)

        #Table + Data

        #First Name
        self.viewCampersFirstName = QWidget()
        self.viewCampersFirstName.layout = QHBoxLayout(self)
        self.viewCampersFirstName.setLayout(self.viewCampersFirstName.layout)
        self.viewCampersFirstNameSearchBoxLabel = QLabel("First Name:")
        self.viewCampersFirstNameSearchBox = QLineEdit()
        self.viewCampersFirstNameSearchBox.setMaximumWidth(300)
        self.viewCampersFirstName.layout.addWidget(self.viewCampersFirstNameSearchBoxLabel)
        self.viewCampersFirstName.layout.addWidget(self.viewCampersFirstNameSearchBox)

        #Last Name
        self.viewCampersLastName = QWidget()
        self.viewCampersLastName.layout = QHBoxLayout(self)
        self.viewCampersLastName.setLayout(self.viewCampersLastName.layout)
        self.viewCampersLastNameSearchBoxLabel = QLabel("Last Name:")
        self.viewCampersLastNameSearchBox = QLineEdit()
        self.viewCampersLastNameSearchBox.setMaximumWidth(300)
        self.viewCampersLastName.layout.addWidget(self.viewCampersLastNameSearchBoxLabel)
        self.viewCampersLastName.layout.addWidget(self.viewCampersLastNameSearchBox)

        #Level
        self.viewCampersLevel = QWidget()
        self.viewCampersLevel.layout = QHBoxLayout(self)
        self.viewCampersLevel.setLayout(self.viewCampersLevel.layout)
        self.viewCampersLevelLabel = QLabel("Level:")
        self.viewCampersLevelEntryBox = QComboBox()
        self.viewCampersLevelEntryBox.addItems(["Any","Beginner","Intermediate","Advanced"])
        self.viewCampersLevelEntryBox.setMaximumWidth(300)
        self.viewCampersLevel.layout.addWidget(self.viewCampersLevelLabel)  
        self.viewCampersLevel.layout.addWidget(self.viewCampersLevelEntryBox)

        self.table = QTableWidget()

        #View Campers Widgets
        self.viewCampersTab.layout.addWidget(self.viewCampersTitle)
        self.viewCampersTab.layout.addWidget(self.viewCampersFirstName)
        self.viewCampersTab.layout.addWidget(self.viewCampersLastName)
        self.viewCampersTab.layout.addWidget(self.viewCampersLevel)
        self.viewCampersFirstNameSearchBox.textChanged.connect(self.updateCamperData)
        self.viewCampersLastNameSearchBox.textChanged.connect(self.updateCamperData)
        self.viewCampersLevelEntryBox.currentTextChanged.connect(self.updateCamperData)

        self.updateCamperData()


        #*******************************************************

        #ADD ACTIVITY
        self.addActivityTab.layout = QVBoxLayout(self)
        self.addActivityTab.setLayout(self.addActivityTab.layout)

        #Title
        self.addActivityLabel = QLabel("Add Activity:")
        self.addActivityLabel.setFont(self.headerFont)
        
        #Activity Name
        self.addActivityName = QWidget()
        self.addActivityName.layout = QHBoxLayout(self)
        self.addActivityName.setLayout(self.addActivityName.layout)
        self.addActivityNameLabel = QLabel("Activity Name:")
        self.addActivityNameEntryBox = QLineEdit()
        self.addActivityNameEntryBox.setMaximumWidth(300)
        self.addActivityName.layout.addWidget(self.addActivityNameLabel)
        self.addActivityName.layout.addWidget(self.addActivityNameEntryBox)

        #Activity Size
        self.activitySize = QWidget()
        self.activitySize.layout = QHBoxLayout(self)
        self.activitySize.setLayout(self.activitySize.layout)
        self.activitySizeLabel = QLabel("Size:")
        self.activitySizeEntryBox = QLineEdit()
        self.activitySizeEntryBox.setMaximumWidth(300)
        self.activitySize.layout.addWidget(self.activitySizeLabel)        
        self.activitySize.layout.addWidget(self.activitySizeEntryBox)

        #Level
        self.level = QWidget()
        self.level.layout = QHBoxLayout(self)
        self.level.setLayout(self.level.layout)
        self.levelLabel = QLabel("Level:")
        self.levelEntryBox = QComboBox()
        self.levelEntryBox.addItems(["Beginner","Intermediate","Advanced"])
        self.levelEntryBox.setMaximumWidth(300)
        self.level.layout.addWidget(self.levelLabel)  
        self.level.layout.addWidget(self.levelEntryBox)

        #Submit Button
        self.addActivityButton = QPushButton("Submit")
        self.addActivityButton.clicked.connect(self.addActivityFunction)

        #Add Camper Widgets
        self.addActivityTab.layout.addWidget(self.addActivityLabel)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityName)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.activitySize)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityButton)





        #*******************************************************


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        


    #FUNCTIONS

    def addCamperFunction(self):
        camperDatabase.addCamper(self.firstNameEntryBox.text(),self.lastNameEntryBox.text(),self.levelEntryBox.currentText())
        self.updateCamperData()
    
    def addActivityFunction(self):
        activityDatabase.addActivity(self.addActivityNameEntryBox.text(),self.activitySizeEntryBox.text(),"Any","Monday","3:30","5:00")
        self.updateCamperData()
  
    def updateCamperData(self):
        self.viewCampersTab.layout.removeWidget(self.table)
        self.table.deleteLater()
        self.table = QTableWidget()
        self.data = camperDatabase.searchCampersByName(self.viewCampersFirstNameSearchBox.text(),self.viewCampersLastNameSearchBox.text(),self.viewCampersLevelEntryBox.currentText())
        if self.data:
            self.table.setRowCount(len(self.data))
            self.table.setColumnCount(len(self.data[0]))
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.table.setItem(i,j,QTableWidgetItem(self.data[i][j]))
        self.viewCampersTab.layout.addWidget(self.table)

        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())