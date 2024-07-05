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
        MainWindow.setFixedSize(349, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.haveccard = QComboBox(self.centralwidget)
        self.haveccard.addItem("")
        self.haveccard.addItem("")
        self.haveccard.setObjectName(u"haveccard")
        sizePolicy.setHeightForWidth(self.haveccard.sizePolicy().hasHeightForWidth())
        self.haveccard.setSizePolicy(sizePolicy)
        self.haveccard.setFont(font)

        self.gridLayout.addWidget(self.haveccard, 8, 1, 1, 1)

        self.esalary = QLineEdit(self.centralwidget)
        self.esalary.setObjectName(u"esalary")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.esalary.sizePolicy().hasHeightForWidth())
        self.esalary.setSizePolicy(sizePolicy1)
        self.esalary.setFont(font)

        self.gridLayout.addWidget(self.esalary, 10, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.balance = QLineEdit(self.centralwidget)
        self.balance.setObjectName(u"balance")
        sizePolicy1.setHeightForWidth(self.balance.sizePolicy().hasHeightForWidth())
        self.balance.setSizePolicy(sizePolicy1)
        self.balance.setFont(font)

        self.gridLayout.addWidget(self.balance, 6, 1, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.credit_score = QLineEdit(self.centralwidget)
        self.credit_score.setObjectName(u"credit_score")
        sizePolicy1.setHeightForWidth(self.credit_score.sizePolicy().hasHeightForWidth())
        self.credit_score.setSizePolicy(sizePolicy1)
        self.credit_score.setFont(font)

        self.gridLayout.addWidget(self.credit_score, 1, 1, 1, 1)

        self.id = QLineEdit(self.centralwidget)
        self.id.setObjectName(u"id")
        sizePolicy1.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy1)
        self.id.setFont(font)

        self.gridLayout.addWidget(self.id, 0, 1, 1, 1)

        self.geo = QLineEdit(self.centralwidget)
        self.geo.setObjectName(u"geo")
        sizePolicy1.setHeightForWidth(self.geo.sizePolicy().hasHeightForWidth())
        self.geo.setSizePolicy(sizePolicy1)
        self.geo.setFont(font)

        self.gridLayout.addWidget(self.geo, 2, 1, 1, 1)

        self.check_btn = QPushButton(self.centralwidget)
        self.check_btn.setObjectName(u"check_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.check_btn.sizePolicy().hasHeightForWidth())
        self.check_btn.setSizePolicy(sizePolicy2)
        self.check_btn.setFont(font)

        self.gridLayout.addWidget(self.check_btn, 13, 0, 1, 2)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.gender = QComboBox(self.centralwidget)
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.setObjectName(u"gender")
        sizePolicy.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy)
        self.gender.setFont(font)

        self.gridLayout.addWidget(self.gender, 3, 1, 1, 1)

        self.no_products = QLineEdit(self.centralwidget)
        self.no_products.setObjectName(u"no_products")
        sizePolicy1.setHeightForWidth(self.no_products.sizePolicy().hasHeightForWidth())
        self.no_products.setSizePolicy(sizePolicy1)
        self.no_products.setFont(font)

        self.gridLayout.addWidget(self.no_products, 7, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.export_btn = QPushButton(self.centralwidget)
        self.export_btn.setObjectName(u"export_btn")
        sizePolicy2.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy2)
        self.export_btn.setFont(font)

        self.gridLayout.addWidget(self.export_btn, 12, 0, 1, 2)

        self.age = QLineEdit(self.centralwidget)
        self.age.setObjectName(u"age")
        sizePolicy1.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy1)
        self.age.setFont(font)

        self.gridLayout.addWidget(self.age, 4, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.tenure = QLineEdit(self.centralwidget)
        self.tenure.setObjectName(u"tenure")
        sizePolicy1.setHeightForWidth(self.tenure.sizePolicy().hasHeightForWidth())
        self.tenure.setSizePolicy(sizePolicy1)
        self.tenure.setFont(font)

        self.gridLayout.addWidget(self.tenure, 5, 1, 1, 1)

        self.isactive = QComboBox(self.centralwidget)
        self.isactive.addItem("")
        self.isactive.addItem("")
        self.isactive.setObjectName(u"isactive")
        sizePolicy.setHeightForWidth(self.isactive.sizePolicy().hasHeightForWidth())
        self.isactive.setSizePolicy(sizePolicy)
        self.isactive.setFont(font)

        self.gridLayout.addWidget(self.isactive, 9, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy2.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy2)
        self.clear_btn.setFont(font)

        self.gridLayout.addWidget(self.clear_btn, 11, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.haveccard.setCurrentIndex(-1)
        self.gender.setCurrentIndex(-1)
        self.isactive.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)

        self.centralwidget.setTabOrder(self.id, self.credit_score)
        self.centralwidget.setTabOrder(self.credit_score, self.geo)
        self.centralwidget.setTabOrder(self.geo, self.gender)
        self.centralwidget.setTabOrder(self.gender, self.age)
        self.centralwidget.setTabOrder(self.age, self.tenure)
        self.centralwidget.setTabOrder(self.tenure, self.balance)
        self.centralwidget.setTabOrder(self.balance, self.no_products)
        self.centralwidget.setTabOrder(self.no_products, self.haveccard)
        self.centralwidget.setTabOrder(self.haveccard, self.isactive)
        self.centralwidget.setTabOrder(self.isactive, self.esalary)
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

