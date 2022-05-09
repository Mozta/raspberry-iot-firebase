import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Configuraciones para conectarme al proyecto firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
# Configuración para conectarme a la BD firestore
db = firestore.client()
sensor_ref = db.collection('sensor')

def read_data():
    sensor = sensor_ref.get()
    for doc in sensor:
        data = doc.to_dict()
        print(f"ID:{doc.id}, DATA:{data['temp']}")

def read_only_data(id):
    data = sensor_ref.document(id).get()
    print(data.to_dict()['created'])
    print(datetime.datetime.now())

def query_data():
    resultado = sensor_ref.where('temp', '==', 29).get()
    for doc in resultado:
        data = doc.to_dict()
        print(f"ID:{doc.id}, DATA:{data['temp']}")

def send_data(temp):
    new_data = {'temp':temp, 'created': datetime.datetime.now()}
    sensor_ref.document().set(new_data)

def delete_data(id):
    sensor_ref.document(id).delete()

def update_data(id):
    sensor_ref.document(id).update({'temp': 18})

# read_data()
# read_only_data('6qNVwvwPCtclJvNmBFoK')
# query_data()
# t = input("Ingresa la temperatura: ")
# send_data(t)
# delete_data('BHEVU7twvsRgqngJDm5m')
update_data('bBbsTO2mb8cn2o4otkmY')