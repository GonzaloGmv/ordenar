# 1.a
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
        if type(c) == type(self.tabla[m]):
            if c in self.tabla:
                if c == self.tabla[m]:
                    print(c, "se encuentra en la posicion", m)
                elif c > self.tabla[m]:
                    self.buscar(c, int((m0+m)/2), m)
                elif c < self.tabla[m]:
                    self.buscar(c, int((m0-m)/2), m)
            else:
                print(c, "no esta en la tabla")
        else:
            print(c, "no esta en la tabla")
        
    def ejecutar_1a(self):
        n = input("Escriba el valor de c: ")
        try:
            n = int(n)
        except:
            try:
                n = float(n)
            except:
                pass
        self.buscar(n, int(len(self.tabla)/2), int(len(self.tabla)))

# 1.b
class ejr1b:
    def __init__(self):
        while True:
            t = input("Escriba los elementos de su tabla separados por espacios: ")
            t = t.split()
            try:
                for i in range(len(t)):
                    t[i] = int(t[i])
                print("Los ordenaremos como tipo int")
            except:
                try:
                    for i in range(len(t)):
                        t[i] = float(t[i])
                    print("Los ordenaremos como tipo float")
                except:
                    print("Los ordenaremos como tipo string")
            break
        r = []
        self.t = t
        self.r = r

    def crear(self, n, m, m0):
        if n == 0:
            self.r.append(self.t[n])
        else:
            if len(self.r) == 1:
                if self.r[m] == self.t[n]:
                    self.r.insert(m, self.t[n])
                elif self.r[m] > self.t[n]:
                    self.r.insert(0, self.t[n])
                elif self.r[m] < self.t[n]:
                    self.r.append(self.t[n])
            else:
                