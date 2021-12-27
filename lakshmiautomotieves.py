import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import os
import PyPDF2
from reportlab.pdfgen.canvas import Canvas
import num2words
import datetime



class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(823, 258)
        LogInWindow.setWindowIcon(QtGui.QIcon("logoicon.ico"))
        self.centralwidget = QtWidgets.QWidget(LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(20, 22, 501, 221))
        self.LogoLabel.setText("")
        self.LogoLabel.setPixmap(QtGui.QPixmap("logonobg.png"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoLabel.setObjectName("LogoLabel")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(540, 30, 91, 41))
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(540, 80, 91, 41))
        self.passwordLabel.setObjectName("passwordLabel")
        self.userInput = QtWidgets.QComboBox(self.centralwidget)
        self.userInput.setGeometry(QtCore.QRect(660, 35, 141, 32))
        self.userInput.setObjectName("userInput")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(670, 90, 121, 21))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(610, 140, 112, 32))
        self.enterButton.setObjectName("enterButton")
        self.msgLabel = QtWidgets.QLabel(self.centralwidget)
        self.msgLabel.setGeometry(QtCore.QRect(540, 190, 251, 20))
        self.msgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgLabel.setObjectName("msgLabel")
        LogInWindow.setCentralWidget(self.centralwidget)

        self.LogInDetails=pd.read_csv("Login.csv")
        for Users in self.LogInDetails["User"]:
            self.userInput.addItem(Users)
        
        self.enterButton.clicked.connect(self.enterButtonPressed)

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "LogInWindow"))
        self.userLabel.setText(_translate("LogInWindow", "User"))
        self.passwordLabel.setText(_translate("LogInWindow", "Password"))
        self.enterButton.setText(_translate("LogInWindow", "Enter"))
        self.msgLabel.setText(_translate("MainWindow", "Select User and Enter Password"))

    def enterButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedUserIndex=self.userInput.currentIndex()
        self.enteredPassword = self.passwordInput.text()
        if(self.enteredPassword == str(self.LogInDetails['Password'][self.selectedUserIndex])):
            self.msgLabel.setText(_translate("MainWindow", "Logigng In"))
            LogInWindow.close()
            AddWindow.show()
        else:
            self.msgLabel.setText(_translate("MainWindow", "Password correct ah podra Pu***!!!"))

class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(1146, 609)
        AddWindow.setWindowIcon(QtGui.QIcon("logoicon.ico"))
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(470, 30, 281, 131))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("logonobg.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(40, 209, 41, 16))
        self.typeLabel.setObjectName("typeLabel")
        self.typeInput = QtWidgets.QComboBox(self.centralwidget)
        self.typeInput.setGeometry(QtCore.QRect(170, 200, 141, 32))
        self.typeInput.setObjectName("typeInput")
        self.itemLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemLabel.setGeometry(QtCore.QRect(150, 250, 41, 16))
        self.itemLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemLabel.setObjectName("itemLabel")
        self.quantityLabel = QtWidgets.QLabel(self.centralwidget)
        self.quantityLabel.setGeometry(QtCore.QRect(41, 336, 58, 16))
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.quantityInput.setGeometry(QtCore.QRect(190, 335, 113, 21))
        self.quantityInput.setObjectName("quantityInput")
        self.unitLabel = QtWidgets.QLabel(self.centralwidget)
        self.unitLabel.setGeometry(QtCore.QRect(38, 380, 31, 16))
        self.unitLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.unitLabel.setObjectName("unitLabel")
        self.unitInput = QtWidgets.QComboBox(self.centralwidget)
        self.unitInput.setGeometry(QtCore.QRect(210, 374, 91, 32))
        self.unitInput.setObjectName("unitInput")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(41, 420, 58, 16))
        self.priceLabel.setObjectName("priceLabel")
        self.priceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.priceInput.setGeometry(QtCore.QRect(180, 420, 113, 21))
        self.priceInput.setObjectName("priceInput")
        self.amountLabel = QtWidgets.QLabel(self.centralwidget)
        self.amountLabel.setGeometry(QtCore.QRect(62, 471, 111, 16))
        self.amountLabel.setObjectName("amountLabel")
        self.amountOutput = QtWidgets.QLabel(self.centralwidget)
        self.amountOutput.setGeometry(QtCore.QRect(170, 470, 81, 20))
        self.amountOutput.setText("")
        self.amountOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.amountOutput.setObjectName("amountOutput")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(322, 553, 131, 31))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(448, 553, 221, 32))
        self.editButton.setObjectName("editButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(667, 553, 221, 32))
        self.deleteButton.setObjectName("deleteButton")
        self.proceedButton = QtWidgets.QPushButton(self.centralwidget)
        self.proceedButton.setGeometry(QtCore.QRect(888, 553, 241, 31))
        self.proceedButton.setObjectName("proceedButton")
        self.particularList = QtWidgets.QListWidget(self.centralwidget)
        self.particularList.setGeometry(QtCore.QRect(450, 196, 441, 311))
        self.particularList.setObjectName("particularList")
        self.quantityList = QtWidgets.QListWidget(self.centralwidget)
        self.quantityList.setGeometry(QtCore.QRect(895, 196, 41, 311))
        self.quantityList.setObjectName("quantityList")
        self.unitList = QtWidgets.QListWidget(self.centralwidget)
        self.unitList.setGeometry(QtCore.QRect(940, 196, 61, 311))
        self.unitList.setObjectName("unitList")
        self.priceList = QtWidgets.QListWidget(self.centralwidget)
        self.priceList.setGeometry(QtCore.QRect(1005, 196, 61, 311))
        self.priceList.setObjectName("priceList")
        self.amountList = QtWidgets.QListWidget(self.centralwidget)
        self.amountList.setGeometry(QtCore.QRect(1070, 196, 61, 311))
        self.amountList.setObjectName("amountList")
        self.typeList = QtWidgets.QListWidget(self.centralwidget)
        self.typeList.setGeometry(QtCore.QRect(375, 196, 71, 311))
        self.typeList.setObjectName("typeList")
        self.snoList = QtWidgets.QListWidget(self.centralwidget)
        self.snoList.setGeometry(QtCore.QRect(330, 196, 41, 311))
        self.snoList.setObjectName("snoList")
        self.quantityDisplay = QtWidgets.QLabel(self.centralwidget)
        self.quantityDisplay.setGeometry(QtCore.QRect(894, 520, 41, 20))
        self.quantityDisplay.setText("")
        self.quantityDisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.quantityDisplay.setObjectName("quantityDisplay")
        self.amountDisplay = QtWidgets.QLabel(self.centralwidget)
        self.amountDisplay.setGeometry(QtCore.QRect(1072, 521, 41, 20))
        self.amountDisplay.setText("")
        self.amountDisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.amountDisplay.setObjectName("amountDisplay")
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(810, 520, 61, 20))
        self.totalLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.snoTitle = QtWidgets.QLabel(self.centralwidget)
        self.snoTitle.setGeometry(QtCore.QRect(334, 170, 31, 20))
        self.snoTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.snoTitle.setObjectName("snoTitle")
        self.typeTitle = QtWidgets.QLabel(self.centralwidget)
        self.typeTitle.setGeometry(QtCore.QRect(374, 170, 71, 20))
        self.typeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.typeTitle.setObjectName("typeTitle")
        self.particularTitle = QtWidgets.QLabel(self.centralwidget)
        self.particularTitle.setGeometry(QtCore.QRect(450, 169, 441, 20))
        self.particularTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.particularTitle.setObjectName("particularTitle")
        self.qtyTiltle = QtWidgets.QLabel(self.centralwidget)
        self.qtyTiltle.setGeometry(QtCore.QRect(890, 170, 51, 20))
        self.qtyTiltle.setAlignment(QtCore.Qt.AlignCenter)
        self.qtyTiltle.setObjectName("qtyTiltle")
        self.unitTitle = QtWidgets.QLabel(self.centralwidget)
        self.unitTitle.setGeometry(QtCore.QRect(940, 170, 61, 20))
        self.unitTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.unitTitle.setObjectName("unitTitle")
        self.priceTitle = QtWidgets.QLabel(self.centralwidget)
        self.priceTitle.setGeometry(QtCore.QRect(1010, 170, 51, 20))
        self.priceTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.priceTitle.setObjectName("priceTitle")
        self.amountTitle = QtWidgets.QLabel(self.centralwidget)
        self.amountTitle.setGeometry(QtCore.QRect(1070, 170, 61, 20))
        self.amountTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.amountTitle.setObjectName("amountTitle")
        self.particularInput = QtWidgets.QLineEdit(self.centralwidget)
        self.particularInput.setGeometry(QtCore.QRect(40, 288, 261, 21))
        self.particularInput.setAlignment(QtCore.Qt.AlignCenter)
        self.particularInput.setObjectName("particularInput")
        self.msgdisplayLabel = QtWidgets.QLabel(self.centralwidget)
        self.msgdisplayLabel.setGeometry(QtCore.QRect(40, 520, 261, 21))
        self.msgdisplayLabel.setText("")
        self.msgdisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgdisplayLabel.setObjectName("msgdisplayLabel")
        AddWindow.setCentralWidget(self.centralwidget)

        self.quantityInput.setText("1")
        self.priceInput.setText("0.0")
        self.amountOutput.setText("0.0")
        self.data=[]
        self.sno=0
        self.types=["SPARE","SERVICE"]
        self.units=["Ltr","ml","Kgs","Grams","Nos"]
        self.total=0

        for i in range(len(self.types)):
            self.typeInput.addItem(self.types[i])
        
        for i in range(len(self.units)):
            self.unitInput.addItem(self.units[i])

        self.selectedTypeIndex=self.typeInput.currentIndex()
        self.enteredParticular=self.particularInput.text()
        self.enteredQuantity=int(self.quantityInput.text())
        self.enteredUnit=str(self.unitInput.currentText())
        self.enteredPrice=float(self.priceInput.text())
        self.calculatedAmount=float(0.0)

        for i in range(len(self.data)):
            self.snoList.addItem(str(self.data[i]['sno']))
            self.typeList.addItem(self.types[self.data[i]['typeindex']])
            self.particularList.addItem(self.data[i]['particular'])
            self.quantityList.addItem(str(self.data[i]['quantity']))
            self.unitList.addItem(str(self.data[i]['unit']))
            self.priceList.addItem(str(self.data[i]['price']))
            self.amountList.addItem(str(self.data[i]['amount']))

        self.snoList.itemSelectionChanged.connect(self.snoSelectionChanged)
        self.typeList.itemSelectionChanged.connect(self.typeSelectionChanged)
        self.particularList.itemSelectionChanged.connect(self.particularSelectionChanged)
        self.quantityList.itemSelectionChanged.connect(self.qtySelectionChanged)
        self.unitList.itemSelectionChanged.connect(self.unitSelectionChanged)
        self.priceList.itemSelectionChanged.connect(self.priceSelectionChanged)
        self.amountList.itemSelectionChanged.connect(self.amountSelectionChanged)        

        self.typeInput.currentIndexChanged.connect(self.typeInputIndexChanged)
        self.priceInput.textChanged.connect(self.priceInputTextChanged)
        self.quantityInput.textChanged.connect(self.priceInputTextChanged)

        self.addButton.clicked.connect(self.addButtonPressed)
        self.editButton.clicked.connect(self.editButtonPressed)
        self.deleteButton.clicked.connect(self.deleteButtonPressed)
        self.proceedButton.clicked.connect(self.proceedButtonPressed)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)
        _translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "AddWindow"))
        self.typeLabel.setText(_translate("AddWindow", "Type"))
        self.itemLabel.setText(_translate("AddWindow", "Item"))
        self.quantityLabel.setText(_translate("AddWindow", "Quantity"))
        self.unitLabel.setText(_translate("AddWindow", "Unit"))
        self.priceLabel.setText(_translate("AddWindow", "Price"))
        self.amountLabel.setText(_translate("AddWindow", "Amount           :"))
        self.addButton.setText(_translate("AddWindow", "Add"))
        self.editButton.setText(_translate("AddWindow", "Edit"))
        self.deleteButton.setText(_translate("AddWindow", "Delete"))
        self.proceedButton.setText(_translate("AddWindow", "Proceed"))
        self.totalLabel.setText(_translate("AddWindow", "Total  : "))
        self.snoTitle.setText(_translate("AddWindow", "S.No"))
        self.typeTitle.setText(_translate("AddWindow", "Type"))
        self.particularTitle.setText(_translate("AddWindow", "Particular"))
        self.qtyTiltle.setText(_translate("AddWindow", "Qty"))
        self.unitTitle.setText(_translate("AddWindow", "Unit"))
        self.priceTitle.setText(_translate("AddWindow", "Price"))
        self.amountTitle.setText(_translate("AddWindow", "Amount"))

    def typeInputIndexChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedTypeIndex=self.typeInput.currentIndex()

    def priceInputTextChanged(self):
        _translate = QtCore.QCoreApplication.translate
        if(self.quantityInput.text()==""):
            self.quantityInput.setText("0")
            self.enteredQuantity=0
        else:
            try:
                self.enteredQuantity=int(self.quantityInput.text())
            except ValueError:
                self.msgdisplayLabel.setText("Enter Valid Quantity")
                self.quantityInput.setText("0")
                self.enteredQuantity=0
        if(self.priceInput.text()==""):
            self.priceInput.setText("0.0")
            self.enteredPrice=0
        else:
            try:
                self.enteredPrice=float(self.priceInput.text())
            except ValueError:
                self.msgdisplayLabel.setText("Enter Valid Price")
                self.priceInput.setText("0.0")
                self.enteredPrice=0.0
        self.calculatedAmount=float(int(self.enteredQuantity)*float(self.enteredPrice))
        self.amountOutput.setText(str(self.calculatedAmount))

    def snoSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.snoList.currentRow()
        self.setSelectionInAllList()

    def typeSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.typeList.currentRow()
        self.setSelectionInAllList()

    def particularSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.particularList.currentRow()
        self.setSelectionInAllList()

    def qtySelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.quantityList.currentRow()
        self.setSelectionInAllList()

    def unitSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.unitList.currentRow()
        self.setSelectionInAllList()

    def priceSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.priceList.currentRow()
        self.setSelectionInAllList()

    def amountSelectionChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.selectedRow=self.amountList.currentRow()
        self.setSelectionInAllList()

    def setSelectionInAllList(self):
        _translate = QtCore.QCoreApplication.translate
        self.snoList.setCurrentRow(self.selectedRow)
        self.typeList.setCurrentRow(self.selectedRow)
        self.particularList.setCurrentRow(self.selectedRow)
        self.quantityList.setCurrentRow(self.selectedRow)
        self.unitList.setCurrentRow(self.selectedRow)
        self.priceList.setCurrentRow(self.selectedRow)
        self.amountList.setCurrentRow(self.selectedRow)

    def clearLists(self):
        self.snoList.clear()
        self.typeList.clear()
        self.particularList.clear()
        self.quantityList.clear()
        self.unitList.clear()
        self.priceList.clear()
        self.amountList.clear()
    
    def updateLists(self):
        self.clearLists()
        for i in range(len(self.data)):
            self.snoList.addItem(str(i+1))
            self.typeList.addItem(self.types[self.data[i]['typeindex']])
            self.particularList.addItem(self.data[i]['particular'])
            self.quantityList.addItem(str(self.data[i]['quantity']))
            self.unitList.addItem(str(self.data[i]['unit']))
            self.priceList.addItem(str(self.data[i]['price']))
            self.amountList.addItem(str(self.data[i]['amount']))
    
    def updateInputVariables(self):
        self.enteredParticular=self.particularInput.text()
        self.enteredQuantity=int(self.quantityInput.text())
        self.enteredUnit=str(self.unitInput.currentText())
        self.enteredPrice=float(self.priceInput.text())
        self.calculatedAmount=float(int(self.enteredQuantity)*float(self.enteredPrice))

    def clearInputFields(self):
        self.particularInput.clear()
        self.quantityInput.setText("1")
        self.priceInput.setText("0.0")

    def getTotal(self):
        self.tempTotal=0
        for i in range(len(self.data)):
            self.tempTotal+=self.data[i]['amount']
        return self.tempTotal

    def addButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        self.sno+=1
        if(self.sno<=16):
            self.updateInputVariables()
            self.data.append({
                'sno':self.sno,
                'typeindex':self.selectedTypeIndex,
                'particular':self.enteredParticular,
                'quantity':self.enteredQuantity,
                'unit':self.enteredUnit,
                'price':self.enteredPrice,
                'amount':self.calculatedAmount
            })
            self.updateLists()
            self.clearInputFields()
            self.msgdisplayLabel.setText("")
            self.total=self.getTotal()
            self.amountDisplay.setText(str(self.total))
            self.quantityDisplay.setText(str(self.getQuantityCount()))
        else:
            self.msgdisplayLabel.setText("Maximum numbers reached")

    def deleteSelectedRow(self):
        del self.data[self.selectedRow]

    def editButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        self.typeInput.setCurrentIndex(self.data[self.selectedRow]['typeindex'])
        self.particularInput.setText(self.data[self.selectedRow]['particular'])
        self.quantityInput.setText(str(self.data[self.selectedRow]['quantity']))
        self.unitInput.setCurrentText(self.data[self.selectedRow]['unit'])
        self.priceInput.setText(str(self.data[self.selectedRow]['price']))
        self.deleteSelectedRow()
        self.updateLists()
        self.quantityDisplay.setText(str(self.getQuantityCount()))
        self.total=self.getTotal()
        self.amountDisplay.setText(str(self.total))
    
    def deleteButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        self.deleteSelectedRow()
        self.updateLists()
        self.quantityDisplay.setText(str(self.getQuantityCount()))
        self.total=self.getTotal()
        self.amountDisplay.setText(str(self.total))

    def getQuantityCount(self):
        self.quantityCount=0
        for i in range(len(self.data)):
            self.quantityCount+=self.data[i]['quantity']
        return self.quantityCount

    def createPDF(self):
        # print(self.data)
        self.dataDF = pd.DataFrame(self.data)
        self.dataDFGrouped = self.dataDF.groupby(self.dataDF.typeindex) 
        self.currentyear=datetime.date.today().strftime('%Y')
        self.currentmonth=datetime.date.today().strftime('%b')
        self.currentdate=datetime.date.today().strftime('%d')
        # home = os.curdir
        # if 'HOME' in os.environ:
        #     home = os.environ['HOME']
        # elif os.name == 'posix':
        #     home = os.path.expanduser("~/")
        # elif os.name == 'nt':
        #     if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        #         home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
        # else:
        #     home = os.environ['HOMEPATH']
        # desktop=os.path.join(home,"Desktop")
        cwd=os.getcwd()
        try:
            os.makedirs(os.path.join(cwd,self.currentyear,self.currentmonth,self.currentdate))
        except FileExistsError:
            pass
        outptufilePath=os.path.join(cwd,self.currentyear,self.currentmonth,self.currentdate,
        self.currentyear+self.currentmonth+self.currentdate+ui3.enteredVehicleNumber+".pdf")
        # print(outptufilePath)
        tempcanvas = Canvas(outptufilePath)
        tempcanvas.drawImage("swamy.PNG",20,150)
        tempcanvas.drawImage("logobw.png",80,410)
        tempcanvas.setFont('Helvetica', 16)
        tempcanvas.drawString(40, 800, "SRI LAKSHMI AUTOMOTIVES")
        tempcanvas.setFont('Helvetica', 11)
        tempcanvas.drawString(40, 780, "Dharapuram Road, Kethanur-641671")
        tempcanvas.drawString(40, 760, "Phone - 9095868775 , 7539907270")
        tempcanvas.drawString(40, 740, "Mail - boobalanselva352@gmail.com")
        tempcanvas.drawImage("logo150x70.jpg",410,750)
        # tempcanvas.setFont('Helvetica', 16)
        # tempcanvas.drawString(250, 720, "Tax Invoice")
        tempcanvas.setFont('Helvetica', 11)
        tempcanvas.drawString(40, 700, "Vehicle No")
        tempcanvas.drawString(110, 700, ":")
        tempcanvas.drawString(120, 700, ui3.enteredVehicleNumber)
        tempcanvas.drawString(40, 680, "Owner Name")
        tempcanvas.drawString(110, 680, ":")
        tempcanvas.drawString(120, 680, ui3.enteredCustomerName)
        tempcanvas.drawString(390, 700, "Invoice No")
        tempcanvas.drawString(450, 700, ":")
        tempcanvas.drawString(460,700,ui3.billNumber)
        tempcanvas.drawString(390, 680, "Date")
        tempcanvas.drawString(450, 680, ":")
        tempcanvas.drawString(460,680,ui3.selectedDate)
        tempcanvas.line(40,670,560,670)
        tempcanvas.line(40,669,560,669)
        tempcanvas.setFont('Helvetica', 9)
        tempcanvas.drawString(45, 657, "S.No")
        tempcanvas.drawString(90, 657, "Particular")
        tempcanvas.drawString(380, 657, "Quantity")
        tempcanvas.drawString(430, 657, "Unit")
        tempcanvas.drawString(460, 657, "Price")
        tempcanvas.drawString(510, 657, "Amount")
        tempcanvas.line(40,650,560,650)
        tempcanvas.line(40,649,560,649)
        ypos=650
        try: 
            self.sparesAvailable=True
            self.dataDFGroupedSpare = self.dataDFGrouped.get_group(0)
        except KeyError:
            self.sparesAvailable=False
        finally:
            if(self.sparesAvailable):
                tempcanvas.setFont('Helvetica', 12)
                ypos=ypos-20
                tempcanvas.drawString(260, ypos, "SPARES")
                tempcanvas.setFont('Helvetica', 9)
                for i in range(len(self.dataDFGroupedSpare)):
                    ypos=ypos-20
                    tempcanvas.drawString(45, ypos, str(i+1))
                    tempcanvas.drawString(90, ypos, self.dataDFGroupedSpare.iloc[i]['particular'])
                    tempcanvas.drawString(380, ypos, str(self.dataDFGroupedSpare.iloc[i]['quantity']))
                    tempcanvas.drawString(430, ypos, self.dataDFGroupedSpare.iloc[i]['unit'])
                    tempcanvas.drawString(460, ypos, str(self.dataDFGroupedSpare.iloc[i]['price']))
                    tempcanvas.drawString(510, ypos, str(self.dataDFGroupedSpare.iloc[i]['quantity']*self.dataDFGroupedSpare.iloc[i]['price']))
        try:
            self.ServiceAvailable=True
            self.dataDFGroupedService = self.dataDFGrouped.get_group(1)
        except KeyError:
            self.ServiceAvailable=False
        finally:
            if(self.ServiceAvailable):
                tempcanvas.setFont('Helvetica', 12)
                ypos=ypos-20
                tempcanvas.drawString(260, ypos, "SERVICE")
                tempcanvas.setFont('Helvetica', 9)
                for i in range(len(self.dataDFGroupedService)):
                    ypos=ypos-20
                    tempcanvas.drawString(45, ypos, str(i+1))
                    tempcanvas.drawString(90, ypos, self.dataDFGroupedService.iloc[i]['particular'])
                    tempcanvas.drawString(380, ypos, str(self.dataDFGroupedService.iloc[i]['quantity']))
                    tempcanvas.drawString(430, ypos, self.dataDFGroupedService.iloc[i]['unit'])
                    tempcanvas.drawString(460, ypos, str(self.dataDFGroupedService.iloc[i]['price']))
                    tempcanvas.drawString(510, ypos, str(self.dataDFGroupedService.iloc[i]['quantity']*self.dataDFGroupedService.iloc[i]['price']))
        ypos=280
        tempcanvas.line(40,ypos,560,ypos)
        tempcanvas.drawString(90, ypos-12.5, "Total")
        tempcanvas.drawString(380, ypos-12.5, str(self.getQuantityCount()))
        self.total=self.getTotal()
        tempcanvas.drawString(510, ypos-12.5, str(self.total))
        tempcanvas.line(40,ypos-20,560,ypos-20)
        tempcanvas.setFont('Helvetica', 12)
        tempcanvas.drawString(40, ypos-40, "INVOICE AMOUNT IN WORDS")
        tempcanvas.setFont('Helvetica', 9)
        tempcanvas.drawString(40, ypos-60, num2words.num2words(self.total).replace('-',' ').title()+" Only")
        tempcanvas.drawString(430, ypos-40, "Sub Total")
        tempcanvas.drawString(485, ypos-39, ":")
        tempcanvas.drawString(510, ypos-40, str(self.total))
        tempcanvas.drawString(430, ypos-60, "Total")
        tempcanvas.drawString(485, ypos-59, ":")
        tempcanvas.drawString(510, ypos-60, str(self.total))
        tempcanvas.drawString(430, ypos-80, "Recieved")
        tempcanvas.drawString(485, ypos-79, ":")
        tempcanvas.drawString(510, ypos-80, str(ui3.enteredRecievedAmount))
        tempcanvas.drawString(430, ypos-100, "Balance")
        tempcanvas.drawString(485, ypos-99, ":")
        self.balance=self.total-ui3.enteredRecievedAmount
        tempcanvas.drawString(510, ypos-100, str(self.balance))
        tempcanvas.drawString(405, ypos-140, "For SRI LAKSHMI AUTOMOTIVES")
        tempcanvas.drawString(435, ypos-200, "Authorized Signatory")
        tempcanvas.setFont('Helvetica', 12)
        tempcanvas.drawImage("tail1.png",40,30)
        tempcanvas.drawImage("tail2.png",330,22)
        tempcanvas.save()

    def proceedButtonPressed(self):
        _translate = QtCore.QCoreApplication.translate
        ui3.dateEdit.setDate(QDate.currentDate())
        AddWindow.close()
        DetailsWindow.show()

class Ui_DetailsWindow(object):
    def setupUi(self, DetailsWindow):
        DetailsWindow.setObjectName("DetailsWindow")
        DetailsWindow.resize(442, 242)
        DetailsWindow.setWindowIcon(QtGui.QIcon("logoicon.ico"))
        self.centralwidget = QtWidgets.QWidget(DetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createBillButton = QtWidgets.QPushButton(self.centralwidget)
        self.createBillButton.setGeometry(QtCore.QRect(160, 190, 112, 32))
        self.createBillButton.setObjectName("createBillButton")
        self.customerNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerNameLabel.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.customerNameLabel.setObjectName("customerNameLabel")
        self.customerNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.customerNameInput.setGeometry(QtCore.QRect(160, 30, 251, 21))
        self.customerNameInput.setObjectName("customerNameInput")
        self.vehicleNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.vehicleNumberLabel.setGeometry(QtCore.QRect(30, 70, 101, 16))
        self.vehicleNumberLabel.setObjectName("vehicleNumberLabel")
        self.vehicleNumberInput = QtWidgets.QLineEdit(self.centralwidget)
        self.vehicleNumberInput.setGeometry(QtCore.QRect(160, 69, 251, 21))
        self.vehicleNumberInput.setObjectName("vehicleNumberInput")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(30, 110, 101, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 109, 251, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.recievedAmountLabel = QtWidgets.QLabel(self.centralwidget)
        self.recievedAmountLabel.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.recievedAmountLabel.setObjectName("recievedAmountLabel")
        self.recievedAmountInput = QtWidgets.QLineEdit(self.centralwidget)
        self.recievedAmountInput.setGeometry(QtCore.QRect(160, 150, 251, 21))
        self.recievedAmountInput.setObjectName("recievedAmountInput")
        DetailsWindow.setCentralWidget(self.centralwidget)

        self.recievedAmountInput.setText("0.0")

        self.enteredCustomerName=self.customerNameInput.textChanged.connect(self.customerNameChanged)
        self.enteredVehicleNumber=self.vehicleNumberInput.textChanged.connect(self.vehicleNumberChanged)
        self.selectedDate=self.dateEdit.dateChanged.connect(self.dateSelected)
        self.enteredRecievedAmount=self.recievedAmountInput.textChanged.connect(self.recievedAmountChanged)

        self.createBillButton.clicked.connect(self.createBillButtonPressed)

        self.retranslateUi(DetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(DetailsWindow)

    def retranslateUi(self, DetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        DetailsWindow.setWindowTitle(_translate("DetailsWindow", "DetailsWindow"))
        self.createBillButton.setText(_translate("DetailsWindow", "Create Bill"))
        self.customerNameLabel.setText(_translate("DetailsWindow", "Customer Name"))
        self.vehicleNumberLabel.setText(_translate("DetailsWindow", "Vehicle Number"))
        self.dateLabel.setText(_translate("DetailsWindow", "Date"))
        self.recievedAmountLabel.setText(_translate("DetailsWindow", "Recieved Amount"))
        self.dateEdit.setDisplayFormat(_translate("DetailsWindow", "d/M/yyyy"))

    def customerNameChanged(self):
        self.enteredCustomerName=self.customerNameInput.text()

    def vehicleNumberChanged(self):
        self.enteredVehicleNumber=self.vehicleNumberInput.text()
    
    def dateSelected(self):
        self.selectedDate=self.dateEdit.date().toPyDate().strftime('%d/%m/%Y')
        self.Date=self.dateEdit.date().toPyDate().strftime('%y%m%d')

    def recievedAmountChanged(self):
        _translate = QtCore.QCoreApplication.translate
        if(self.recievedAmountInput.text()==""):
            self.recievedAmountInput.setText("0.0")
            self.enteredRecievedAmount=0
        else:
            try:
                self.enteredRecievedAmount=float(self.recievedAmountInput.text())
            except ValueError:
                # self.msgdisplayLabel.setText("Enter Valid Price")
                self.recievedAmountInput.setText("0.0")
                self.enteredRecievedAmount=0.0
        self.enteredRecievedAmount=float(self.recievedAmountInput.text())

    def createBillButtonPressed(self):
        self.enteredCustomerName=self.customerNameInput.text()
        self.enteredVehicleNumber=self.vehicleNumberInput.text()
        self.selectedDate=self.dateEdit.date().toPyDate().strftime('%d/%m/%Y')
        self.billNumber=self.dateEdit.date().toPyDate().strftime('%Y%m%d')+self.enteredVehicleNumber.replace(" ","")
        self.enteredRecievedAmount=float(self.recievedAmountInput.text())
        ui2.createPDF()
        DetailsWindow.close()
        AddWindow.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInWindow = QtWidgets.QMainWindow()
    ui1 = Ui_LogInWindow()
    ui1.setupUi(LogInWindow)
    AddWindow = QtWidgets.QMainWindow()
    ui2 = Ui_AddWindow()
    ui2.setupUi(AddWindow)
    DetailsWindow = QtWidgets.QMainWindow()
    ui3 = Ui_DetailsWindow()
    ui3.setupUi(DetailsWindow)
    LogInWindow.show()
    sys.exit(app.exec_())