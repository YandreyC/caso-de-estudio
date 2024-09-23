class Motor:
    def __init__(self, cilindros, hp):
        self.__cilindros = cilindros
        self.__hp = hp

    def __repr__(self):
        return f"{self.__cilindros} cilindros tiene una potencia de {self.__hp} hp"

    def trabajar(self):
        print("El motor esta encendido")

    @property
    def cilindros(self):
        return self.__cilindros


class Auto:
    autos_predeterminados = {
        1: {"modelo": "Ford", "precio": 20000},
        2: {"modelo": "Chevrolet", "precio": 25000},
        3: {"modelo": "Toyota", "precio": 18000},
        4: {"modelo": "Honda", "precio": 22000},
        5: {"modelo": "Nissan", "precio": 28000},
    }

    def __init__(self, modelo, precio, color):
        self.__modelo = modelo
        self.__precio = precio
        self.__motor = Motor(4, 250)
        self.__color = color

    def __repr__(self):
        return f"El auto {self.__modelo} de color {self.__color} con el motor de {self.__motor}, cuesta ${self.__precio} dolar(es)"

    def encender(self):
        print("Encendiendo el motor...")
        self.__motor.trabajar()

    @staticmethod
    def seleccionar_color():
        lista = {1: "Rojo", 2: "Azul", 3: "Negro", 4: "Blanco", 5: "Gris"}
        while True:
            try:
                print(lista)
                seleccion = int(input("Seleccione un número para su color\n"))
                color = lista.get(seleccion)
                if color:
                    return color
                else:
                    print("Opción inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Error... Ingrese digitos")
                continue

    @classmethod
    def seleccionar_auto(cls):
        while True:
            try:
                print("Autos disponibles:")
                for key, value in cls.autos_predeterminados.items():
                    print(f"{key}: {value['modelo']} - ${value['precio']}")
                seleccion = int(input("Seleccione un número para su auto\n"))
                auto = cls.autos_predeterminados.get(seleccion)
                if auto:
                    return auto
                else:
                    print("Opción inválida. Intente de nuevo.")
                    continue
            except ValueError:
                print("Error... Ingrese digitos")
                continue

    @classmethod
    def crear_auto(cls):
        auto_seleccionado = cls.seleccionar_auto()
        color_seleccionado = cls.seleccionar_color()
        return cls(auto_seleccionado["modelo"], auto_seleccionado["precio"], color_seleccionado)


auto1 = Auto.crear_auto()
print(auto1)
auto1.encender()  