import time
import sys
# Definición de la función global
def pausa(segundos):
    print(f"Pausa de {segundos} segundos...")
    import time
    time.sleep(segundos)

# Puedes llamar a la función desde cualquier parte del programa
print("Inicio del programa.")

print("Después de la pausa.")
print ("""
Se acaba de correr una carrera de F1 de 52 vueltas. Sabemos que corrieron a lo sumo 20 pilotos.
Los datos estan cargados en un diccionario en donde el nombre del piloto es la clave a la que se le asocian tres valores
enteros que representan la duración de la carrera, la de la vuelta mas rapida y la cantidad de vueltas que realizó,
respectivamente.

Los dos primeros datos estan dados en segundos
Ejemplo:
    Hamilton,   6115,113,52
    Vettel,     4720,112,40

Significa que Hamilton completé la carrera en 6115 segundos, su vuelta mas rapida fue de 113 segundos y finaliz6 la
carrera ya que hizo las 52 vueltas. Vettel tuvo su vuelta mas rapida en 112 segundos pero no finalizé la carrera, ya que
completé solo 40 vueltas

    'Se proporsionan los datos en un diccionario con listas como valores.'
    'tranformalo en un dicionario con otro diccionario anidado' en base a la aux
Ej
    origen <clave>:    <    lista   >  pasar a < clave > :<                              valor                                               >
                                                          {  <sub clave 1         :val 1>,<sub clave 2       :val 1>,<sub clave 3      :val 3>
          {"Hamilton":[6115, 113, 52], ====>  "Hamilton": {"tiempo_Total en pista":6115  ,"vuelta Mas Rapida":113   ,"total de vueltas":52    },
           "Bottas":  [3610, 115, 30], ====>  "Bottas":   {"tiempo_Total en pista":3610  ,"vuelta Mas Rapida":115   ,"total de vueltas":30    },

cada_clave='Hamilton'
                tiempo_Total en pista=6115
                vuelta Mas Rapida=113
                total de vueltas=52

0) Estructura de datos:
1) Manupulacion de datos:
    A)Hay dos listas de los pilotos que abandonaro y los que no.

    B) Quien gano, con que tiempos de vuelta y totales

    C) Generación del dicionario del podio
    podio= {
            "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}
            }

    D) Generacipon del dicionario de los 3 pilotos mas rápidos
    piloto_mas_rapido= {
                        "Apellido1":puntos1,
                        "Apellido2":puntos2,
                        "Apellido3":puntos3,
                        }

    E) Generación del diccionario de puntage obtenido por cada piloto: puntaje.
    Para simplificar, solo reciben puntos los pilotos que hayan finalizado la carrera,
    salvo que sea el piloto que hizo la vuelta mas rapida quien recibirá un punto extra haya o no finalizado la carrera.
    datos:
            puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    En base a la lista de puntos por posición (el primero 25, el segundo 18, etc.)
2) Escuderías
    F) Puntos por escuderia
    G) Podio escuderia
3)  Menu con opciones y colores
4)  Guardado dic_general en Excel y BBDD 
""")


CANTIDAD_DE_VUELTAS = 52# CONSTANTE
pilotos = [ "Alexander Albon",
             "Carlos Sainz",
             "Charles Leclerc",
             "Esteban Ocon",
             "Fernando Alonso",
             "Gabriel Bortoleto",
             "George Russell",
             "George Russell",
             "Isack Hadjar",
             "Jack Doohan",
             "Kimi Antonelli",
             "Lance Stroll",
             "Lando Norris",
             "Lewis Hamilton",
             "Liam Lawson",
             "Max Verstappen",
             "Nico Hulkenberg",
             "Oliver Bearman",
             "Oscar Piastri",
             "Pierre Gasly",
             "Yuki Tsunoda"]# tiene un error


tiempos= [        [1417, 13, 86],
                  [1482, 13, 94],
                  [5408, 52, 81],
                  [ 708,  6, 79],
                  [ 222,  2,102],
                  [5355, 45, 93],
                  [4935, 47, 89],
                  [4935, 47, 8],
                  [5616, 52, 98],
                  [5980, 52, 91],
                  [5512, 52, 85],
                  [3600, 30, 98],
                  [5304, 52, 90],
                  [5564, 52, 94],
                  [6084, 52, 87],
                  [5200, 52, 85],
                  [6032, 52, 91],
                  [5720, 52, 88],
                  [5356, 52, 87],
                  [5876, 52, 88],
                  [5824, 52, 92]      ]#tiene un error

pilotos_escuderias=[    
            "PIERRE GASLY"      ,	"ALPINE",		10,
            "JACK DOOHAN"       ,	"ALPINE",		7,
            "FERNANDO ALONSO"   ,	"ASTON MARTIN",	14,
            "LANCE STROLL"      ,	"ASTON MARTIN",	18,
            "LEWIS HAMILTON"    ,	"FERRARI",		44,
            "CHARLES LECLERC"   ,	"FERRARI",		16,
            "ESTEBAN OCON"      ,	"HAAS",			31,
            "OLIVER BEARMAN"    ,	"HAAS",			87,
            "NICO HULKENBERG"   ,	"KICK SAUBER",	27,
            "GABRIEL BORTOLETO" ,	"KICK SAUBER",	5,
            "LANDO NORRIS"      ,	"MCLAREN",		81,
            "OSCAR PIASTRI"     ,	"MCLAREN",		4,
            "GEORGE RUSSELL"    ,	"MERCEDES",		63,
            "KIMI ANTONELLI"    ,	"MERCEDES",		12,
            "LIAM LAWSON"       ,	"RACING BULL",	30,
            "ISACK HADJAR"      ,	"RACING BULL",	6,
            "MAX VERSTAPPEN"    ,	"RED BULL",		1,
            "YUKI TSUNODA"      ,	"RED BULL",		22,
            "CARLOS SAINZ"      ,	"WILLIAMS",		55,
            "ALEXANDER ALBON"   ,	"WILLIAMS",		23	]

aux =  "tiempo total en pista", "total de vueltas", "vuelta mas rapida"
########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
def terminaron():
    """
    📊 Clasifica a los pilotos en dos listas:
    👉 pilotos_si_terminaron: quienes completaron las 52 vueltas.
    👉 pilotos_no_terminaron: quienes no lo lograron.
    ✅ Muestra los datos de cada piloto.
    """
    # ~ global pilotos_si_terminaron
    # ~ global pilotos_no_terminaron
    
    pilotos_si_terminaron = []
    pilotos_no_terminaron = []
    print (f"📋 Lista de pilotos: {pilotos}")
    print (f"⏱️ Lista de tiempos: {tiempos}")
    print (f"📑 Lista de aux: {aux}")
    
    for piloto,(datos) in zip(pilotos,tiempos):
        print (f"""el piloto {piloto} tiene los siguientes datos :
        {aux[0]}= {datos[0]} 
        {aux[1]}= {datos[1]} vueltas completas 
        {aux[2]}= {datos[2]} segundos
        {"-"*100}
        """)
        if datos[1]== 52:
            pilotos_si_terminaron.append(piloto)
        else:
            pilotos_no_terminaron.append(piloto)
    
    # ~ return 
    return (pilotos_si_terminaron, pilotos_no_terminaron) # empaqueto en tupla


# ~ tupla_de_regreso = terminaron ()
# ~ print (f"""
# ~ {tupla_de_regreso=}
# ~ {type(tupla_de_regreso)=}
# ~ """)
# ~ pilotos_si_terminaron, pilotos_no_terminaron = tupla_de_regreso


pilotos_si_terminaron, pilotos_no_terminaron = terminaron ()# desempaquetar

print ("*"*100)
print (f"los pilotos que terminaron la carrera fueron :{pilotos_si_terminaron}")
print (f"los pilotos que no terminaron la carrera fueron :{pilotos_no_terminaron}")





########################################################################
dic_general=dict()
dic_escuderias={}
def estruc_dic():
    """
    🗃️ Estructura el diccionario principal `dic_general` a partir de las listas
    de pilotos, tiempos y escuderías.

    🚗 Usa `dic_escuderias` para asociar escudería y número de piloto.
    
    📊 Añade campos:
    - tiempo total en pista
    - vuelta más rápida
    - total de vueltas
    - escudería
    - número
    - puntos
    """
    
    
    
    for piloto,(datos) in zip(pilotos,tiempos):
        
        
        indice     = pilotos_escuderias.index(piloto.upper())
        escuderia  = pilotos_escuderias[indice+1]
        numero     = pilotos_escuderias[indice+2]
        
        
        
        dic_general[piloto]= {
                                aux[0]          :   datos[0], 
                                aux[1]          :   datos[1], 
                                aux[2]          :   datos[2],
                                "Escuderia"     :   escuderia.title(),
                                "Numero"        :   numero,
                                "Puntos"        :   0
                                }
    
    """
    {'Alexander Albon': [1417, 13, 86], 'Carlos Sainz': [1482, 13, 94], 'Charles Leclerc': [5408, 52, 81], 'Esteban Ocon': [708, 6, 79], 'Fernando Alonso': [222, 2, 102], 'Gabriel Bortoleto': [5355, 45, 93], 'George Russell': [4935, 47, 8], 'Isack Hadjar': [5616, 52, 98], 'Jack Doohan': [5980, 52, 91], 'Kimi Antonelli': [5512, 52, 85], 'Lance Stroll': [3600, 30, 98], 'Lando Norris': [5304, 52, 90], 'Lewis Hamilton': [5564, 52, 94], 'Liam Lawson': [6084, 52, 87], 'Max Verstappen': [5200, 52, 85], 'Nico Hulkenberg': [6032, 52, 91], 'Oliver Bearman': [5720, 52, 88], 'Oscar Piastri': [5356, 52, 87], 'Pierre Gasly': [5876, 52, 88], 'Yuki Tsunoda': [5824, 52, 92]}
    {'Alexander Albon': {'tiempo total en pista': 1417, 'total de vueltas': 13, 'vuelta mas rapida': 86, 'Escuderia': 'WILLIAMS', 'Numero': 23}, 'Carlos Sainz': {'tiempo total en pista': 1482, 'total de vueltas': 13, 'vuelta mas rapida': 94, 'Escuderia': 'WILLIAMS', 'Numero': 55}, 'Charles Leclerc': {'tiempo total en pista': 5408, 'total de vueltas': 52, 'vuelta mas rapida': 81, 'Escuderia': 'FERRARI', 'Numero': 16}, 'Esteban Ocon': {'tiempo total en pista': 708, 'total de vueltas': 6, 'vuelta mas rapida': 79, 'Escuderia': 'HAAS', 'Numero': 31}, 'Fernando Alonso': {'tiempo total en pista': 222, 'total de vueltas': 2, 'vuelta mas rapida': 102, 'Escuderia': 'ASTON MARTIN', 'Numero': 14}, 'Gabriel Bortoleto': {'tiempo total en pista': 5355, 'total de vueltas': 45, 'vuelta mas rapida': 93, 'Escuderia': 'KICK SAUBER', 'Numero': 5}, 'George Russell': {'tiempo total en pista': 4935, 'total de vueltas': 47, 'vuelta mas rapida': 8, 'Escuderia': 'MERCEDES', 'Numero': 63}, 'Isack Hadjar': {'tiempo total en pista': 5616, 'total de vueltas': 52, 'vuelta mas rapida': 98, 'Escuderia': 'RACING BULL', 'Numero': 6}, 'Jack Doohan': {'tiempo total en pista': 5980, 'total de vueltas': 52, 'vuelta mas rapida': 91, 'Escuderia': 'ALPINE', 'Numero': 7}, 'Kimi Antonelli': {'tiempo total en pista': 5512, 'total de vueltas': 52, 'vuelta mas rapida': 85, 'Escuderia': 'MERCEDES', 'Numero': 12}, 'Lance Stroll': {'tiempo total en pista': 3600, 'total de vueltas': 30, 'vuelta mas rapida': 98, 'Escuderia': 'ASTON MARTIN', 'Numero': 18}, 'Lando Norris': {'tiempo total en pista': 5304, 'total de vueltas': 52, 'vuelta mas rapida': 90, 'Escuderia': 'MCLAREN', 'Numero': 81}, 'Lewis Hamilton': {'tiempo total en pista': 5564, 'total de vueltas': 52, 'vuelta mas rapida': 94, 'Escuderia': 'FERRARI', 'Numero': 44}, 'Liam Lawson': {'tiempo total en pista': 6084, 'total de vueltas': 52, 'vuelta mas rapida': 87, 'Escuderia': 'RACING BULL', 'Numero': 30}, 'Max Verstappen': {'tiempo total en pista': 5200, 'total de vueltas': 52, 'vuelta mas rapida': 85, 'Escuderia': 'RED BULL', 'Numero': 1}, 'Nico Hulkenberg': {'tiempo total en pista': 6032, 'total de vueltas': 52, 'vuelta mas rapida': 91, 'Escuderia': 'KICK SAUBER', 'Numero': 27}, 'Oliver Bearman': {'tiempo total en pista': 5720, 'total de vueltas': 52, 'vuelta mas rapida': 88, 'Escuderia': 'HAAS', 'Numero': 87}, 'Oscar Piastri': {'tiempo total en pista': 5356, 'total de vueltas': 52, 'vuelta mas rapida': 87, 'Escuderia': 'MCLAREN', 'Numero': 4}, 'Pierre Gasly': {'tiempo total en pista': 5876, 'total de vueltas': 52, 'vuelta mas rapida': 88, 'Escuderia': 'ALPINE', 'Numero': 10}, 'Yuki Tsunoda': {'tiempo total en pista': 5824, 'total de vueltas': 52, 'vuelta mas rapida': 92, 'Escuderia': 'RED BULL', 'Numero': 22}}
    """
    print (f"{dic_general=}")
    # ~ return dic_general
# ~ dic_general = estruc_dic()
estruc_dic()
########################################################################
def ver_datos_dic(**dic):
    for clave, valor in dic.items():
        print(f"📌 {clave}") 
        if isinstance(valor, dict):
            for sub_clave, sub_valor in valor.items():
                print (f"    ➤ {sub_clave.ljust(25)}:   {str(sub_valor).ljust(20)}     ({type(sub_valor).__name__})") 
        elif isinstance(valor, (list,tuple,set) ):
            for indice, sub_valor in enumerate(valor):
                print (f"    ➤ {indice}                 {str(sub_valor).ljust(20)}     ({type(sub_valor).__name__})")  
        else:
            print (f"{valor}") 
        print (f"{'-'*100} ") 
        

print ("*"*100)
ver_datos_dic(**dic_general)


########################################################################
def buscar_piloto_ganador(dic_general):
    """
    🥇 Busca al piloto que ganó la carrera:
    - Que haya completado las 52 vueltas.
    - Con menor tiempo total en pista.

    📤 Devuelve su nombre.
    """
    # Inicializo el tiempo mínimo como infinito
        
    menor = float("inf")
    piloto_ganador = None

    # Recorro todos los pilotos en el diccionario
    """
    for piloto_nombre, valor in dic_general.items():
        # Solo evaluamos pilotos que completaron la carrera
        # ~ if valor["total de vueltas"] == 52 and valor["tiempo total en pista"] < menor:
        if valor[aux[1]] == 52 and valor[aux[0]] < menor:
    """
    for piloto_nombre in dic_general.keys():
        if dic_general[piloto_nombre][aux[1]] == 52 and dic_general[piloto_nombre][aux[0]] < menor:
            
            menor = dic_general[piloto_nombre][aux[0]]
            piloto_ganador = piloto_nombre
    
    return piloto_ganador
piloto_ganador = buscar_piloto_ganador(dic_general)

print ("-"*100)
print (f"""
🥇 El piloto ganador es {piloto_ganador}
    🔁 {dic_general[piloto_ganador][aux[1]] =}
    ⚡ {dic_general[piloto_ganador][aux[2]] =}
    ️⏱️ {dic_general[piloto_ganador][aux[0]] =}
""")
print ("*"*100)

########################################################################
def buscar_pilotos_podio(dic_general,podio):
    """
    🏆 Busca los tres primeros pilotos (podio) por menor tiempo total en pista
    de quienes completaron las 52 vueltas.

    📥 Modifica el diccionario `podio` recibido como parámetro.
    """
    
    for clave in podio.keys():
        menor = float("inf")
        for piloto_nombre, valor in dic_general.items():
            if valor ["total de vueltas"] ==52 \
                and valor["tiempo total en pista"] < menor \
                and piloto_nombre not in  podio.values():
                menor = valor["tiempo total en pista"]
                podio[clave] = piloto_nombre
    return 
podio= {
     "primer puesto" : "",
     "segundo puesto":"",
     "tercer puesto" :""
        }
    
buscar_pilotos_podio(dic_general,podio)

print("-" * 100)
print("🏆 P O D I O   F Ó R M U L A   1 - 2 0 2 5 🏆".center(100))
print("-" * 100)

for puesto, piloto in podio.items():
    datos = dic_general[piloto]
    print(f"""
🥇 {puesto.upper()}
    👤 Piloto:              {piloto}
    ⏱️ Tiempo total:        {datos['tiempo total en pista']} s
    ⚡ Vuelta más rápida:   {datos['vuelta mas rapida']} s
    🔁 Vueltas completadas: {datos['total de vueltas']}
    """)
print("-" * 100)



########################################################################
def buscar_pilotos_puntos(*puntos, **dic_general):#   *lista o tupla  **dict
    """
    Busca los pilotos que reciben puntos según el tiempo total en pista.
    Devuelve una lista con los nombres de los pilotos que completaron 52 vueltas
    y tienen los tiempos más bajos.

    🎖️ Asigna puntos a los pilotos según su posición (orden de llegada)
    de quienes completaron las 52 vueltas.
    
    Parámetros:
    📥 entrada: lista de puntos por posición.
    📥 dic_general: diccionario con datos de pilotos.
    entrada: puntos asignados a cada posición (ej. 25, 18, 15, ...)
    dic_general: diccionario con los datos de los pilotos
    
    Retorna:
    📤 Devuelve lista ordenada de pilotos con puntos asignados.
    lista con los nombres de los pilotos en orden según los puntos.
    """
    puntos_por_orden_llegada = []
    # Inicializar los puntos de los pilotos a cero
    # ~ for piloto in dic_general.keys():
        # ~ dic_general[piloto]["Puntos"] = 0
    
    for puntos_obtenidos in puntos:
        menor_tiempo_total_en_pista = float("inf")
        piloto_con_puntos = None
        
        for piloto in dic_general.keys():
            if (dic_general[piloto]['total de vueltas'] == 52 and
                dic_general[piloto]['tiempo total en pista'] < menor_tiempo_total_en_pista and
                piloto not in puntos_por_orden_llegada):
                
                menor_tiempo_total_en_pista = dic_general[piloto]['tiempo total en pista']
                piloto_con_puntos = piloto  # Cambié de piloto_puntos a piloto_con_puntos
        
        if piloto_con_puntos:  # Asegúrate de que hay un piloto ganador
            puntos_por_orden_llegada.append(piloto_con_puntos)
            dic_general[piloto_con_puntos]["Puntos"] += puntos_obtenidos  # Acumular puntos al piloto ganador
            
    return puntos_por_orden_llegada
    dic_puntos = dict(fromkeys(puntos))
    

# Lista de puntos según el lugar (ej. primero, segundo, tercero)
puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
puntos_por_orden_llegada = buscar_pilotos_puntos(*puntos, **dic_general)

print("-" * 100)
print("🏁  RESULTADO FINAL DEL GRAN PREMIO 🏁\n")
for index, (puntos, piloto) in enumerate(zip(puntos, puntos_por_orden_llegada)):
    print(f"Piloto en {index + 1} lugar con {puntos} puntos = {piloto}\n{dic_general[piloto]}\n")
print ("-"*50)
print(f"{puntos_por_orden_llegada=}")
print(f"{dic_general=}")
print ("-"*50)

ver_datos_dic(**dic_general)

print("*"*100)

########################################################################
def vuelta_mas_rapida( **dic_general):
    """
    ⚡ Busca al piloto con la vuelta más rápida entre los 10 primeros puestos.

    
    Parámetros:
    📥 dic_general: diccionario con datos de pilotos.
    
    Retorna:
    📤 Devuelve el nombre del piloto con vuelta más rápida o un mensaje si no hay.
    """
    vuelta_rapida_menor = float("inf")
    piloto_vuelta_rapida = None

    # Encontrar el piloto con la vuelta más rápida más baja en los primeros 10
    for piloto in dic_general.keys():
        if dic_general[piloto]['vuelta mas rapida'] < vuelta_rapida_menor \
        and piloto in puntos_por_orden_llegada[:10]:
            vuelta_rapida_menor = dic_general[piloto]['vuelta mas rapida']
            piloto_mas_rapido = piloto
    # Si se encontró un piloto, agregarle un punto
    if piloto_mas_rapido:
        return piloto_mas_rapido
    else:
        return "No se consiguie la vuelta mas rápida dentro de los 10 primeros"

piloto_mas_rapido=vuelta_mas_rapida( **dic_general)
print(f'''{"-" * 100}
    ⚡ El piloto más rápido de la carrera fue: {piloto_mas_rapido}
    🕒 En su vuelta más rápida tardó: {dic_general[piloto_mas_rapido]["vuelta mas rapida"]} segundos
    🔁 Total de vueltas: {dic_general[piloto_mas_rapido]["total de vueltas"]}
    ⏱️ Tiempo total en pista: {dic_general[piloto_mas_rapido]["tiempo total en pista"]}
{"-"*100}''')
print ("-"*100)
########################################################################

# Función para sumar puntos por escudería
def sumar_puntos_por_escuderia(dic_general):
    """
    📊 Crea un diccionario que suma los puntos de los pilotos por escudería.

    Parámetros:
    dic_general: diccionario con los datos de los pilotos, incluyendo los puntos y la escudería.
    
    Retorna:
    dic_escuderia: diccionario con el total de puntos por escudería.
    """
    # Inicializar un diccionario vacío para acumular los puntos por escudería
    dic_escuderia = {}

    # Acumular puntos por escudería
    for piloto, datos in dic_general.items():
        escuderia = datos['Escuderia']
        puntos = datos['Puntos']

        if escuderia not in dic_escuderia.keys():
            dic_escuderia[escuderia] = puntos
        else:
            dic_escuderia[escuderia] += puntos

    return dic_escuderia

# Llamar a la función y mostrar resultados
dic_escuderia = sumar_puntos_por_escuderia(dic_general)

# Mostrar resultados de puntos por escudería
print("⭐" * 50)
for escuderia, puntos in dic_escuderia.items():
    print(f"Escudería: {escuderia}, Puntos Totales: {puntos}")
print("⭐" * 50) 








########################################################################
# Función para obtener las n escuderías con más puntos
def obtener_top_escuderias(dic_escuderia, n=3):
    """
    Obtiene las n escuderías con más puntos.
    
    Parámetros:
    dic_escuderia: diccionario con el total de puntos por escudería.
    n: número de escuderías a retornar.
    
    Retorna:
    lista_top: lista de las n escuderías con más puntos.
    """
    # Ordenar el diccionario por puntos en orden descendente y obtener las n escuderías con más puntos
    lista_top = list(map(lambda item: item[0:2], sorted(dic_escuderia.items(), key=lambda x: x[1], reverse=True)))[:n]
    
    return lista_top

# Obtener las tres escuderías con más puntos
top_escuderias = obtener_top_escuderias(dic_escuderia)
# ~ top_escuderias = obtener_top_escuderias(dic_escuderia,5)

# Mostrar resultados del top de escuderías
print("\n" + "🏆" * 30)
print("🔥 TOP 3 ESCUDERÍAS 🔥")
print("🏆" * 30)
for escuderia, puntos in top_escuderias:
    print(f"Escudería: {escuderia}, Puntos Totales: {puntos}")

print("*" * 100)

########################################################################
# Guardar el diccionario de puntos por escudería en formato JSON
import os
import json
try:
    import pandas as pd
except ImportError:
    import pip
    pip.main(['install', 'pandas'])
    import pandas as pd
    
    
try:
    from sqlalchemy import create_engine# librerias de bbdd---->sqlite
except ImportError:
    import pip
    pip.main(['install', 'sqlalchemy'])
    from sqlalchemy import create_engine# librerias de bbdd---->sqlite


# Guardar JSON
json_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.json')
with open(json_path, 'w') as json_file:
    json.dump(dic_escuderia, json_file)

# Guardar el diccionario en formato Excel (XLSX)
df_escuderia = pd.DataFrame(list(dic_escuderia.items()), columns=['Escudería', 'Puntos Totales'])
excel_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.xlsx')
df_escuderia.to_excel(excel_path, index=False)

# Guardar el diccionario en una base de datos SQLite
# Crear el path absoluto
db_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.db')
# Crear el engine con el path correcto
engine = create_engine(f'sqlite:///{db_path}')
# Guardar el DataFrame en la tabla 'escuderias'
df_escuderia.to_sql('escuderias', con=engine, if_exists='replace', index=False)

# Confirmación de los archivos guardados
print("Podio de escuderías guardado en JSON, Excel y BBDD.")
print("*" * 100) 
########################################################################