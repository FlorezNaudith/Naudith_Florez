import requests
import json

#URL de la API
url = "https://api.artic.edu/api/v1/artworks"

# Hacer la solicitud GET  a la API
response = requests.get(url)

#verificar si la solicitud fue exitosa (codigo 200)
if response.status_code == 200 :
    # Convertir la respuesta a un objeto python
    data = response.json

    # Escribir la respuesta en un archivo JSON 
    with open("art_institute_of_chicago.json", "w") as file:
        json.dump(data, file, indent=4)
    print("datos guardados en art_institute_of_chicago.json")
    




