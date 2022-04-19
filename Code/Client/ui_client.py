# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(2100, 1500)
        font = QtGui.QFont()
        font.setFamily("Arial")
        client.setFont(font)
        client.setStyleSheet(   
                "QWidget{ background:#f3f3f3 }"
        
                "QAbstractButton{ border-style:outset; border-radius:5px; border-color: #d3d3d3; padding:5px; color:#1a1a1a; background:#fafafa }"
                "QAbstractButton:hover{ color:#1a1a1a; background-color:#e8e8e8 }"
                "QAbstractButton:pressed{ color:#dcdcdc; background-color:#8a6353 }"
        
                "QLabel{ color:#1a1a1a }"
                "QLabel:focus{ border:1px solid #8a6353 }"
        
                "QLineEdit{ border:1px solid #d3d3d3; border-radius:5px; padding:2px; background:none; selection-background-color:#8a6353; selection-color:#dcdcdc }"
                "QLineEdit:focus,QLineEdit:hover{ border:1px solid #d3d3d3 }"
                "QLineEdit{ lineedit-password-character:9679 }"

                "QSlider::groove:horizontal,QSlider::add-page:horizontal{ height:3px; border-radius:3px; background:#fafafa }"
                "QSlider::sub-page:horizontal{ height:8px; border-radius:3px; background:#8a6353 }"
                "QSlider::handle:horizontal{ width:12px; margin-top:-5px; margin-bottom:-4px; border-radius:6px; background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #8a6353,stop:0.8 #8a6353) }"
                "QSlider::groove:vertical,QSlider::sub-page:vertical{ width:3px; border-radius:3px; background:#fafafa }"
                "QSlider::add-page:vertical{ width:8px; border-radius:3px; background:#8a6353 }"
                "QSlider::handle:vertical{ height:12px; margin-left:-5px; margin-right:-4px; border-radius:6px; background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #8a6353,stop:0.8 #8a6353) }"
        
                "QGroupBox::title { pading:2px; color:white; subcontrol-position: top center; border-top:0px ; background: transparent; }")
        
        client.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.Video = QtWidgets.QLabel(client)
        self.Video.setGeometry(QtCore.QRect(30, 30, 990, 810))
        self.Video.setFont(font)
        self.Video.setText("")
        self.Video.setObjectName("Video")

        self.Button_Connect = QtWidgets.QPushButton(client)
        self.Button_Connect.setGeometry(QtCore.QRect(30, 1380, 180, 30))
        self.Button_Connect.setFont(font)
        self.Button_Connect.setObjectName("Button_Connect")

        self.lineEdit_IP_Adress = QtWidgets.QLineEdit(client)
        self.lineEdit_IP_Adress.setGeometry(QtCore.QRect(240, 1380, 180, 30))
        self.lineEdit_IP_Adress.setFont(font)
        self.lineEdit_IP_Adress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_IP_Adress.setObjectName("lineEdit_IP_Adress")

        self.Button_Calibration = QtWidgets.QPushButton(client)
        self.Button_Calibration.setGeometry(QtCore.QRect(30, 1440, 180, 30))
        font.setBold(False)
        font.setWeight(50)
        self.Button_Calibration.setFont(font)
        self.Button_Calibration.setObjectName("Button_Calibration")

        self.Button_Video = QtWidgets.QPushButton(client)
        self.Button_Video.setGeometry(QtCore.QRect(1560, 1320, 180, 30))
        font.setBold(False)
        font.setWeight(50)
        self.Button_Video.setFont(font)
        self.Button_Video.setObjectName("Button_Video")

        # Button labelled balance
        self.Button_IMU = QtWidgets.QPushButton(client)
        self.Button_IMU.setGeometry(QtCore.QRect(1350, 1380, 180, 30))
        self.Button_IMU.setFont(font)
        self.Button_IMU.setObjectName("Button_IMU")
        
        self.Button_Buzzer = QtWidgets.QPushButton(client)
        self.Button_Buzzer.setGeometry(QtCore.QRect(1140, 1320, 180, 30))
        self.Button_Buzzer.setFont(font)
        self.Button_Buzzer.setObjectName("Button_Buzzer")

        # Button for ultrasound obstacle detection and it's output
        self.Button_Sonic = QtWidgets.QPushButton(client)
        self.Button_Sonic.setGeometry(QtCore.QRect(1140, 1380, 180, 30))
        self.Button_Sonic.setFont(font)
        self.Button_Sonic.setObjectName("Button_Sonic")

        self.label_sonic = QtWidgets.QLabel(client)
        self.label_sonic.setGeometry(QtCore.QRect(1140, 1440, 180, 30))
        self.label_sonic.setFont(font)
        self.label_sonic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sonic.setObjectName("label_sonic")

        self.Button_LED = QtWidgets.QPushButton(client)
        self.Button_LED.setGeometry(QtCore.QRect(1350, 1320, 180, 30))
        self.Button_LED.setFont(font)
        self.Button_LED.setObjectName("Button_LED")

        # Twist slider and it's labels
        self.label_twist_title = QtWidgets.QLabel(client)
        self.label_twist_title.setGeometry(QtCore.QRect(1590, 1230, 120, 30))
        self.label_twist_title.setFont(font)
        self.label_twist_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_twist_title.setObjectName("label_twist_title")

        self.label_twist_value = QtWidgets.QLabel(client)
        self.label_twist_value.setGeometry(QtCore.QRect(1590, 1200, 120, 30))
        self.label_twist_value.setFont(font)
        self.label_twist_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_twist_value.setObjectName("label_twist_value")

        self.slider_twist = QtWidgets.QSlider(client)
        self.slider_twist.setGeometry(QtCore.QRect(1620, 900, 60, 300))
        self.slider_twist.setMinimum(-20)
        self.slider_twist.setMaximum(20)
        self.slider_twist.setOrientation(QtCore.Qt.Vertical)
        self.slider_twist.setObjectName("slider_twist")


        self.label_attitude = QtWidgets.QLabel(client)
        self.label_attitude.setGeometry(QtCore.QRect(801, 185, 60, 20))
        self.label_attitude.setFont(font)
        self.label_attitude.setAlignment(QtCore.Qt.AlignCenter)
        self.label_attitude.setObjectName("label_attitude")

        self.label_Y = QtWidgets.QLabel(client)
        self.label_Y.setGeometry(QtCore.QRect(891, 285, 30, 20))
        self.label_Y.setFont(font)
        self.label_Y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y.setObjectName("label_Y")

        self.label_Y_2 = QtWidgets.QLabel(client)
        self.label_Y_2.setGeometry(QtCore.QRect(786, 285, 30, 20))
        self.label_Y_2.setFont(font)
        self.label_Y_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_2.setObjectName("label_Y_2")

        self.label_Y_3 = QtWidgets.QLabel(client)
        self.label_Y_3.setGeometry(QtCore.QRect(686, 285, 30, 20))
        self.label_Y_3.setFont(font)
        self.label_Y_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_3.setObjectName("label_Y_3")

        self.label_Y_4 = QtWidgets.QLabel(client)
        self.label_Y_4.setGeometry(QtCore.QRect(921, 285, 40, 20))
        self.label_Y_4.setFont(font)
        self.label_Y_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_4.setObjectName("label_Y_4")

        self.label_X = QtWidgets.QLabel(client)
        self.label_X.setGeometry(QtCore.QRect(665, 265, 30, 20))
        self.label_X.setFont(font)
        self.label_X.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X.setObjectName("label_X")

        self.label_X_2 = QtWidgets.QLabel(client)
        self.label_X_2.setGeometry(QtCore.QRect(665, 170, 30, 20))
        self.label_X_2.setFont(font)
        self.label_X_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_2.setObjectName("label_X_2")

        self.label_X_3 = QtWidgets.QLabel(client)
        self.label_X_3.setGeometry(QtCore.QRect(665, 74, 30, 20))
        self.label_X_3.setFont(font)
        self.label_X_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_3.setObjectName("label_X_3")

        self.label_X_4 = QtWidgets.QLabel(client)
        self.label_X_4.setGeometry(QtCore.QRect(645, 90, 50, 20))
        self.label_X_4.setFont(font)
        self.label_X_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_4.setObjectName("label_X_4")

        self.label_X_5 = QtWidgets.QLabel(client)
        self.label_X_5.setGeometry(QtCore.QRect(736, 54, 131, 20))
        self.label_X_5.setFont(font)
        self.label_X_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_5.setObjectName("label_X_5")

        self.label_Y_5 = QtWidgets.QLabel(client)
        self.label_Y_5.setGeometry(QtCore.QRect(917, 751, 40, 20))
        self.label_Y_5.setFont(font)
        self.label_Y_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_5.setObjectName("label_Y_5")

        self.label_Y_6 = QtWidgets.QLabel(client)
        self.label_Y_6.setGeometry(QtCore.QRect(686, 751, 30, 20))
        self.label_Y_6.setFont(font)
        self.label_Y_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_6.setObjectName("label_Y_6")

        self.label_X_6 = QtWidgets.QLabel(client)
        self.label_X_6.setGeometry(QtCore.QRect(665, 545, 30, 20))
        self.label_X_6.setFont(font)
        self.label_X_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_6.setObjectName("label_X_6")

        self.label_Y_7 = QtWidgets.QLabel(client)
        self.label_Y_7.setGeometry(QtCore.QRect(786, 751, 30, 20))
        self.label_Y_7.setFont(font)
        self.label_Y_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_7.setObjectName("label_Y_7")

        self.label_X_7 = QtWidgets.QLabel(client)
        self.label_X_7.setGeometry(QtCore.QRect(665, 640, 30, 20))
        self.label_X_7.setFont(font)
        self.label_X_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_7.setObjectName("label_X_7")

        self.label_Y_8 = QtWidgets.QLabel(client)
        self.label_Y_8.setGeometry(QtCore.QRect(891, 751, 30, 20))
        self.label_Y_8.setFont(font)
        self.label_Y_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Y_8.setObjectName("label_Y_8")

        self.label_X_8 = QtWidgets.QLabel(client)
        self.label_X_8.setGeometry(QtCore.QRect(665, 735, 30, 20))
        self.label_X_8.setFont(font)
        self.label_X_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_8.setObjectName("label_X_8")

        self.label_X_9 = QtWidgets.QLabel(client)
        self.label_X_9.setGeometry(QtCore.QRect(650, 560, 40, 20))
        self.label_X_9.setFont(font)
        self.label_X_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_9.setObjectName("label_X_9") 
 
        self.label_X_10 = QtWidgets.QLabel(client)
        self.label_X_10.setGeometry(QtCore.QRect(736, 525, 130, 20))
        self.label_X_10.setFont(font)
        self.label_X_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_X_10.setObjectName("label_X_10")
 
        self.label_position = QtWidgets.QLabel(client)
        self.label_position.setGeometry(QtCore.QRect(801, 655, 60, 20))
        self.label_position.setFont(font)
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")

        # Height slider and its values
        self.label_height = QtWidgets.QLabel(client)
        self.label_height.setGeometry(QtCore.QRect(1110, 1230, 120, 30))
        self.label_height.setFont(font)
        self.label_height.setAlignment(QtCore.Qt.AlignCenter)
        self.label_height.setObjectName("label_height")

        self.slider_height = QtWidgets.QSlider(client)
        self.slider_height.setGeometry(QtCore.QRect(1140, 900, 60, 300))
        self.slider_height.setMinimum(-40)
        self.slider_height.setMaximum(40)
        self.slider_height.setOrientation(QtCore.Qt.Vertical)
        self.slider_height.setObjectName("slider_height")

        self.label_height_value = QtWidgets.QLabel(client)
        self.label_height_value.setGeometry(QtCore.QRect(1110, 1200, 120, 30))
        self.label_height_value.setFont(font)
        self.label_height_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_height_value.setObjectName("label_height_value")

        self.Button_Face_ID = QtWidgets.QPushButton(client)
        self.Button_Face_ID.setGeometry(QtCore.QRect(1560, 1440, 180, 30))
        self.Button_Face_ID.setFont(font)
        self.Button_Face_ID.setObjectName("Button_Face_ID")

        self.Button_Face_Recognition = QtWidgets.QPushButton(client)
        self.Button_Face_Recognition.setGeometry(QtCore.QRect(1560, 1380, 180, 30))
        self.Button_Face_Recognition.setFont(font)
        self.Button_Face_Recognition.setObjectName("Button_Face_Recognition")

        self.Button_Relax = QtWidgets.QPushButton(client)
        self.Button_Relax.setGeometry(QtCore.QRect(1350, 1440, 180, 30))
        self.Button_Relax.setFont(font)
        self.Button_Relax.setObjectName("Button_Relax")

        self.slider_head_1 = QtWidgets.QSlider(client)
        self.slider_head_1.setGeometry(QtCore.QRect(245, 765, 160, 20))
        self.slider_head_1.setMaximum(180)
        self.slider_head_1.setProperty("value", 90)
        self.slider_head_1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_head_1.setObjectName("slider_head_1")

        self.label_head_1 = QtWidgets.QLabel(client)
        self.label_head_1.setGeometry(QtCore.QRect(410, 765, 30, 20))
        self.label_head_1.setFont(font)
        self.label_head_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_head_1.setObjectName("label_head_1")

        self.label_10 = QtWidgets.QLabel(client)
        self.label_10.setGeometry(QtCore.QRect(195, 765, 50, 20))
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.label_8 = QtWidgets.QLabel(client)
        self.label_8.setGeometry(QtCore.QRect(480, 555, 30, 16))
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.slider_head = QtWidgets.QSlider(client)
        self.slider_head.setGeometry(QtCore.QRect(485, 572, 20, 160))
        self.slider_head.setMaximum(180)
        self.slider_head.setProperty("value", 90)
        self.slider_head.setOrientation(QtCore.Qt.Vertical)
        self.slider_head.setObjectName("slider_head")

        self.label_head = QtWidgets.QLabel(client)
        self.label_head.setGeometry(QtCore.QRect(480, 732, 30, 20))
        self.label_head.setFont(font)
        self.label_head.setAlignment(QtCore.Qt.AlignCenter)
        self.label_head.setObjectName("label_head")

        self.label_7 = QtWidgets.QLabel(client)
        self.label_7.setGeometry(QtCore.QRect(553, 555, 36, 16))
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_speed = QtWidgets.QLabel(client)
        self.label_speed.setGeometry(QtCore.QRect(563, 732, 16, 16))
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")

        self.slider_speed = QtWidgets.QSlider(client)
        self.slider_speed.setGeometry(QtCore.QRect(560, 572, 20, 160))
        self.slider_speed.setFont(font)
        self.slider_speed.setMinimum(2)
        self.slider_speed.setMaximum(10)
        self.slider_speed.setProperty("value", 8)
        self.slider_speed.setOrientation(QtCore.Qt.Vertical)
        self.slider_speed.setObjectName("slider_speed")

        self.label_Load = QtWidgets.QLabel(client)
        self.label_Load.setGeometry(QtCore.QRect(1770, 1380, 90, 30))
        self.label_Load.setObjectName("label_Load")

        self.progress_Power1 = QtWidgets.QProgressBar(client)
        self.progress_Power1.setGeometry(QtCore.QRect(1890, 1380, 180, 30))
        self.progress_Power1.setStyleSheet(
                "QProgressBar::chunk { background-color:#08aaff; width: 20px } "
                "QProgressBar { border-style:outset; border-radius:2px; border-color: #d3d3d3; padding: 5px; background-color: #FFFFFF }"
                "QProgressBar { text-align: center; color: rgb(0,0,0) }")
        self.progress_Power1.setProperty("value", 100)
        self.progress_Power1.setFormat("")
        self.progress_Power1.setObjectName("progress_Power1")

        self.label_RasPi = QtWidgets.QLabel(client)
        self.label_RasPi.setGeometry(QtCore.QRect(1770, 1440, 90, 30))
        self.label_RasPi.setObjectName("label_RasPi")

        self.progress_Power2 = QtWidgets.QProgressBar(client)
        self.progress_Power2.setGeometry(QtCore.QRect(1890, 1440, 180, 30))
        self.progress_Power2.setStyleSheet(
                "QProgressBar::chunk { background-color:#26fa03; width: 20px; }"
                "QProgressBar { border-style:outset; border-radius:2px; border-color: #d3d3d3; padding: 5px; background-color: #FFFFFF }"
                "QProgressBar { text-align: center; color: rgb(0,0,0) }")
        self.progress_Power2.setProperty("value", 100)
        self.progress_Power2.setFormat("")
        self.progress_Power2.setObjectName("progress_Power2")
        
        self.layoutWidget = QtWidgets.QWidget(client)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 1380, 180, 90))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonActionMode1 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ButtonActionMode1.setFont(font)
        self.ButtonActionMode1.setObjectName("ButtonActionMode1")
        self.verticalLayout.addWidget(self.ButtonActionMode1)
        self.ButtonActionMode2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ButtonActionMode2.setFont(font)
        self.ButtonActionMode2.setObjectName("ButtonActionMode2")

        self.verticalLayout.addWidget(self.ButtonActionMode2)
        self.layoutWidget1 = QtWidgets.QWidget(client)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 1380, 180, 90))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ButtonGaitMode1 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ButtonGaitMode1.setFont(font)
        self.ButtonGaitMode1.setObjectName("ButtonGaitMode1")
        self.verticalLayout_2.addWidget(self.ButtonGaitMode1)
        self.ButtonGaitMode2 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ButtonGaitMode2.setFont(font)
        self.ButtonGaitMode2.setObjectName("ButtonGaitMode2")
        self.verticalLayout_2.addWidget(self.ButtonGaitMode2)

        self.Video.raise_()
        self.Button_Buzzer.raise_()
        self.lineEdit_IP_Adress.raise_()
        self.Button_Connect.raise_()
        self.Button_Video.raise_()
        self.Button_IMU.raise_()
        self.Button_Calibration.raise_()
        self.Button_Sonic.raise_()
        self.Button_LED.raise_()

        self.label_twist_title.raise_()
        self.label_twist_value.raise_()
        self.slider_twist.raise_()

        self.label_attitude.raise_()
        self.label_Y.raise_()
        self.label_Y_2.raise_()
        self.label_Y_3.raise_()
        self.label_Y_4.raise_()
        self.label_X.raise_()
        self.label_X_2.raise_()
        self.label_X_3.raise_()
        self.label_X_4.raise_()
        self.label_X_5.raise_()
        self.label_sonic.raise_()
        self.label_Y_5.raise_()
        self.label_Y_6.raise_()
        self.label_X_6.raise_()
        self.label_Y_7.raise_()
        self.label_X_7.raise_()
        self.label_Y_8.raise_()
        self.label_X_8.raise_()
        self.label_position.raise_()
        self.label_X_9.raise_()
        self.label_X_10.raise_()
        self.slider_height.raise_()
        self.label_height_value.raise_()
        self.label_height.raise_()
        self.Button_Face_ID.raise_()
        self.Button_Face_Recognition.raise_()
        self.Button_Relax.raise_()
        self.slider_head_1.raise_()
        self.label_head_1.raise_()
        self.label_10.raise_()
        self.label_8.raise_()
        self.slider_head.raise_()
        self.label_head.raise_()
        self.label_7.raise_()
        self.label_speed.raise_()
        self.slider_speed.raise_()
        self.progress_Power2.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget1.raise_()
        self.label_RasPi.raise_()
        self.label_Load.raise_()
        self.progress_Power1.raise_()

        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Freenove Client for Hexapod by PR"))
        self.Button_Buzzer.setText(_translate("client", "Buzzer"))
        self.lineEdit_IP_Adress.setText(_translate("client", "x.x.x.x"))
        self.Button_Connect.setText(_translate("client", "Connect"))
        self.Button_Video.setText(_translate("client", "Open Video"))
        self.Button_IMU.setText(_translate("client", "Balance"))
        self.Button_Calibration.setText(_translate("client", "Calibration"))
        self.Button_Sonic.setText(_translate("client", "Sonar"))
        self.label_sonic.setText(_translate("client", "Obstacle: 0cm"))

        self.Button_LED.setText(_translate("client", "LED"))

        self.label_twist_title.setText(_translate("client", "Twist"))
        self.label_twist_value.setText(_translate("client", "0"))

        self.label_height.setText(_translate("client", "Height"))
        self.label_height_value.setText(_translate("client", "0"))

        self.label_Y_4.setText(_translate("client", "(Yaw)"))

        self.label_attitude.setText(_translate("client", "(0,0)"))
        self.label_Y.setText(_translate("client", "15"))
        self.label_Y_2.setText(_translate("client", "0"))
        self.label_Y_3.setText(_translate("client", "-15"))

        self.label_X.setText(_translate("client", "-15"))
        self.label_X_2.setText(_translate("client", "0"))
        self.label_X_3.setText(_translate("client", "15"))
        self.label_X_4.setText(_translate("client", "(Pitch)"))
        self.label_X_5.setText(_translate("client", "Attitude"))

        self.label_Y_5.setText(_translate("client", "(X)"))
        self.label_Y_6.setText(_translate("client", "-40"))
       
        self.label_X_6.setText(_translate("client", "40"))
       
        self.label_Y_7.setText(_translate("client", "0"))
       
        self.label_X_7.setText(_translate("client", "0"))
       
        self.label_Y_8.setText(_translate("client", "40"))
       
        self.label_X_8.setText(_translate("client", "-40"))

        self.label_position.setText(_translate("client", "(0,0)"))
        self.label_X_9.setText(_translate("client", "(Y)"))
        self.label_X_10.setText(_translate("client", "Position"))


        
        self.Button_Face_ID.setText(_translate("client", "Face ID"))
        self.Button_Face_Recognition.setText(_translate("client", "Face Recog"))
        self.Button_Relax.setText(_translate("client", "Relax"))
        self.label_head_1.setText(_translate("client", "90"))
        self.label_10.setText(_translate("client", "Head"))
        self.label_8.setText(_translate("client", "Head"))
        self.label_head.setText(_translate("client", "90"))
        self.label_7.setText(_translate("client", "Speed"))
        self.label_speed.setText(_translate("client", "8"))

        self.ButtonActionMode1.setText(_translate("client", "Turn"))
        self.ButtonActionMode2.setText(_translate("client", "Strafe"))
        self.ButtonGaitMode1.setText(_translate("client", "Walk"))
        self.ButtonGaitMode2.setText(_translate("client", "Run"))
        self.label_RasPi.setText(_translate("client", "RasPi"))
        self.label_Load.setText(_translate("client", "Load"))
