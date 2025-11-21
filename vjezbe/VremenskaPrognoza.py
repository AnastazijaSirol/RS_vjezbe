class VremenskaPrognoza:
    def __init__(self, grad, temp_zraka, datum):
        self.grad = grad
        self.temp_zraka = temp_zraka
        self.datum = datum
    def ispis(self):
        print(f"{self.datum.strftime('%d.%m.%Y')} - {self.grad}: {self.temp_zraka}°C")
    def dnevna_promjena(self, nova_temp, novi_datum):
        self.temp_zraka = nova_temp
        self.datum = novi_datum
