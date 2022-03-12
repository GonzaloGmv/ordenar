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