# Matriz 3D que recopila los datos pertenecientes a las temperaturas de 3 ciudades durante 4 semanas
# En esta Matriz averiguaremos el promedio total de temperaturas respecto a las 3 ciudades
# Primera dimensión: Ciudades (Quito, Guayaquil, Ambato)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [
    [   #Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp":19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Ambato
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ]
    ]
]


def calcular_temperatura_promedio(temperaturas):
    """
    Esta función calcula el promedio total de temperaturas de las ciudades de Quito Guayaquil y Ambato durante 4 semanas.

        :temperaturas: contiene los datos de las temperaturas en lista organizada por ciudades y semanas.
    Return:
        dict: devuelve un diccionario con los nombres de las ciudades y las temperaturas promedio con sus valores.
    """
    ciudades = ["Quito", "Guayaquil", "Ambato"]# creamos una lista para las ciudades

    promedio_temperaturas = {}# agregamos un diccionario para guardar las ciudades y promedios

    for indice_ciudad , ciudad in enumerate(temperaturas): #blucle for para recorrer listas de temperaturas el numerate se encargara de asociar los datos de las temperaturas con el nombre correcto de la ciudad

        total_temp = 0      #almacena la suma de las temperaturas de la ciudad
        total_dias = 0      #contará el número total de días

        for semana in ciudad: #bucle for que recorre cada semana dentro de la ciudad
            for dia in semana: #buble for recorre cada dia dentro de la semana
                total_temp += dia["temp"] #se sumaran las temperaturas del dia
                total_dias += 1 #ayuda a incrementar en 1 la cantidad de días registrados

        promedios = total_temp / total_dias #se calcula el promedio dividiendo la suma total de las temperaturas con el total de dias
        promedio_temperaturas[ciudades[indice_ciudad]] = promedios #asignamos al diccionario el resultado del promedio con el nombre de las ciudades correspondientes

    return promedio_temperaturas #devuelve al diccionario las temperaturas promedio de cada ciudad


# Llamamos a la función para calcular las temperaturas promedio
promedio_temperaturas = calcular_temperatura_promedio(temperaturas)

# Mostramos los resultados
print("=" * 50)
print("PROMEDIO TOTAL DE LAS TEMPERATURAS DE CADA CIUDAD :")
print("=" * 50)
for ciudad, promedios in promedio_temperaturas.items():
    print("-" * 20)
    print(f"{ciudad}: {promedios:.2f}°C")

