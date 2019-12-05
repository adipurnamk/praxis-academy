class toko:
    def __init__(self, nama, lokasi):
        self.nama=nama
        self.lokasi=lokasi
        
    def tampil (self):
        return "{} {}".format(self.nama, self.lokasi)

Toko1=toko("Kelontong", "Cangkringan")
print(Toko1.tampil())
