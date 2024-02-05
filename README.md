# python_web

## Manual de uso app.py del proyecto entry_level

En la carpeta **proyecto_flask** está un archivo llamado **app.py**, el cual es un programa que toma dos argumentos: una lista y un entero, cuya idea principal es encontrar, de la lista suministrada, qué par de números al sumarse dan como resultado el objetivo (segundo argumento). A continuación se detalla como utilizarlo y un ejemplo.

### Instrucciones de uso:

La función toma dos argumentos: **lista** y **objetivo**. El primer argumento es una lista de números enteros y el segundo es un número entero. La idea es que de la lista suministrada se extraigan TODAS las parejas de la misma que, al sumarse, den como resultado el número provisto en el segundo argumento, es decir, el ojetivo. 
Por defecto, si no se incluye ningún argumento explícitamente, la lista son los números naturales del 1 al 10 y el objetivo es cinco. La lista debe incluirse como números enteros separados únicamente por comas (sin espacios) y, una vez suministrada la lista, se debe hacer un espacio y escribir el número entero objetivo.

### Ejemplos de uso:

Para ejecutar el programa, se debe ejecturar *python app.py [lista] [objetivo]*; por ejemplo, si quiero saber de los números naturales del 1 al 5, qué pareja de estos al sumarla dan como resultado 3, se debe correr: *python app.py 1,2,3,4,5 3*. Si no se suministra ningún argumento y se ejecuta únicamente *python app.py*, se obtiene como resultado las parejas de los números naturales del 1 al 10 que al sumarse dan como resultado 5.

