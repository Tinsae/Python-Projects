"""
Created on Mon Jul  9 14:25:36 2018

@author: Tinsae
"""
    
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Homework4(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
            
    def initUI(self):
        
        self.setGeometry(500, 500, 400, 310)
        self.setMinimumSize(400, 310);
        self.setMaximumSize(400, 310);

        self.setWindowTitle('Home work 4')
        self.setWindowIcon(QIcon('web.png'))    
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        self.grid.setSpacing(0)
        self.setLayout(self.grid)
        
        #self.bp = QPushButton("Up")
        self.bp = upButton(self)

        self.bp.setText("Up")
        
        self.bl = QPushButton("Left")
        
        self.br = QPushButton("Right")

        self.bd = QPushButton("Down")



        self.mySizePolicy = QSizePolicy()
        self.mySizePolicy.setVerticalPolicy(QSizePolicy.Expanding)
        #self.mySizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
        
        self.bl.setSizePolicy(self.mySizePolicy)
        self.br.setSizePolicy(self.mySizePolicy)

        self.draw = DrawImage(self, "Up")

        self.grid.addWidget(self.bp, 0,0,1,5)
        self.grid.addWidget(self.bl, 1,0,3,1)
        self.grid.addWidget(self.draw, 1,2,3,1)
        self.grid.addWidget(self.br, 1,4,3,1)
        self.grid.addWidget(self.bd, 4,0,1,5)

        
        self.bp.clicked.connect(self.drawDiagram);
        self.bl.clicked.connect(self.drawDiagram);
        self.br.clicked.connect(self.drawDiagram);
        self.bd.clicked.connect(self.drawDiagram);

        
        
        self.show()
        
    def drawDiagram(self):
        if (self.sender().text() == "Up"):
            print("Up is clicked")
            self.draw = DrawImage(self, "Up")
            self.grid.addWidget(self.draw, 1,2,3,1)
        elif (self.sender().text() == "Down"):
            print("Down is clicked")
            self.draw = DrawImage(self, "Down")
            self.grid.addWidget(self.draw, 1,2,3,1)
        elif (self.sender().text() == "Left"):
            print("Left is clicked")
            self.draw = DrawImage(self, "Left")
            self.grid.addWidget(self.draw, 1,2,3,1)
        elif (self.sender().text() == "Right"):
            print("Right is clicked")
            self.draw = DrawImage(self, "Right")
            self.grid.addWidget(self.draw, 1,2,3,1)
        
        
            
    def closeEvent(self, event):
        #reply = QuitMessage().exec_()
        #if(reply == QMessageBox.Yes):
            event.accept()
        #else:
           # event.ignore()
            #print("you are not going anywhere")

class QuitMessage(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText("Wanna exit?")
        self.addButton(self.No)
        self.addButton(self.Yes)


class upButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
    def paintEvent(self, e):
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor(255, 0, 255, 255))
        qp.setPen(QColor(255, 255, 255))
        qp.save() # save the QPainter config

        buttonWidth = int(self.size().width())
        buttonHeight = int(self.size().height())

        buttonCenterX =buttonWidth/2.
        buttonCenterY = buttonHeight/2.

        qp.drawRect(buttonCenterX - buttonWidth/2.,
            buttonCenterY - buttonHeight/2.,
            buttonWidth, buttonHeight)
        qp.end()
            


          
class DrawImage(QLabel):
    
    def __init__(self, parent, which):
        super().__init__(parent)
        self.which = which

        #self.setStyleSheet('QFrame {background-color:grey;}')
        #self.resize(200, 200)
        
        self.mySizePolicy = QSizePolicy()
        self.mySizePolicy.setVerticalPolicy(QSizePolicy.Expanding)
        self.mySizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
        self.setSizePolicy(self.mySizePolicy)

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        #qp.setBrush(QColor(130, 100, 0))
        #qp.drawRect(0,0,120,200)

    def drawRectangles(self, qp):    
        qp.setBrush(QColor(255, 255, 255, 255))
        col = QColor(255, 255, 255)
        qp.setPen(col)
        qp.save() # save the QPainter config
        
        labelWidth = int(self.size().width())
        labelHeight = int(self.size().height())
        
        labelCenterX =labelWidth/2.
        labelCenterY = labelHeight/2.
        
        qp.drawRect(labelCenterX - labelWidth/4.,
                    labelCenterY - labelHeight/4.,
                    labelWidth/2., labelHeight/2.)

        if(self.which == "Up"):
            #the semicircles first
            radx = labelWidth/9
            rady = labelHeight/9
            qp.setPen(Qt.black)
            center = QPoint(labelCenterX, labelCenterY - (labelWidth/7) ) #7 is just perfect
            qp.setBrush(Qt.white)
            qp.drawEllipse(center, radx, rady)


            radx = labelWidth/13
            rady = labelHeight/13
            qp.setPen(Qt.white)
            center = QPoint(labelCenterX, labelCenterY - (labelWidth/7) ) #7 is just perfect
            qp.setBrush(QColor(255, 165, 0, 255))
            qp.drawEllipse(center, radx, rady)

        if(self.which == "Down"):
            #the semicircles first
            radx = labelWidth/9
            rady = labelHeight/9
            qp.setPen(Qt.black)
            center = QPoint(labelCenterX, labelCenterY + (labelWidth/7) ) #7 is just perfect
            qp.setBrush(Qt.white)
            qp.drawEllipse(center, radx, rady)


            radx = labelWidth/13
            rady = labelHeight/13
            qp.setPen(Qt.white)
            center = QPoint(labelCenterX, labelCenterY + (labelWidth/7) ) #7 is just perfect
            qp.setBrush(QColor(255, 165, 0, 255))
            qp.drawEllipse(center, radx, rady)


        
        elif(self.which == "Left"):
            #the semicircles first
            radx = labelWidth/9
            rady = labelHeight/9
            qp.setPen(Qt.black)
            center = QPoint(labelCenterX - (labelHeight/7), labelCenterY  ) #7 is just perfect
            qp.setBrush(Qt.white)
            qp.drawEllipse(center, radx, rady)


            radx = labelWidth/13
            rady = labelHeight/13
            qp.setPen(Qt.white)
            center = QPoint(labelCenterX - (labelHeight/7), labelCenterY  ) #7 is just perfect
            qp.setBrush(QColor(255, 165, 0, 255))
            qp.drawEllipse(center, radx, rady)


        elif(self.which == "Right"):
            #the semicircles first
            radx = labelWidth/9
            rady = labelHeight/9
            qp.setPen(Qt.black)
            center = QPoint(labelCenterX + (labelHeight/7), labelCenterY  ) #7 is just perfect
            qp.setBrush(Qt.white)
            qp.drawEllipse(center, radx, rady)


            radx = labelWidth/13
            rady = labelHeight/13
            qp.setPen(Qt.white)
            center = QPoint(labelCenterX + (labelHeight/7), labelCenterY  ) #7 is just perfect
            qp.setBrush(QColor(255, 165, 0, 255))
            qp.drawEllipse(center, radx, rady)

        
        # big white circle
        radx = labelWidth/6
        rady = labelHeight/6
        qp.setPen(Qt.black)
        center = QPoint(labelCenterX, labelCenterY)
        qp.setBrush(Qt.white)
        qp.drawEllipse(center, radx, rady)

        # orange circle
        radx = labelWidth/9
        rady = labelHeight/9
        qp.setPen(Qt.white)
        center = QPoint(labelCenterX, labelCenterY)
        qp.setBrush(QColor(255, 165, 0, 255))
        qp.drawEllipse(center, radx, rady)

        # small white circle
        radx = labelWidth/18
        rady = labelHeight/18
        qp.setPen(Qt.white)
        center = QPoint(labelCenterX, labelCenterY)
        qp.setBrush(Qt.white)
        qp.drawEllipse(center, radx, rady)


           
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ex = Homework4()
    sys.exit(app.exec_())
