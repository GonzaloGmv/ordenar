# 1.1
class ejr1a:
    def __init__(self):
        while True:
            tabla = input("Escriba los elementos de su tabla separados por espacios: ")
            tabla = tabla.split()
            try:
                for i in range(len(tabla)):
                    tabla[i] = int(tabla[i])
                print("Los ordenaremos como tipo int")
            except:
                try:
                    for i in range(len(tabla)):
                        tabla[i] = float(tabla[i])
                    print("Los ordenaremos como tipo float")
                except:
                    print("Los ordenaremos como tipo string")
            break
        tabla.sort()
        self.tabla = tabla

    def buscar(self, c, m, m0):
        if m >= 0 and m <= len(self.tabla):
            if type(c) == type(self.tabla[m]):
                if c == self.tabla[m]:
                    print(c, "se encuentra en la posicion", m)
                elif c > self.tabla[m] and m >= m0:
                    m0 = m
                    self.buscar(c, m+1, m0)
                elif c < self.tabla[m] and m <= m0:
                    m0 = m
                    self.buscar(c, m-1, m0)
                else:
                    print(c, "no esta en la tabla")
            else:
                    print(c, "no esta en la tabla")
        else:
            print(c, "no esta en la tabla")

    def ejecutar(self):
        n = input("Escriba el valor de c: ")
        try:
            n = int(n)
        except:
            try:
                n = float(n)
            except:
                pass
        self.buscar(n, int(len(self.tabla)/2), int(len(self.tabla)/2))

#1.2 - 1.3
