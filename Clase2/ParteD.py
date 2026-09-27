#D2
#El primer mensaje no aparece al suscribirte después.
#El segundo mensaje sí aparece porque ya estás suscripto cuando se publica.
#Por defecto, MQTT no guarda los mensajes para los suscriptores que se conecten más tarde.

#D3
#En una API con request/response, un cliente realiza una petición y espera una respuesta 
# del servidor. Por ejemplo, una aplicación pide GET /libros y la API devuelve la lista. 
# En MQTT, un publisher publica un mensaje en un topic y el broker lo distribuye a los 
# suscriptores de ese topic, sin que el publisher tenga que conocerlos. La API sirve 
# cuando necesitás pedir un dato o ejecutar una operación concreta; MQTT sirve cuando 
# querés distribuir eventos o mediciones a varios consumidores.

#D4
#Alguien que quiere recibir todo lo que se publique directamente en la cocina puede 
#suscribirse a: casa/cocina/+
#Un wildcard es un comodín que permite suscribirse a varios topics que coinciden con un patrón.
# + reemplaza un solo nivel del topic.
# # representa todos los niveles restantes, y se usa al final del filtro.

#D5
#casa/cocina/temperatura
# casa/cocina/humedad

# casa/dormitorio/temperatura
# casa/dormitorio/humedad

# casa/living/temperatura
# casa/living/humedad

#Recibir todo de la casa:  casa/#

#Recibir todo de la cocina:  casa/cocina/#

#Recibir temperatura de todos los ambientes:  casa/+/temperatura

#Recibir todos los sensores de un ambiente:  casa/living/+

#D6

#QoS0:  Se intenta entregar una vez, sin confirmación ni garantía de entrega.

#QoS1:  Se garantiza que llegue al menos una vez, pero puede llegar duplicado.

#QoS2:  Se garantiza que llegue exactamente una vez, usando un intercambio más complejo.

#Sensor de temperatura cada 2 segundos:
#Para un sensor que publica continuamente, podría usarse QoS 0 si perder una medición 
# ocasional no es grave. La siguiente lectura llegará poco después y puede reemplazar a 
# la anterior.

#Comando de abrir una puerta:
#Para un comando puntual que no debería perderse, convendría considerar QoS 1 o QoS 2. 
#QoS 1 permite duplicados, por lo que la aplicación debe contemplar ese caso. QoS 2 
#evita duplicados en la entrega MQTT, aunque la lógica del sistema también debe manejar 
#correctamente la ejecución del comando.

#D7

#Un mensaje retained es un mensaje que el broker conserva como el último mensaje retenido 
#de un topic.
#Si un sensor publica:
#Topic: casa/cocina/temperatura
#Mensaje: 23.5
#Retained: true
#Y después alguien se suscribe a casa/cocina/temperatura, el broker le envía el último 
# mensaje retenido, aunque se haya publicado antes de la suscripción.
#Sin retained: el suscriptor que llega tarde no recibe el mensaje anterior.
#Con retained: el broker le entrega el último mensaje retenido del topic al nuevo suscriptor.
#Esto es útil para conocer el último estado conocido de un sensor, por ejemplo, la 
# temperatura actual registrada, sin tener que esperar a que el sensor vuelva a publicar.

#D8
#En polling, cada cliente pregunta periódicamente a una API si hay novedades. En MQTT, 
# el dispositivo publica un evento y el broker lo distribuye a los suscriptores.
#Supongamos que tenemos 1000 sensores y cada uno consulta la API una vez por segundo:
#1000 sensores ×1 consulta/segundo = 1000 consultas/segundo
#En un minuto serían:
#1000×60=60000 consultas
#Aunque no haya ocurrido ningún cambio, las consultas siguen llegando.
#Con MQTT, si cada sensor publica cuando tiene un dato nuevo, el broker distribuye esos 
# mensajes a quienes estén suscriptos. No hace falta que cada consumidor consulte 
# continuamente si apareció algo.
#Demora:
#En polling cada un segundo, un evento puede tardar casi un segundo en ser detectado, según 
#cuándo ocurra respecto de la próxima consulta.
#En MQTT, el mensaje se distribuye cuando se publica, sin esperar a la próxima consulta 
#periódica.
#Conclusión: MQTT puede reducir las consultas innecesarias y la demora de detección para 
#muchos sensores, especialmente cuando los consumidores solo necesitan recibir novedades.