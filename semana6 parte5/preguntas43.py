#Para las siguientes preguntas, toma como referencia el diccionario siguiente y escribe el código necesario para que imprimas lo que se solicita en cada pregunta: 

datosClima = {'lat': 28.5421, 
              'lon': -81.379, 
              'timezone': 'America/New_York', 
              'timezone_offset': -18000, 
              'daily':  [{'dt': '09/Sep/24', 'temp': 26.33,'pressure': 1020, 'humidity': 58}, 
                   {'dt': '10/Sep/24', 'temp': 28.03, 'pressure': 1018, 'humidity': 47}, 
                   {'dt': '11/Sep/24', 'temp': 28.93, 'pressure': 1018, 'humidity': 56}, 
                   {'dt': '12/Sep/24', 'temp': 30.8, 'pressure': 1018, 'humidity': 46}, 
                   {'dt': '13/Sep/24', 'temp': 27.17, 'pressure': 1019, 'humidity': 61}, 
                   {'dt': '14/Sep/24', 'temp': 24.02, 'pressure': 1020, 'humidity': 67}, 
                   {'dt': '17/Sep/24', 'temp': 23.73, 'pressure': 1023, 'humidity': 40}, 
                   {'dt': '18/Sep/24', 'temp': 24.7, 'pressure': 1024, 'humidity': 39}]} 


#¿Cómo puedo obtener la latitud y longitud del lugar registrado en datosClima? 
print(datosClima["lat"])
print(datosClima["lon"])

#¿Imprimir el valor de la presión atmosférica el 11 de septiembre? 
print(datosClima['daily'][2]["pressure"])

#¿Cuál es la humedad relativa el 13 de septiembre? 
print(datosClima['daily'][4]["humidity"])

#¿Cómo accedo a la lista completa de datos diarios (claves 'daily')? 
print(datosClima['daily'])

#¿Cómo obtengo la temperatura registrada el 14 de septiembre? 
print(datosClima['daily'][5]["temp"])

#¿Cuántos elementos hay en la lista 'daily'?  
print(len(datosClima['daily']))
