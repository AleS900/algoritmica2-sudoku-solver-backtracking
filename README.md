# Bactracking - Resolver un Sudoku
Programa realizado en la versión de Python 3.9, el cual tiene la capacidad de resolver un sudoku de una aplicación **Sudoku** para Android, sin importar cual sea esta (El programa actual está configurado para la siguiente [aplicación](https://play.google.com/store/apps/details?id=le.lenovo.sudoku)).<br/>
Se toma un screenshot del juego (se obtiene una imagen de 720x1280), luego se extrae información útil a partir de visión artificial y posteriormente se analiza con un algoritmo de satisfacción de restricciones con backtracking.<br/>
## Nociones Básicas
Todo el mundo sabe que es un Sudoku y sus reglas básicas, sin embargo presentamos la noción básica del mismo:

-  Un Sudoku es básicamente una cuadrícula de 9x9 casillas dividida en 9 cuadrados de 3x3 casillas.
-  Los valores que puede contener una casilla son 1, 2, 3, 4, 5, 6, 7, 8 o 9.
-  Si una casilla contiene un determinado valor, entonces ninguna de las casillas en la misma columna, fila o cuadrado de 3x3 al que pertenece dicha casilla puede contener ese mismo valor.
-  Si solo hay un valor permitido para una determinada casilla dada su columna, fila o cuadrado al que pertenece, entonces ese valor se asignará a dicha casilla.<br/>
## Requisitos Iniciales
-  Tener instalado un [kit de desarrollo](https://www.python.org/downloads/) (**SDK**) de Python, se recomienda la última versión del mismo.
-  Tener instalado un kit herramientas de desarrollo para la creación de programas en Java[**JDK**](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html).
-  Tener instalado el [sistema de gestión de paquetes **pip**](https://phoenixnap.com/kb/install-pip-windows), utilizado para instalar y administrar paquetes de software escritos en Python.
-  Tener instalado el marco de automatización de pruebas **Gauge** y un **IDE** de preferencia (se sugiere la instalación de **IntelliJ IDEA**), puede encontrar ayuda con la intalación de los mismos [aquí](https://medium.com/automationmaster/installing-gauge-and-intellij-idea-community-edition-287e70635477).
-  Estar seguro de tener [habilitada la opción de adb debbuging](https://developer.android.com/studio/command-line/adb.html#Enabling) en el dispositivo móvil a utilizar.
-  Tener intalada la aplicación de visualización y control de dispositivos vía USB [Scrcpy](https://github.com/Genymobile/scrcpy).
-  Tener instalado (**Tesseract**)[https://github.com/UB-Mannheim/tesseract/wiki], el cual es un motor de reconocimiento de texto que extrae el mismo de imagenes impresas.
-  Agregar a nuestras variables de entorno de Windows todas las _dependencias_ de los anteriores pasos si es que no estuvieran ya configuradas.<br/>
## Ejecutar el Programa
1. Primero clonamos el actual repistorio, o descargamos el mismo como un archivo comprimido.
2. Luego, en nuestro _IDE_ realizamos una busqueda de nuestro achivo y abrimos su ubicación.
3. Realizamos una descarga de las librerias adicionales que se encuentran sitadas en el archivo `requeirments.txt`,a través del comando `pip install<br/>  "Ingresar Rqeuerimiento"`.
4. Verificamos si no existe ningún error de compilación, caso contrario importar todas las librerias que causen algún tipo de conflicto.
5. Conectar el dispositivo android desde el cual se trabajará.
6. Eejcutar el comando `scrcpy` en la carpeta donde se intalo dicho recurso, par poder tener la pantalla del dispositivo en nuestro monitor.
7. Ejecutar el método `main` o ejecutar desde el símbolo de sistema `python ./main.py`.
8. **Opcional**: Si es que se desea la cambiar la aplicación por defecto configurada en el código cambiar los puntos indicados con la palabra `TO_MOD`, asignando a las variables correspondientes los datos indicados.<br/>
## ¿Cómo Funciona?
-   Realiza el análisis del Sudoku con el que se trabajará, verificando primero si este es válido, para luego a través y gracias al uso del Backtracking, solucionar el mismo e imprimirlo en pantalla.<br/>
`main.py`
-   Extrae cada cuadrado de sudoku individualmente y los guarda secuencialmente en una matriz de datos, y ejecutando en el proceso el análisis correpondiente del sudoku y mostrando el resultado en pantalla; **ejecuta todo el programa**.<br/>
`sudoku.py`
