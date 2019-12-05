class binatang:
    def __init__(self, nama):    # Constructor of the class
        self.nama = nama

class Kucing(binatang):
    def suara(self):
        return self.nama+ ' mengeong!'

class Tikus(binatang):
    def suara(self):
        return self.nama+ ' bercicit!'

class Anjing(binatang):
    def suara(self):
        return self.nama+ ' menggonggong!'

T = Kucing('Tom')
J = Tikus('Jerry') 
H = Anjing('Hector')

print(T.suara())
print(J.suara())
print(H.suara())