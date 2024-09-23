class Hamburguesa: # La clase base para todas la hamburguesas
    def __init__(self, pan, carne, salsa_tomate, mayonesa):
        self.__pan = pan
        self.__carne = carne                    # Se inizializan los ingredientes principales
        self.__salsa_tamate = salsa_tomate
        self.__mayonesa = mayonesa

    def tiempo(self):
        i = 5               # Nos ayuda a saber cuanto se tarda una hamburguesa simple, por cada ingrediente agregado se tardara un minuto mas
        print(f"esta haburguesa estara lista en {i} minutos")

    def personalizar(self):
        print("Seleccione los ingredientes adicionales:")
        ingredientes = ["cebolla caramelizada", "champiñón", "tocineta", "huevo", "maiz", "lechuga", "tomate", "queso mozzarella"]
        seleccionados = []
        for ingrediente in ingredientes:                                    # Permite elegir los ingredientes en la clase HamburgesaPersonalizada
            respuesta = input(f"¿Desea agregar {ingrediente}? (s/n): ")
            if respuesta.lower() == "s":
                seleccionados.append(ingrediente)
        return seleccionados

class HamburguesaCampesina(Hamburguesa):  # Esta hamburgesa ya biene con ingredientes predeterminados
    def __init__(self, pan, carne, salsa_tomate, mayonesa, cebolla_caramelizada, champiñón, tocineta, huevo, maiz, lechuga, tomate, queso_mozarella):
        self.__cebolla_caramelizada = cebolla_caramelizada
        self.__champiñón = champiñón
        self.__tocineta = tocineta
        self.__huevo = huevo
        self.__maiz = maiz
        self.__lechuga = lechuga
        self.__tomate = tomate
        self.__queso_mozarella = queso_mozarella
        super().__init__(pan, carne, salsa_tomate, mayonesa)
    
    def tiempo(self):
        i = 5
        ingredientes_totales = 8                # Se suman la cantidad de ingredientes agregados al tiempo de la hamburgesa simple
        i = i + ingredientes_totales
        print(f"La hamburguesa estara lista en {i} minutos")

class HamburguesaAmericana(Hamburguesa):
    def __init__(self, pan, carne, salsa_tomate, mayonesa, cebolla_caramelizada, tocineta, piña, queso_mozarella, lechuga, tomate):
        self.__cebolla_caramelizada = cebolla_caramelizada
        self.__tocineta = tocineta
        self.__lechuga = lechuga
        self.__tomate = tomate
        self.__queso_mozarella = queso_mozarella
        self.__piña = piña
        super().__init__(pan, carne, salsa_tomate, mayonesa)

    def tiempo(self):
        i = 5
        ingredientes_totales = 6
        i = i + ingredientes_totales
        print(f"La hamburguesa estara lista en {i} minutos")

class HamburguesaClasica(Hamburguesa):
    def __init__(self, pan, carne, salsa_tomate, mayonesa, cebolla_caramelizada, queso_mozarella, lechuga, tomate):
        self.__cebolla_caramelizada = cebolla_caramelizada
        self.__lechuga = lechuga
        self.__tomate = tomate
        self.__queso_mozarella = queso_mozarella
        super().__init__(pan, carne, salsa_tomate, mayonesa)

    def tiempo(self):
        i = 5
        ingredientes_totales = 4
        i = i + ingredientes_totales
        print(f"La hamburguesa estara lista en {i} minutos")

class HamburguesaPersonalizada(Hamburguesa): # Permite añadir los ingredientes que quieras
    def __init__(self, pan, carne, salsa_tomate, mayonesa):
        super().__init__(pan, carne, salsa_tomate, mayonesa)
        self.ingredientes_adicionales = []

    def personalizar(self):
        self.ingredientes_adicionales = super().personalizar(hamburguesa)      # Desde aqui se añaden los ingredientes, tomando la funcion de la clase base
        print(f"Ingredientes adicionales seleccionados: {self.ingredientes_adicionales}")

    def tiempo(self):
        i = 5
        ingredientes_totales = len(self.ingredientes_adicionales)    # Se suma el numero de ingredientes selecionados al tiempo de una hamburguresa simple
        i = i + ingredientes_totales
        print(f"La hamburguesa estará lista en {i} minutos")

while True:
    try:
        pedido = int(input("Que hamburguesa desea pedir?\n1.Hamburguesa Simple\n2.Hamburgesa Clasica\n3.Hamburguesa Americana\n4.Hamburguesa Campesina\n5.Hamburgueza Personalizada\n"))
        if pedido == 1:
            hamburguesa = Hamburguesa
            hamburguesa.tiempo(hamburguesa)
        elif pedido == 2:
            hamburguesa = HamburguesaClasica
            hamburguesa.tiempo(hamburguesa)
        elif pedido == 3:
            hamburguesa = HamburguesaAmericana
            hamburguesa.tiempo(hamburguesa)                     # Se toma el pedido y se toma la clase a la que pertenece para asi poder saber el tiempo de pedido
        elif pedido == 4:
            hamburguesa = HamburguesaCampesina
            hamburguesa.tiempo(hamburguesa)
        elif pedido == 5:
            hamburguesa = HamburguesaPersonalizada
            hamburguesa.personalizar(hamburguesa)
            hamburguesa.tiempo(hamburguesa)
        
        pedir_otra_hamburguesa = int(input("Desea pedir otra hamburguesa\n1.Si\n2.No\n"))
        if pedir_otra_hamburguesa == 1:                     # Aqui eligen si desean tomar otro pedido
            continue
        else:
            break

    except ValueError:
        print("Error... Ingrese datos validos")
        continue