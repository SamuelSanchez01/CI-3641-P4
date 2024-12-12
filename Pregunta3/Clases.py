class Clase:
    #Una clase para representar un tipo de clase
    
    #constructor
    def __init__(self, name, superclase=None):
        self.name = name
        self.superclase = superclase
        self.metodos = {}

    #añadir
    def add_metodo(self, metodo):
        self.metodos[metodo] = f'{self.name} :: {metodo}'

    #obtener
    def getmetodo(self, metodo):
        if metodo in self.metodos:
            return self.metodos[metodo]
        elif self.superclase:
            return self.superclase.getmetodo(metodo)
        else:
            return None

#el simulador
class Simulator:
    def __init__(self):
        self.classes = {}

    def add_class(self, name, metodos, superclase_name=None):
        #Verificamos si ya existe la clase
        if name in self.classes:
            print(f'La clase {name} ya existe')
            return
        #Verificamos ya existe la superclase
        if superclase_name and superclase_name not in self.classes:
            print(f'La super clase {superclase_name} no existe')
            return
        #Verificamos si hay nombres de metodos duplicados
        if len(set(metodos)) < len(metodos):
            print('Nombres de metodos duplicados')
            return
        superclase = self.classes.get(superclase_name)
        #Verificamos si la clase está intentando heredar de si misma
        while superclase:
            if superclase.name == name:
                print(f'La clase {name} no puede heredar de si misma')
                return
            superclase = superclase.superclase
        superclase = self.classes.get(superclase_name)
        new_class = Clase(name, superclase)
        for metodo in metodos:
            new_class.add_metodo(metodo)
        self.classes[name] = new_class

    def describe_class(self, name):
        #describe una clase

        if name not in self.classes:
            print(f'La clase {name} no existe')
            return
        class_type = self.classes[name]
        metodosimpresos = set()

        string_metodos = ""
        while class_type:
            for metodo in class_type.metodos:
                if metodo not in metodosimpresos:
                    if not string_metodos:
                        string_metodos = f'{metodo} -> {class_type.getmetodo(metodo)}'
                    else:
                        string_metodos += f'\n{metodo} -> {class_type.getmetodo(metodo)}'
                    metodosimpresos.add(metodo)
            class_type = class_type.superclase
        if not metodosimpresos:
            string_metodos = f'La clase {name} no tiene metodos'
        return string_metodos