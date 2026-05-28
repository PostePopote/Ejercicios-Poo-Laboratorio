"""Crear 3 clases: “Mago” , “Guerrero” y “Elfo”

La clase “Mago”, debe tener un método llamado “hechizos”
la clase “Guerrero” debe tener un método llamado “defensa”
la clase “Elfo” debe tener una método llamado “aura”.

Luego crear una clase llamada “DarkLord” que herede de “Guerrero “ y “Elfo”, 
en ese orden y por lo tanto puede usar “defensa” y “aura”, además de los hechizos.

por último cambiar el orden de las herencias de la clase “DarkLord” y 
observa cómo se va modificando el orden del MRO.
"""

class Mago:
    def __init__(self, nombre, fuerza, agilidad, vitalidad, mana):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.mana = mana
    def hechizo(self, daño, efecto, coste):
        self.daño = daño
        self.efecto = efecto
        self.coste = coste

class Guerrero:
    def __init__(self, nombre, fuerza, agilidad, vitalidad, mana):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.mana = mana
    def defensa(self, reduccion, efecto, coste):
        self.reduccion = reduccion
        self.efecto = efecto
        self.coste = coste

class Elfo:
    def __init__(self, nombre, fuerza, agilidad, vitalidad, mana):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.vitalidad = vitalidad
        self.mana = mana
    def aura(self, curacion, efecto, coste):
        self.curacion = curacion
        self.efecto = efecto
        self.coste = coste

class DarkLord(Mago, Elfo, Guerrero):
    def __init__(self, nombre, fuerza, agilidad, vitalidad, mana):
        super().__init__(nombre, fuerza, agilidad, vitalidad, mana)

mago = Mago("Merlin", 20, 30, 50, 200)
guerrero = Guerrero("Thor", 90, 40, 120, 30)
elfo = Elfo("Legolas", 50, 100, 70, 80)
dark = DarkLord("Sauron", 100, 60, 200, 300)

mago.hechizo(80, "Fuego", 40)

guerrero.defensa(50, "Escudo", 20)

elfo.aura(30, "Regeneración", 15)

dark.defensa(70, "Armadura oscura", 25)
dark.aura(40, "Aura maldita", 35)
dark.hechizo(120, "Tormenta oscura", 60)


print("MRO de DarkLord:")
print(DarkLord.__mro__)