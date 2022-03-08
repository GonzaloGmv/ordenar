from clases.ejercicio1 import ejr1a, ejr1b
from clases.ejercicio2 import ejr2

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
                ejr == 'a' or ejr == 'b'
            except:
                pass
            else:
                break

        if ejr == 'a':
            ejercicio = ejr1a()
            ejercicio.ejecutar_1a()

        elif ejr == 'b':
            ejercicio = ejr1b()
            ejercicio.crear(0, 0, 0)
            
    if ejr == 2:
        ejercicio = ejr2()
        ejercicio.ordenacion(1, 0)
