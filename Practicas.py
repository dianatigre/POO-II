#Ejercicio 1
notas = [10, 8, 9, 5]
print(notas)
print(notas[1])
notas.append(20)
print(max(notas))
notas.insert(1, 10)
print(len(notas))
print(notas[-1])
print(sum(notas))
print(notas[0])
print(notas[-2])
print(notas[2])
print(min(notas))
notas.remove(9)
notas = sorted(notas)
print(notas[2:])
print(notas[:2])

# Ejercicio 2
# Tuplas
meses =("1","2","3","4","5","6","7","8","9","10","11","12")
print(meses[0])
print(meses[-1])
print(meses)

# Ejercicio 3
estudiante={
     "cedula": "0106384258",
     "nombre": "diana tigre",
     "correo":"diana,tigre10.@gmail.com",
     "celular":"0959173771",
     "nota": [10,9,8,5,4]
     }
print(estudiante.get("nombre"))
print(estudiante.keys())

# Ejercicio 4
conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

# Ejercicio 5
socio = {
    "cedula": "0102030405",                 
    "nombre": "  ana lucía pérez ",          
    "edad": 34,                              
    "activo": True,                         
    "garante": None,                         
    "cuentas": [                             
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ]
}

print(socio.get    ("nombre").strip())
print(socio.get    ("nombre").title())
print("La cedula es", socio.get("cedula"),"La edad es: ", {socio.get("edad"))
print(f'activo'={socio.get("activo")})


# Ejercicio 6
# Definición de diccionarios y copias
original = {"nombre": "Ana", "saldo": 100}
alias = original           # Asigna una referencia al mismo diccionario
copia = original.copy()    # Crea una copia independiente (superficial) en memoria

alias["saldo"] = 500       # Modifica 'original' porque comparten la misma referencia
copia["saldo"] = 999       # Modifica únicamente la copia independiente

# 1. Muestre original, alias y copia
print("--- 1. Resultados ---")
print("Original:", original) # Muestra saldo: 500 (afectado por alias)
print("Alias:   ", alias)    # Muestra saldo: 500
print("Copia:   ", copia)    # Muestra saldo: 999

# 2. Compruebe con 'is' cuáles son el mismo objeto
print("\n--- 2. Comprobación de identidad (is) ---")
print("¿alias es el mismo objeto que original?:", alias is original) # True: Apuntan a la misma dirección
print("¿copia es el mismo objeto que original?:", copia is original) # False: Es un objeto distinto

# 3. Compare con id() las direcciones de memoria
print("\n--- 3. Identificadores de memoria (id) ---")
print("ID Original:", id(original)) # Mismo valor numérico que alias
print("ID Alias:   ", id(alias))    # Mismo valor numérico que original
print("ID Copia:   ", id(copia))    # Dirección de memoria diferente


#Condicionales

i=0
while i<5:
     print(i)
     i+=1
print("fin de ejecucion")

While True:
    s=input("ingreso un nuemero")
    it int(s)

for i in range


tyuil
