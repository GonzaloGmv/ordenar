from clases.ejercicio1 import ejr1a

if __name__ == "__main__":

    while True:
        ejr = input("Escriba el numero del ejercicio que desea iniciar: ")
        try:
            ejr = int(ejr)
        except:
            pass
        else:
            if 1 <= ejr <= 3:
                break

    if ejr == 1:
        while True:
            ejr = input("Escriba el apartado que desea iniciar, a o b: ")
            try:
                ejr = 'a'
            except:
                try:
                    ejr = 'b'
                except:
                    pass
            else:
                break

        if ejr == 'a':
            ejercicio_1 = ejr1a()
            ejercicio_1.ejecutar()