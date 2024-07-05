from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QFileDialog)
from mainui import Ui_MainWindow
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import sys, re, os, chardet, pickle
import pandas as pd
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.clear_btn.clicked.connect(self.clear_entry)
        self.ui.export_btn.clicked.connect(self.export_data)
        self.ui.check_btn.clicked.connect(self.check_data)

        self.tfidf = TfidfVectorizer(max_features=6000)
        data_loc = os.path.join("data", "Churn_Modelling.csv")
        train_data = self.load_file(data_loc)
        x_train = self.finalize_file(train_data)
        y_train = train_data["Exited"]
        m_path = os.path.join("model", "model.pkl")
        if os.path.isfile(m_path):
            with open(m_path, 'rb') as f:
                self.model = pickle.load(f)
        else:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(x_train, y_train)
            with open(m_path, 'wb') as f:
                pickle.dump(self.model, f)


    def clear_entry(self):
        self.ui.id.clear()
        self.ui.credit_score.clear()
        self.ui.geo.clear()
        self.ui.gender.setCurrentIndex(-1)
        self.ui.age.clear()
        self.ui.tenure.clear()
        self.ui.balance.clear()
        self.ui.no_products.clear()
        self.ui.haveccard.setCurrentIndex(-1)
        self.ui.isactive.setCurrentIndex(-1)
        self.ui.esalary.clear()


    def clean_data(self, df):
        df["Surname"] = df["Surname"].str.lower()
        df["Geography"] = df["Geography"].str.lower()
        df["Gender"] = df["Gender"].str.lower()
        df["Surname"] = df["Surname"].apply(lambda x: re.sub(r'[^\w\s]', "", x))
        return df


    def load_file(self, loc):
        with open(loc, "rb") as f:
            result = chardet.detect(f.read())
            encoding = result["encoding"]

        data = pd.read_csv(loc, delimiter=",", encoding=encoding)
        data = self.clean_data(data)
        return data


    def finalize_file(self, data):
        text_features = data[["Geography", "Gender"]].apply(lambda x: " ".join(x), axis=1)
        text_features_tfidf = self.tfidf.fit_transform(text_features).toarray()
        numerical_features = data[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary"]].values
        x = np.hstack([text_features_tfidf, numerical_features])
        return x


    def export_data(self):
        QMessageBox.information(self, "Bank Customer Churn Predictor", "The data in the .txt or the .csv file should be in the following format: \nRowNumber, CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary")
        sel_file = QFileDialog.getOpenFileName(self, caption="Choose a file", filter="(*.txt *.csv)")
        if sel_file[0] != "":
            data = self.load_file(os.path.normpath(sel_file[0]))
            x_input = self.finalize_file(data)
            y_output = self.model.predict(x_input)
            df = pd.DataFrame(data)
            df.insert(13, "Exit", y_output)
            d = os.path.split(sel_file[0])[0]
            f = os.path.split(sel_file[0])[-1].split(".")
            new_f = "".join(f[:-1]) + "_result." + f[-1]
            df.to_csv(os.path.join(d, new_f))
            QMessageBox.information(self, "Bank Customer Churn Predictor", f"Prediction saved to {new_f}.\n1 means that the customer will exit and 0 means that the customer will not.")


    def check_data(self):
        id = self.ui.id.text().strip()
        credit_score = self.ui.credit_score.text().strip()
        geo = self.ui.geo.text().strip().lower()
        gender = self.ui.gender.currentText().strip().lower()
        age = self.ui.age.text().strip()
        tenure = self.ui.tenure.text().strip()
        balance = self.ui.balance.text().strip()
        no_products = self.ui.no_products.text().strip()
        haveccard = self.ui.haveccard.currentText().strip()
        isactive = self.ui.isactive.currentText().strip()
        esalary = self.ui.esalary.text().strip()

        if (id != "") and (credit_score != "") and (geo != "") and (gender != "") and (age != "") and (tenure != "") and (balance != "") and (no_products != "") and (haveccard != "") and (isactive != "") and (esalary != ""):
            if isactive == "Yes":
                isactive = 1
            else:
                isactive = 0
            if haveccard == "Yes":
                haveccard = 1
            else:
                haveccard = 0

            text_data = [geo, gender]
            text_data = " ".join(text_data)
            text_data_new = self.tfidf.transform([text_data]).toarray()
            numeric_data = np.array([int(credit_score), int(age), int(tenure), int(balance), int(no_products), haveccard, isactive, int(esalary)], dtype=float).reshape(1, -1)

            x_input = np.hstack([text_data_new, numeric_data])
            y_output = self.model.predict(x_input)
            if y_output[0] == 0:
                result = "not exit"
            elif y_output[0] == 1:
                result = "exit"
            else:
                print("error")
            QMessageBox.information(self, "Bank Customer Churn Predictor", f"User with CustomerID: {id} will {result}")
        else:
            QMessageBox.warning(self, "Bank Customer Churn Predictor", "Data not entered")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())