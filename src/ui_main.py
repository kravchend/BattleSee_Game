from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 750)
        MainWindow.setFixedSize(1240, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_fon = QtWidgets.QLabel(self.centralwidget)
        self.label_fon.setGeometry(QtCore.QRect(0, 0, 1240, 750)) 
        self.label_fon.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/fon.png"))
        self.label_fon.setScaledContents(True)

        self.statuslabel_Ramkalicht = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel_Ramkalicht.setGeometry(QtCore.QRect(375, 28, 500, 45))
        self.statuslabel_Ramkalicht.setAutoFillBackground(False)
        self.statuslabel_Ramkalicht.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.statuslabel_Ramkalicht.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.statuslabel_Ramkalicht.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.statuslabel_Ramkalicht.setLineWidth(9)
        self.statuslabel_Ramkalicht.setMidLineWidth(2)
        self.statuslabel_Ramkalicht.setObjectName("statuslabel_Ramkalicht")
        self.licht_effect(self.statuslabel_Ramkalicht, x_offset=0, y_offset=-7, blur_radius=50)

        self.label_playerRamkalicht = QtWidgets.QLabel(self.centralwidget)
        self.label_playerRamkalicht.setGeometry(QtCore.QRect(65, 112, 500, 490))
        self.label_playerRamkalicht.setAutoFillBackground(False)
        self.label_playerRamkalicht.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_playerRamkalicht.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_playerRamkalicht.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_playerRamkalicht.setLineWidth(9)
        self.label_playerRamkalicht.setMidLineWidth(2)
        self.label_playerRamkalicht.setObjectName("label_playerRamkalicht")
        self.licht_effect(self.label_playerRamkalicht, x_offset=0, y_offset=-7, blur_radius=55)

        self.label_playerRamkalinks = QtWidgets.QLabel(self.centralwidget)
        self.label_playerRamkalinks.setGeometry(QtCore.QRect(52, 110, 535, 535))
        self.label_playerRamkalinks.setAutoFillBackground(False)
        self.label_playerRamkalinks.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_playerRamkalinks.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_playerRamkalinks.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_playerRamkalinks.setLineWidth(9)
        self.label_playerRamkalinks.setMidLineWidth(2)
        self.label_playerRamkalinks.setObjectName("label_playerRamkalinks")
        self.add_shadow_effect(self.label_playerRamkalinks, x_offset=-15, y_offset=0, blur_radius=80)

        self.label_playerRamkaRechts= QtWidgets.QLabel(self.centralwidget)
        self.label_playerRamkaRechts.setGeometry(QtCore.QRect(52, 110, 535, 535))
        self.label_playerRamkaRechts.setAutoFillBackground(False)
        self.label_playerRamkaRechts.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_playerRamkaRechts.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_playerRamkaRechts.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_playerRamkaRechts.setLineWidth(9)
        self.label_playerRamkaRechts.setMidLineWidth(2)
        self.label_playerRamkaRechts.setObjectName("label_playerRamkaRechts")
        self.add_shadow_effect(self.label_playerRamkaRechts, x_offset=18, y_offset=0, blur_radius=70)

        self.label_playerRamka = QtWidgets.QLabel(self.centralwidget)
        self.label_playerRamka.setGeometry(QtCore.QRect(52, 110, 535, 535))
        self.label_playerRamka.setAutoFillBackground(False)
        self.label_playerRamka.setStyleSheet("background-color: rgb(10, 10, 10); border-color: rgb(10, 10, 10);")
        self.label_playerRamka.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_playerRamka.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_playerRamka.setLineWidth(9)
        self.label_playerRamka.setMidLineWidth(2)
        self.label_playerRamka.setObjectName("label_playerRamka")
        self.add_shadow_effect(self.label_playerRamka, x_offset=0, y_offset=25, blur_radius=40)
        self.apply_3d_borders(self.label_playerRamka)

        self.label_enemyRamkalicht = QtWidgets.QLabel(self.centralwidget)
        self.label_enemyRamkalicht.setGeometry(QtCore.QRect(665, 110, 500, 490))
        self.label_enemyRamkalicht.setAutoFillBackground(False)
        self.label_enemyRamkalicht.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_enemyRamkalicht.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_enemyRamkalicht.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_enemyRamkalicht.setLineWidth(9)
        self.label_enemyRamkalicht.setMidLineWidth(2)
        self.label_enemyRamkalicht.setObjectName("label_enemyRamkalicht")
        self.licht_effect(self.label_enemyRamkalicht, x_offset=0, y_offset=-7, blur_radius=70)

        self.label_enemyRamkalinks = QtWidgets.QLabel(self.centralwidget)
        self.label_enemyRamkalinks.setGeometry(QtCore.QRect(652, 110, 535, 535))
        self.label_enemyRamkalinks.setAutoFillBackground(False)
        self.label_enemyRamkalinks.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_enemyRamkalinks.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_enemyRamkalinks.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_enemyRamkalinks.setLineWidth(9)
        self.label_enemyRamkalinks.setMidLineWidth(2)
        self.label_enemyRamkalinks.setObjectName("label_enemyRamkalinks")
        self.add_shadow_effect(self.label_enemyRamkalinks, x_offset=-18, y_offset=0, blur_radius=70)

        self.label_enemyRamkaRechts = QtWidgets.QLabel(self.centralwidget)
        self.label_enemyRamkaRechts.setGeometry(QtCore.QRect(652, 110, 535, 535))
        self.label_enemyRamkaRechts.setAutoFillBackground(False)
        self.label_enemyRamkaRechts.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.label_enemyRamkaRechts.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_enemyRamkaRechts.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_enemyRamkaRechts.setLineWidth(9)
        self.label_enemyRamkaRechts.setMidLineWidth(2)
        self.label_enemyRamkaRechts.setObjectName("label_enemyRamkaRechts")
        self.add_shadow_effect(self.label_enemyRamkaRechts, x_offset=15, y_offset=0, blur_radius=70)

        self.statuslabel_Ramkalinks = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel_Ramkalinks.setGeometry(QtCore.QRect(367, 25, 515, 50))
        self.statuslabel_Ramkalinks.setAutoFillBackground(False)
        self.statuslabel_Ramkalinks.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.statuslabel_Ramkalinks.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.statuslabel_Ramkalinks.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.statuslabel_Ramkalinks.setLineWidth(9)
        self.statuslabel_Ramkalinks.setMidLineWidth(2)
        self.statuslabel_Ramkalinks.setObjectName("statuslabel_Ramkalinks")
        self.add_shadow_effect(self.statuslabel_Ramkalinks, x_offset=-12, y_offset=0, blur_radius=40)

        self.statuslabel_RamkaRechts = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel_RamkaRechts.setGeometry(QtCore.QRect(367, 25, 515, 50))
        self.statuslabel_RamkaRechts.setAutoFillBackground(False)
        self.statuslabel_RamkaRechts.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.statuslabel_RamkaRechts.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.statuslabel_RamkaRechts.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.statuslabel_RamkaRechts.setLineWidth(9)
        self.statuslabel_RamkaRechts.setMidLineWidth(2)
        self.statuslabel_RamkaRechts.setObjectName("statuslabel_Ramkaechts")
        self.add_shadow_effect(self.statuslabel_RamkaRechts, x_offset=11, y_offset=0, blur_radius=40)

        self.statuslabel_Ramka = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel_Ramka.setGeometry(QtCore.QRect(367, 23, 515, 54))
        self.statuslabel_Ramka.setAutoFillBackground(False)
        self.statuslabel_Ramka.setStyleSheet("background-color: rgb(10, 13, 30); border-color: rgb(10, 13, 30);")
        self.statuslabel_Ramka.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.statuslabel_Ramka.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.statuslabel_Ramka.setLineWidth(2)
        self.statuslabel_Ramka.setMidLineWidth(1)
        self.statuslabel_Ramka.setObjectName("statuslabel_Ramka")
        self.add_shadow_effect(self.statuslabel_Ramka, x_offset=0, y_offset=17, blur_radius=30)
        self.apply_3d_borders(self.statuslabel_Ramka)

        self.label_enemyRamka = QtWidgets.QLabel(self.centralwidget)
        self.label_enemyRamka.setGeometry(QtCore.QRect(652, 110, 535, 535))
        self.label_enemyRamka.setAutoFillBackground(False)
        self.label_enemyRamka.setStyleSheet("background-color: rgb(10, 10, 10); border-color: rgb(10, 10, 10);")
        self.label_enemyRamka.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_enemyRamka.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.label_enemyRamka.setLineWidth(9)
        self.label_enemyRamka.setMidLineWidth(2)
        self.label_enemyRamka.setObjectName("label_enemyRamka")
        self.add_shadow_effect(self.label_enemyRamka, x_offset=0, y_offset=25, blur_radius=40)
        self.apply_3d_borders(self.label_enemyRamka)

        self.playerBoard = QtWidgets.QWidget(self.centralwidget)
        self.playerBoard.setGeometry(QtCore.QRect(70, 127, 500, 500))
        self.playerBoard.setStyleSheet("background-color: rgb(10, 13, 30);")
        self.playerBoard.setObjectName("playerBoard")

        self.playerBoard_bildLoser = QtWidgets.QLabel(self.centralwidget)
        self.playerBoard_bildLoser.setGeometry(self.playerBoard.geometry())
        self.playerBoard_bildLoser.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/gameOver.png"))
        self.playerBoard_bildLoser.setScaledContents(True)

        self.playerBoard_bildWinner = QtWidgets.QLabel(self.centralwidget)
        self.playerBoard_bildWinner.setGeometry(self.playerBoard.geometry())
        self.playerBoard_bildWinner.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/winnerPlayer.png"))
        self.playerBoard_bildWinner.setScaledContents(True)

        self.playerBoard_bild = QtWidgets.QLabel(self.centralwidget)
        self.playerBoard_bild.setGeometry(self.playerBoard.geometry())
        self.playerBoard_bild.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/fensterGame.png"))
        self.playerBoard_bild.setScaledContents(True)

        self.gridLayout = QtWidgets.QGridLayout(self.playerBoard)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.enemyBoard = QtWidgets.QWidget(self.centralwidget)
        self.enemyBoard.setGeometry(QtCore.QRect(670, 127, 500, 500))
        self.enemyBoard.setStyleSheet("background-color: rgb(10, 13, 30);")
        self.enemyBoard.setObjectName("enemyBoard")

        self.enemyBoard_bildWinner = QtWidgets.QLabel(self.centralwidget)
        self.enemyBoard_bildWinner.setGeometry(self.enemyBoard.geometry())
        self.enemyBoard_bildWinner.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/winnerAi.png"))
        self.enemyBoard_bildWinner.setScaledContents(True)

        self.enemyBoard_bildLoser = QtWidgets.QLabel(self.centralwidget)
        self.enemyBoard_bildLoser.setGeometry(self.enemyBoard.geometry())
        self.enemyBoard_bildLoser.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/gameOver.png"))
        self.enemyBoard_bildLoser.setScaledContents(True)

        self.enemyBoard_bild = QtWidgets.QLabel(self.centralwidget)
        self.enemyBoard_bild.setGeometry(self.enemyBoard.geometry())
        self.enemyBoard_bild.setPixmap(QtGui.QPixmap(
            "/Users/dmitriykravchenko/Documents/Programirovanie/BattleSee_Game/.venv/resource/fensterGame.png"))
        self.enemyBoard_bild.setScaledContents(True)

        button_style = """
            QPushButton {
                background-color: rgba(240, 230, 170, 15%);
                border: 2px solid rgba(205, 180, 180, 40%);
                border-radius: 7px;
                color: white;
                font-size: 14px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: rgba(240, 230, 170, 30%);
                border: 2px solid rgba(205, 180, 180, 50%);
            }
            QPushButton:pressed {
                background-color: rgba(240, 230, 170, 50%);
                border: 2px solid rgba(205, 180, 180, 70%);
            }
        """

        self.gridLayout_2 = QtWidgets.QGridLayout(self.enemyBoard)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.newGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.newGameButton.setGeometry(QtCore.QRect(860, 675, 120, 40))
        self.newGameButton.setObjectName("newGameButton")
        self.newGameButton.setStyleSheet(button_style)
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(40)
        self.newGameButton.setFont(font)

        self.surrenderButton = QtWidgets.QPushButton(self.centralwidget)
        self.surrenderButton.setGeometry(QtCore.QRect(1030, 675, 120, 40))
        self.surrenderButton.setObjectName("surrenderButton")
        self.surrenderButton.setStyleSheet(button_style)
        self.surrenderButton.setFont(font)

        self.enemy_shipsButton = QtWidgets.QPushButton(self.centralwidget)
        self.enemy_shipsButton.setGeometry(QtCore.QRect(80, 675, 120, 40))
        self.enemy_shipsButton.setObjectName("enemy_shipsButton")
        self.enemy_shipsButton.setStyleSheet(button_style)
        self.enemy_shipsButton.setFont(font)

        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(375, 30, 500, 40))
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statusLabel.setStyleSheet("background-color: rgb(32, 40, 46);")
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(20) 

        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_shadow_effect(self, widget, *, x_offset=0, y_offset=0, blur_radius=10):
        shadow = QtWidgets.QGraphicsDropShadowEffect(widget)
        color = QtGui.QColor(0, 0, 0, 180)
        shadow.setColor(color)
        shadow.setOffset(x_offset, y_offset)
        shadow.setBlurRadius(blur_radius)
        widget.setGraphicsEffect(shadow)

    def licht_effect(self, widget, *, x_offset=0, y_offset=0, blur_radius=10):
        licht = QtWidgets.QGraphicsDropShadowEffect(widget)
        color = QtGui.QColor(240, 230, 170, 200)
        licht.setColor(color)
        licht.setOffset(abs(x_offset), (y_offset))
        licht.setBlurRadius(blur_radius)
        widget.setGraphicsEffect(licht)

    def apply_3d_borders(self, widget):
        original_paint_event = widget.paintEvent

        def paint_with_borders(event):
            original_paint_event(event)

            painter = QPainter(widget)

            painter.setPen(QColor(205, 180, 180))
            painter.drawLine(0, 0, widget.width(), 0)

        widget.paintEvent = paint_with_borders

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SEE BATTLE"))
        self.newGameButton.setText(_translate("MainWindow", "NEW GAME"))
        self.surrenderButton.setText(_translate("MainWindow", "SURRENDER"))
        self.enemy_shipsButton.setText(_translate("MainWindow", "SHIPS ENEMY"))
