import json
import requests



class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad_2025/static/"

    def leer_api(self,url):
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self):
        pass


# vamos a crear una instancia de la clase
ingestion = Ingestiones()
datos_json =ingestion.leer_api("https://api.artic.edu/api/v1/artworks")
print("esta es la ruta estatica :",ingestion.ruta_static)
print("datos json:",datos_json)



        
    