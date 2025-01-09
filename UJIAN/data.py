class Data:
    
    def __init__(self):
        self.data = []

    def add_mahasiswa(self, nama, nim, nilai):
        self.data.append({"Nama": nama, "NIM": nim, "Nilai": nilai})

    def get_all_data(self):
        return self.data