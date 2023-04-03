class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies
    
    def suara(self, suara):
        print(f"{self.nama} adalah {self.spesies} memiliki suara {suara}")
        
kucing = Hewan("Caca", "Kucing")
anjing = Hewan("Chiko", "Anjing")

kucing.suara("Meoww")  # Caca adalah Kucing memiliki suara Meoww
anjing.suara("Woogg")  # Chiko adalah Anjing memiliki suara Woogg
