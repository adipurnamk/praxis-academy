class Binatang:
    def __init__(self, nama, kaki):
        self.nama = nama
        self.kaki = kaki

class Beruang(Binatang):
    def __init__(self, nama, kaki=4, hibernasi='ya'):
        Binatang.__init__(self, nama, kaki)
        self. hibernasi = hibernasi

K = Beruang('Kuma')
print(K.nama)
print(K.kaki)
print(K.hibernasi)