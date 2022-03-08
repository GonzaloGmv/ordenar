import random

class ejr2():
    def __init__(self):
        tareas = []
        for i in range(int(input("Escriba el numero de tareas que va a realizar: "))):
            tarea = 't' + (str(i+1))
            tareas.append(tarea)
        random.shuffle(tareas)
        print(tareas)
        self.tareas = tareas

    def ordenacion(self, n, t):
        if len(self.tareas) > 0:
            if 't' + str(n) == self.tareas[t]:
                print("Ha realizado la tarea", n)
                del self.tareas[t]
                self.ordenacion(n+1, 0)
            else:
                print("Esa tarea no es la que toca ahora, realice la tarea", n)
                self.ordenacion(n, t+1)