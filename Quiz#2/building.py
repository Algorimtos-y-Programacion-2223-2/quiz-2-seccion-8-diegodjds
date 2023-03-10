# Pregunta#1

class Building:

    def _init_(self, name, floors, street, city, postal, apartments):
        self.name = name
        self.floors = floors
        self.street = street
        self.city = city
        self.postal = postal
        self.apartments = []

    def showDirection(self):
        print(f"""
    Nombre: {self.name}
    Pisos: {self.floors}
    Calle: {self.street}
    Ciudad: {self.city}
    Código Postal: {self.postal}
    Apartamentos: {self.apartments}
    """)

    def clasifyBuilding(self):
        if len(self.apartments) > (6 * self.floors):
            return "Bloque de Pisos"
        if len(self.apartments) < (6 * self.floors):
            return "Edificio Residencial"

    def showApartments(self):
        for i, apartment in enumerate(self.apartments):
            print(f"{i+1}. {apartment}")
