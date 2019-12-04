class Orang:
    def __init__(self, nama):
        self.nama = nama

    def say_hi(self):
        print ('Halo, nama saya adalah', self.nama)

p = Orang ('Aca')
p.say_hi()