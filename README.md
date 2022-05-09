
# raspberry-iot-firebase

## Arquitecturas Programables Avanzadas
Aplicación de escritorio para la Raspberry Pi, escrita en Python.
Interfaz creada en QT Designer.
Base de datos en Firestore, Firebase


## Instalación
Requerimientos:
- Entorno virtual (venv)
- Python 3.9
- pip 22.0.4
- PyQt5==5.15.6
- firebase-admin==5.2.0

### Entorno de Desarrollo

1. Crear entorno virtual (_venv_)
```shell script 
python -m venv venv
```
2. Activar entorno virtual
```shell script
source venv/bin/activate
```
3. Instalar bibliotecas
```shell script
(venv) pip install -r app/requirements.txt
```
4. Ejecutar la aplicación
```shell script
(venv) python app.py
```

# Notes
Deberás colocar tu archivo json de configuraciones de firebase en la carpeta del proyecto