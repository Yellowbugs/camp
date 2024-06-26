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
        self.title = 'Camp Scheduler'
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
        self.viewActivitiesTab = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.addCamperTab,"Add Camper")
        self.tabs.addTab(self.viewCampersTab,"View Campers")
        self.tabs.addTab(self.addActivityTab,"Add Activity")
        self.tabs.addTab(self.viewActivitiesTab, "View Activities")
        
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

        #Levels
        self.addActivityLevels = QWidget()
        self.addActivityLevels.layout = QHBoxLayout(self)
        self.addActivityLevels.setLayout(self.addActivityLevels.layout)
        self.levelLabel = QLabel("Levels:")
        self.levelCheckBoxBeginnerLabel = QLabel("Beginner:")
        self.levelCheckBoxBeginner = QCheckBox()
        self.levelCheckBoxIntermediateLabel = QLabel("Intermediate:")      
        self.levelCheckBoxIntermediate = QCheckBox()
        self.levelCheckBoxAdvancedLabel = QLabel("Advanced:")              
        self.levelCheckBoxAdvanced = QCheckBox()
        self.addActivityLevels.layout.addWidget(self.levelLabel)  
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxBeginnerLabel)
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxBeginner)
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxIntermediateLabel)
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxIntermediate)
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxAdvancedLabel)
        self.addActivityLevels.layout.addWidget(self.levelCheckBoxAdvanced)

        #Days
        self.addActivityDays= QWidget()
        self.addActivityDays.layout = QHBoxLayout(self)
        self.addActivityDays.setLayout(self.addActivityDays.layout)
        self.daysLabel = QLabel("Days:")
        self.daysCheckBoxMondayLabel = QLabel("Monday:")
        self.daysCheckBoxMonday= QCheckBox()
        self.daysCheckBoxTuesdayLabel = QLabel("Tuesday:")      
        self.daysCheckBoxTuesday = QCheckBox()
        self.daysCheckBoxWednesdayLabel = QLabel("Wednesday:")              
        self.daysCheckBoxWednesday = QCheckBox()
        self.daysCheckBoxThursdayLabel = QLabel("Thursday:")              
        self.daysCheckBoxThursday = QCheckBox()
        self.daysCheckBoxFridayLabel = QLabel("Friday:")              
        self.daysCheckBoxFriday = QCheckBox()
        self.addActivityDays.layout.addWidget(self.daysLabel)  
        self.addActivityDays.layout.addWidget(self.daysCheckBoxMondayLabel)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxMonday)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxTuesdayLabel)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxTuesday)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxWednesdayLabel)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxWednesday)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxThursdayLabel)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxThursday)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxFridayLabel)
        self.addActivityDays.layout.addWidget(self.daysCheckBoxFriday)

        #Start Time
        self.addActivityStartTime = QWidget()
        self.addActivityStartTime.layout = QHBoxLayout(self)
        self.addActivityStartTime.setLayout(self.addActivityStartTime.layout)
        self.addActivityStartTimeLabel = QLabel("Start Time:")
        self.addActivityStartTimeSelector = QTimeEdit()
        self.addActivityStartTime.layout.addWidget(self.addActivityStartTimeLabel)
        self.addActivityStartTime.layout.addWidget(self.addActivityStartTimeSelector)

        #End Time
        self.addActivityEndTime = QWidget()
        self.addActivityEndTime.layout = QHBoxLayout(self)
        self.addActivityEndTime.setLayout(self.addActivityEndTime.layout)
        self.addActivityEndTimeLabel = QLabel("End Time:")
        self.addActivityEndTimeSelector = QTimeEdit()
        self.addActivityEndTime.layout.addWidget(self.addActivityEndTimeLabel)
        self.addActivityEndTime.layout.addWidget(self.addActivityEndTimeSelector)


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
        self.addActivityTab.layout.addWidget(self.addActivityLevels)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityDays)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityStartTime)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityEndTime)
        self.addActivityTab.layout.addStretch()
        self.addActivityTab.layout.addWidget(self.addActivityButton)
       

        #*******************************************************

        #VIEW ACTIVITEIS
        self.viewActivitiesTab.layout = QVBoxLayout(self)
        self.viewActivitiesTab.setLayout(self.viewActivitiesTab.layout)

        #Title
        self.viewActivitiesTitle = QLabel("View Activities")
        self.viewActivitiesTitle.setFont(self.headerFont)

        self.activityTable = QTableWidget()

        #Activity Name
        self.viewActivityName = QWidget()
        self.viewActivityName.layout = QHBoxLayout(self)
        self.viewActivityName.setLayout(self.viewActivityName.layout)
        self.viewActivityNameLabel = QLabel("Activity Name:")
        self.viewActivityNameEntryBox = QLineEdit()
        self.viewActivityNameEntryBox.setMaximumWidth(300)
        self.viewActivityName.layout.addWidget(self.viewActivityNameLabel)
        self.viewActivityName.layout.addWidget(self.viewActivityNameEntryBox)

        #Available
        self.viewActivityAvailability = QWidget()
        self.viewActivityAvailability.layout = QHBoxLayout(self)
        self.viewActivityAvailability.setLayout(self.viewActivityAvailability.layout)
        self.viewActivityAvailabilityLabel = QLabel("Available?")
        self.viewActivityAvailabilityCheckBox = QCheckBox()
        self.viewActivityAvailability.layout.addWidget(self.viewActivityAvailabilityLabel)
        self.viewActivityAvailability.layout.addWidget(self.viewActivityAvailabilityCheckBox)

        #Levels
        self.viewActivityLevels = QWidget()
        self.viewActivityLevels.layout = QHBoxLayout(self)
        self.viewActivityLevels.setLayout(self.viewActivityLevels.layout)
        self.viewLevelsLabel = QLabel("Levels:")
        self.viewLevelsCheckBoxBeginnerLabel = QLabel("Beginner:")
        self.viewLevelsCheckBoxBeginner = QCheckBox()
        self.viewLevelsCheckBoxBeginner.setChecked(True)
        self.viewLevelsCheckBoxIntermediateLabel = QLabel("Intermediate:")      
        self.viewLevelsCheckBoxIntermediate = QCheckBox()
        self.viewLevelsCheckBoxIntermediate.setChecked(True)
        self.viewLevelsCheckBoxAdvancedLabel = QLabel("Advanced:")              
        self.viewLevelsCheckBoxAdvanced = QCheckBox()
        self.viewLevelsCheckBoxAdvanced.setChecked(True)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsLabel)  
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxBeginnerLabel)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxBeginner)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxIntermediateLabel)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxIntermediate)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxAdvancedLabel)
        self.viewActivityLevels.layout.addWidget(self.viewLevelsCheckBoxAdvanced)

        #Days
        self.viewActivityDays= QWidget()
        self.viewActivityDays.layout = QHBoxLayout(self)
        self.viewActivityDays.setLayout(self.viewActivityDays.layout)
        self.viewDaysLabel = QLabel("Days:")
        self.viewDaysCheckBoxMondayLabel = QLabel("Monday:")
        self.viewDaysCheckBoxMonday = QCheckBox()
        self.viewDaysCheckBoxMonday.setChecked(True)
        self.viewDaysCheckBoxTuesdayLabel = QLabel("Tuesday:")      
        self.viewDaysCheckBoxTuesday = QCheckBox()
        self.viewDaysCheckBoxTuesday.setChecked(True)
        self.viewDaysCheckBoxWednesdayLabel = QLabel("Wednesday:")              
        self.viewDaysCheckBoxWednesday = QCheckBox()
        self.viewDaysCheckBoxWednesday.setChecked(True)
        self.viewDaysCheckBoxThursdayLabel = QLabel("Thursday:")              
        self.viewDaysCheckBoxThursday = QCheckBox()
        self.viewDaysCheckBoxThursday.setChecked(True)
        self.viewDaysCheckBoxFridayLabel = QLabel("Friday:")              
        self.viewDaysCheckBoxFriday = QCheckBox()
        self.viewDaysCheckBoxFriday.setChecked(True)
        self.viewActivityDays.layout.addWidget(self.viewDaysLabel)  
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxMondayLabel)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxMonday)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxTuesdayLabel)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxTuesday)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxWednesdayLabel)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxWednesday)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxThursdayLabel)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxThursday)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxFridayLabel)
        self.viewActivityDays.layout.addWidget(self.viewDaysCheckBoxFriday)

        #View Activities Widgets
        self.viewActivitiesTab.layout.addWidget(self.viewActivitiesTitle)
        self.viewActivitiesTab.layout.addWidget(self.viewActivityName)
        self.viewActivitiesTab.layout.addWidget(self.viewActivityAvailability)
        self.viewActivitiesTab.layout.addWidget(self.viewActivityLevels)
        self.viewActivitiesTab.layout.addWidget(self.viewActivityDays)
        self.viewActivityNameEntryBox.textChanged.connect(self.updateActivityData)
        self.viewActivityAvailabilityCheckBox.stateChanged.connect(self.updateActivityData)
        self.viewLevelsCheckBoxBeginner.stateChanged.connect(self.updateActivityData)
        self.viewLevelsCheckBoxIntermediate.stateChanged.connect(self.updateActivityData)
        self.viewLevelsCheckBoxAdvanced.stateChanged.connect(self.updateActivityData)        
        self.viewDaysCheckBoxMonday.stateChanged.connect(self.updateActivityData)
        self.viewDaysCheckBoxTuesday.stateChanged.connect(self.updateActivityData)
        self.viewDaysCheckBoxWednesday.stateChanged.connect(self.updateActivityData)
        self.viewDaysCheckBoxThursday.stateChanged.connect(self.updateActivityData)
        self.viewDaysCheckBoxFriday.stateChanged.connect(self.updateActivityData)
        self.updateActivityData()


        #*******************************************************


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        


    #FUNCTIONS

    def addCamperFunction(self):
        camperDatabase.addCamper(self.firstNameEntryBox.text(),self.lastNameEntryBox.text(),self.levelEntryBox.currentText())
        self.updateCamperData()
    
    def addActivityFunction(self):
        levels = ""
        if self.levelCheckBoxBeginner.isChecked():
            levels += "Beginner,"
        if self.levelCheckBoxIntermediate.isChecked():
            levels += "Intermediate,"
        if self.levelCheckBoxAdvanced.isChecked():
            levels += "Advanced,"
        levels = levels.rstrip(",")

        days = ""
        if self.daysCheckBoxMonday.isChecked():
            days += "Monday,"
        if self.daysCheckBoxTuesday.isChecked():
            days += "Tuesday,"
        if self.daysCheckBoxWednesday.isChecked():
            days += "Wednesday,"
        if self.daysCheckBoxThursday.isChecked():
            days += "Thursday,"
        if self.daysCheckBoxFriday.isChecked():
            days += "Friday," 
        days = days.rstrip(",")
        
        activityDatabase.addActivity(self.addActivityNameEntryBox.text(),self.activitySizeEntryBox.text(),levels,days,self.addActivityStartTimeSelector.text(),self.addActivityEndTimeSelector.text())

        self.updateActivityData()


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
                item = QTableWidgetItem(self.data[i][j])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.table.setItem(i,j,item)        
        self.table.setHorizontalHeaderLabels(["First Name", "Last Name", "Level"])
        self.viewCampersTab.layout.addWidget(self.table)

    def updateActivityData(self):
        self.viewActivitiesTab.layout.removeWidget(self.activityTable)
        self.activityTable.deleteLater()
        self.activityTable = QTableWidget()
        levels = ["****","****","****"]
        if self.viewLevelsCheckBoxBeginner.isChecked():
            levels[0] = "Beginner"
        if self.viewLevelsCheckBoxIntermediate.isChecked():
            levels[1] = "Intermediate"
        if self.viewLevelsCheckBoxAdvanced.isChecked():
            levels[2] = "Advanced"

        days = ["****","****","****","****","****"]
        if self.viewDaysCheckBoxMonday.isChecked():
            days[0] = "Monday"
        if self.viewDaysCheckBoxTuesday.isChecked():
            days[1] = "Tuesday"
        if self.viewDaysCheckBoxWednesday.isChecked():
            days[2] = "Wednesday"
        if self.viewDaysCheckBoxThursday.isChecked():
            days[3] = "Thursday"
        if self.viewDaysCheckBoxFriday.isChecked():
            days[4] = "Friday"
        
        self.data = activityDatabase.searchActivity(self.viewActivityNameEntryBox.text(),self.viewActivityAvailabilityCheckBox.isChecked(),levels,days)
        if self.data:
            self.activityTable.setRowCount(len(self.data))
            self.activityTable.setColumnCount(len(self.data[0]))
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] is not str:
                    item = QTableWidgetItem(str(self.data[i][j]))
                else:
                    item = QTableWidgetItem(self.data[i][j])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.activityTable.setItem(i,j,item)
        self.activityTable.setHorizontalHeaderLabels(["Name", "Size", "Spots Left", "Levels", "Days", "Start  Time", "End Time"])
        self.activityTable.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeMode.ResizeToContents)
        self.activityTable.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeMode.ResizeToContents)
        self.viewActivitiesTab.layout.addWidget(self.activityTable)

        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())