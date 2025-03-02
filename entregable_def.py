import requests
import json

#URL de la API
url = "https://extinct-api.herokuapp.com/api/v1/animal/"

# Hacer la solicitud GET  a la API
response = requests.get(url)

#verificar si la solicitud fue exitosa (codigo 200)
if response.status_code == 200 :
    # Convertir la respuesta a un objeto python
    data = response.json

    # Escribir la respuesta en un archivo JSON 
    with open("extinct.json", "w") as file:
        json.dump(data, file, indent=4)
    print("datos guardados en extint.json")
    




