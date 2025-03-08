#Matriz 3D que recopila los datos pertenecientes a las temperaturas de 3 ciudades durante 4 semanas para averiguar su promedio
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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Quito", "Guayaquil", "Ambato"]

print("=" * 47)
print("PROMEDIO DE LAS TEMPERATURAS EN LAS 3 CIUDADES")
print("=" * 47)

for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\nCiudad: {ciudades[ciudad_idx]}")
    print("-" * 40)
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Semana {semana_idx + 1}: {promedio:.2f} °C")

        