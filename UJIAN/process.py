from data import Data
from view import View

class Process:
    
    def __init__(self):
        self.data_store = Data()
        self.view = View()

    def run(self):
        while True:
            print("\n1. Tambah Data Mahasiswa")
            print("2. Tampilkan Data Mahasiswa")
            print("3. Keluar")
            try:
                pilihan = int(input("Pilih menu: "))

                if pilihan == 1:
                    result = self.view.input_data()
                    if result:
                        self.data_store.add_mahasiswa(*result)
                        print("Data berhasil ditambahkan!")
                elif pilihan == 2:
                    self.view.display_table(self.data_store.get_all_data())
                elif pilihan == 3:
                    print("Keluar dari program.")
                    break
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka!")