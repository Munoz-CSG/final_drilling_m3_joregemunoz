nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

magos = ["Harry Houdini","David Blaine","Teller"]
cientificos = ["Newton","Hawking","Einstein"]
otros = []

for nombre in nombres:
    if nombre not in magos and nombre not in cientificos:
        otros.append(nombre)

def hacer_grandioso(magos):
    return [f"El gran {mago}" for mago in magos]

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

print("TOTALIDAD DE NOMBRES:")
imprimir_nombres(nombres)
print("\nMAGOS GRANDIOSOS:")
imprimir_nombres(hacer_grandioso(magos))
print("\nCIENTÍFICOS:")
imprimir_nombres(cientificos)
print("\nOTROS:")
imprimir_nombres(otros)