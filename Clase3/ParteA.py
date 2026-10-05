#A5
#Una imagen es el molde: el programa con todo lo que necesita (Python, librerías, archivos), 
# empaquetado y quieto. Un contenedor es lo que sale de ese molde cuando lo ponés a correr, 
# y de una imagen pueden salir muchos.
#Docker resuelve el "en mi máquina anda" porque el programa viaja con su propio entorno 
# adentro de la caja, así que no depende de lo que tenga instalado cada máquina.
#El venv solo aislaba las librerías de Python; no aislaba la versión de Python 
#(yo tengo 3.14 y el contenedor 3.12), ni el sistema operativo, ni programas que no 
#son de Python, como una base de datos o un broker.