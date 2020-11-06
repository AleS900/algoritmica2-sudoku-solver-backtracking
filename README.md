# Bactracking - Resolver un Sudoku
Programa realizado en la versión de Python 3.9, el cual tiene la capacidad de resolver un sudoku de una aplicación **Sudoku** para Android, sin importar cual sea esta (El programa actual está configurado para la siguiente [aplicación](https://play.google.com/store/apps/details?id=le.lenovo.sudoku)).<br/>
Se toma un screenshot del juego (se obtiene una imagen de 720x1280), luego se extrae información útil a partir de visión artificial y posteriormente se analiza con un algoritmo de satisfacción de restricciones con backtracking.

## Requisitos Iniciales
-  Tener instalado un [kit de desarrollo](https://www.python.org/downloads/) (**SDK**) de Python, se recomienda la última versión del mismo. 
-  Tener instalado el [sistema de gestión de paquetes **pip**](https://phoenixnap.com/kb/install-pip-windows), utilizado para instalar y administrar paquetes de software escritos en Python.
-  Tener instalado el marco de automatización de pruebas **Gauge** y un **IDE** de preferencia (se sugiere la instalación de **IntelliJ IDEA**), puede encontrar ayuda con la intalación de los mismos [aquí](https://medium.com/automationmaster/installing-gauge-and-intellij-idea-community-edition-287e70635477).
-  Estar seguro de tener [habilitada la opción de adb debbuging](https://developer.android.com/studio/command-line/adb.html#Enabling) en el dispositivo móvil a utilizar.
-  Tener intalada la aplicación de visualización y control de dispositivos vía USB [Scrcpy](https://github.com/Genymobile/scrcpy). 
