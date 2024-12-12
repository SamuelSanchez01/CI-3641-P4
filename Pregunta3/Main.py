from Clases import Simulator

# Se ejecuta el simulador
simulator = Simulator()

while True:
    # Solicita una acción al usuario
    action = input('> ')
    # Si la acción es 'SALIR', termina el bucle
    if action == 'SALIR':
        break
    # Si la acción comienza con 'CLASS ', intenta agregar una clase
    elif action.startswith('CLASS '):
        # Divide la acción en nombre y métodos
        _, name, *metodos = action.split()
        # Si el primer método es ':', se proporcionó un nombre de superclase
        if len(metodos) > 0 and metodos[0] == ':':
            # Divide los métodos en nombre de superclase y métodos
            _, superclase_name, *metodos = metodos
            # Si ':' está en los métodos, imprime un error y continúa con el siguiente ciclo
            if ':' in metodos:
                print('Error: El nombre ":" no es válido para un método..')
                continue
            # Agrega la clase con el nombre de superclase
            simulator.add_class(name, metodos, superclase_name)
        else:
            # Si ':' está en los métodos, imprime un error y continúa con el siguiente ciclo
            if ':' in metodos:
                print('Error: El nombre ":" no es válido para un método.')
                continue
            # Agrega la clase sin nombre de superclase
            simulator.add_class(name, metodos)
    # Si la acción comienza con 'DESCRIBIR ', intenta describir una clase
    elif action.startswith('DESCRIBIR '):
        # Si la acción se divide en dos partes, intenta describir la clase
        if len(action.split()) == 2:
            _, name = action.split()
            print(simulator.describe_class(name))
        else:
            # Si la acción no se divide en dos partes, imprime un error
            print('Error: Comando inválido. \n \t USO: DESCRIBIR <nombre>')
    else:
        # Si la acción no es reconocida, imprime un error
        print('Error: Comando inválido.\n \t USO: CLASS <tipo> [<nombre>], DESCRIBIR <nombre>, o SALIR')