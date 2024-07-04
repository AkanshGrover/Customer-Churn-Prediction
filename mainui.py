from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(353, 369)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.id = QLineEdit(self.centralwidget)
        self.id.setObjectName(u"id")

        self.credit_score = QLineEdit(self.centralwidget)
        self.credit_score.setObjectName(u"credit_score")

        self.geo = QLineEdit(self.centralwidget)
        self.geo.setObjectName(u"geo")

        self.gender = QComboBox(self.centralwidget)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")

        self.age = QLineEdit(self.centralwidget)
        self.age.setObjectName(u"age")

        self.tenure = QLineEdit(self.centralwidget)
        self.tenure.setObjectName(u"tenure")

        self.balance = QLineEdit(self.centralwidget)
        self.balance.setObjectName(u"balance")

        self.no_products = QLineEdit(self.centralwidget)
        self.no_products.setObjectName(u"no_products")

        self.haveccard = QComboBox(self.centralwidget)
        self.haveccard.addItem("")
        self.haveccard.addItem("")
        self.haveccard.setObjectName(u"haveccard")

        self.isactive = QComboBox(self.centralwidget)
        self.isactive.addItem("")
        self.isactive.addItem("")
        self.isactive.setObjectName(u"isactive")

        self.esalary = QLineEdit(self.centralwidget)
        self.esalary.setObjectName(u"esalary")

        self.gridLayout.addWidget(self.haveccard, 8, 1, 1, 1)

        self.gridLayout.addWidget(self.esalary, 10, 1, 1, 1)

        self.check_btn = QPushButton(self.centralwidget)
        self.check_btn.setObjectName(u"check_btn")

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.balance, 6, 1, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.gridLayout.addWidget(self.credit_score, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.id, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.geo, 2, 1, 1, 1)

        self.gridLayout.addWidget(self.check_btn, 13, 0, 1, 2)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.gridLayout.addWidget(self.gender, 3, 1, 1, 1)

        self.gridLayout.addWidget(self.no_products, 7, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.export_btn = QPushButton(self.centralwidget)
        self.export_btn.setObjectName(u"export_btn")

        self.gridLayout.addWidget(self.export_btn, 12, 0, 1, 2)

        self.gridLayout.addWidget(self.age, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.gridLayout.addWidget(self.tenure, 5, 1, 1, 1)

        self.gridLayout.addWidget(self.isactive, 9, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.gridLayout.addWidget(self.clear_btn, 11, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.haveccard.setCurrentIndex(-1)
        self.gender.setCurrentIndex(-1)
        self.isactive.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bank Customer Churn Predictor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter credit score:", None))
        self.haveccard.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.haveccard.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.haveccard.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an option", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter customerID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter geography:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Is active:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Have credit card:", None))
        self.check_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Estimated salary:", None))
        self.gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an option", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter tenure:", None))
        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"Export data from a file", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter age:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enter number of products:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter gender:", None))
        self.isactive.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.isactive.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.isactive.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an option", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter balance:", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

