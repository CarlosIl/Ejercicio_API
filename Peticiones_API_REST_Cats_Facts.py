import json
from pathlib import Path
import requests
import os
#direccion API publica que vamos a utilizar
# https://alexwohlbruck.github.io/cat-facts/docs/
try:
    def menu():
        os.system('cls')
        print("Selecciona una opcion:")
        print("\t1 - Muestra uno o varios datos al azar de uno de los animales disponibles")
        print("\t2 - Visualiza un dato a partir de su ID")
        print("\t3 - Listado de todos los datos")
        print("\t4 - Salir")
        opcion=int(input("Selecciona una opcion : "))
        return (opcion)
    def datos_al_azar():
        animal=input("Introduce el nombre de uno de los animales disponibles (cat,dog,snail,horse): ")
        n_datos=int(input("Introduce el numero de datos que quieres recibir (Máx:100): ")) 
        api_address="https://cat-fact.herokuapp.com/facts/random?animal_type=%s&amount=%i" %(animal,n_datos)

        resp = requests.get(api_address)
        if resp.status_code==200:
           
            json_data=json.loads(resp.content)
            print(json_data)

    def datos_por_identificador():
        #Para probar: 59669484bf604b00205c20e3
        ID=input ("Introduce el ID del dato: ")
        api_address="https://cat-fact.herokuapp.com/facts/%s"%ID
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            print(json_data)
                   
    def listado_datos():
        api_address="https://cat-fact.herokuapp.com/facts"
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            print(json_data)

    while True:
        opcion=menu()
        if opcion==1:
            datos_al_azar()
        elif opcion==2:
            datos_por_identificador()
        elif opcion==3:
            listado_datos()
        elif opcion==4:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")