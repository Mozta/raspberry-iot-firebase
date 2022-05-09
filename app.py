from ui_qt import *
import random
import firebase_admin
from firebase_admin import credentials, firestore
import datetime


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.temp = 0
        # Configuraciones para conectarme al proyecto firebase
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        # Configuración para conectarme a la BD firestore
        db = firestore.client()
        self.sensor_ref = db.collection('sensor')
        self.actualizados_ref = db.collection('actualizados').document('data')


        self.pushButton.clicked.connect(self.generar_dato)
        self.pushButton_2.clicked.connect(self.enviar_dato)

    def generar_dato(self):
        self.temp = self.temperatura()
        self.label.setText(str(self.temp)+'º')

    def enviar_dato(self):
        self.send_data(self.temp)
        self.update_data(self.temp)

    def temperatura(self):
        return round(random.uniform(11.0, 27.0), 2)

    def send_data(self,temp):
        new_data = {'temp':temp, 'created': datetime.datetime.now()}
        self.sensor_ref.document().set(new_data)

    def update_data(self,temp):
        self.actualizados_ref.update({'temp': temp})

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()