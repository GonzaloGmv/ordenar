# ordenar

Mi dirección de github para este repositorio es: [ github](https://github.com/GonzaloGmv/ordenar)

El diagrama de flujo se encuentra en la carpeta diagramas, como archivo .jpg y como archivo .drawio y es el siguiente:

![diagrama](https://user-images.githubusercontent.com/91721237/158027643-f206f135-36e2-48bd-8ef8-e00f9bf6e119.jpg)

El UML se encuentra en la carpeta diagramas, como archivo .jpg y como archivo .drawio y es el siguiente:

![uml](https://user-images.githubusercontent.com/91721237/158073053-3677f934-b5b3-42de-acdb-ca5a97b4b995.jpg)

### Ejercicio 1
Mi código para este ejercicio es el siguiente:
```
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
                if self.t[n] == self.r[m]:
                    self.r.insert(m, self.t[n])
                elif self.t[n] < self.r[m]:
                    if m == 0:
                        self.r.insert(0, self.t[n])
                    else:
                        if m0 == m or m0 > m:
                            self.crear(n, int(m/2), m)
                        else:
                            self.r.insert(m, self.t[n])
                elif self.t[n] > self.r[m]:
                    if m == len(self.r) - 1:
                        self.r.append(self.t[n])
                    else:
                        if m0 == m or m0 < m:
                            self.crear(n, int((len(self.r)+m)/2), m)
                        else:
                            self.r.insert(m+1, self.t[n])            
        if len(self.r) < len(self.t):
            self.crear(n+1, int(len(self.r)/2), int(len(self.r)/2))
    
    def resultado(self):
        print(self.r)
```

### Ejercicio 2
Mi código para este ejercicio es el siguiente:
```
import random

class ejr2():
    def __init__(self):
        tareas = []
        for i in range(int(input("Escriba el numero de tareas que va a realizar: "))):
            tarea = 't' + (str(i+1))
            tareas.append(tarea)
        random.shuffle(tareas)
        print(tareas)
        orden = []
        self.tareas = tareas
        self.orden = orden

    def ordenacion(self, n, t):
        if len(self.tareas) > 0:
            if 't' + str(n) == self.tareas[t]:
                print("Ha realizado la tarea", n)
                self.orden.append(self.tareas[t])
                del self.tareas[t]
                self.ordenacion(n+1, 0)
            else:
                print("Esa tarea no es la que toca ahora, realice la tarea", n)
                self.ordenacion(n, t+1)
        else:
            print(self.orden)
```

### Ejercicio 3
Mi código para este ejercicio es el siguiente:
```
class ejr3():
    def __init__(self):
        while True:
            vector = input("Escriba los elementos de su vector separados por espacios: ")
            vector = vector.split()
            try:
                for i in range(len(vector)):
                    vector[i] = int(vector[i])
            except:
                try:
                    for i in range(len(vector)):
                        vector[i] = float(vector[i])
                except:
                    break
            break
        s1 = []
        s2 = []
        self.vector = vector
        self.s1 = s1
        self.s2 = s2


    def segmentos(self):
        d1 = max(self.vector[:int(len(self.vector)/2)])
        d2 = ''
        self.s1.append(d1)
        for i in range(len(self.vector) - self.vector.index(d1)):
            i = i + self.vector.index(d1) + 1
            if i != len(self.vector):
                if self.vector[i] <= d1:
                    self.s1.append(self.vector[i])
                else:
                    d2 = self.vector[i]
                    break
            else:
                break
        self.s2.append(d2)
        if self.s2 != ['']:
            for i in range(len(self.vector) - self.vector.index(d1)):
                i = i + self.vector.index(d2) + 1
                if i != len(self.vector):
                    if self.vector[i] <= d2:
                        self.s2.append(self.vector[i])
                    else:
                        d2 = self.vector[i]
                        break
                else:
                    break

    def explorar(self, segmento):
        mi = segmento[0]
        for i in range(len(segmento)-1):
            segmento[i] = segmento[i + 1]
        segmento[len(segmento)-1] = mi
        print(segmento)

    def resultado(self):
        self.segmentos()
        print("Este es el primer segmento:")
        print(self.s1)
        print("Este es el primer segmento ordenado:")
        self.explorar(self.s1)
        if self.s2 != ['']:
            print("Este es el segundo segmento:")
            print(self.s2)
            print("Este es el segundo segmento ordenado:")
            self.explorar(self.s2)
        else:
            print("Solo hay un vector")
```

### Main
El código del main es:
```
from clases.ejercicio1 import ejr1a, ejr1b
from clases.ejercicio2 import ejr2
from clases.ejercicio3 import ejr3

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
            ejercicio.resultado()        
    elif ejr == 2:
        ejercicio = ejr2()
        ejercicio.ordenacion(1, 0)
    else:
        ejercicio = ejr3()
        ejercicio.resultado()
```        
