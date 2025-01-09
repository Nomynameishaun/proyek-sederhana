class View:
    
    @staticmethod
    def input_data():
        try:
            nama = input("Masukkan Nama: ").strip()
            if not nama:
                raise ValueError("Nama tidak boleh kosong!")

            nim = input("Masukkan NIM: ").strip()
            if not nim.isdigit():
                raise ValueError("NIM harus berupa angka!")

            nilai = float(input("Masukkan Nilai: "))
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus di antara 0-100!")

            return nama, nim, nilai
        except ValueError as e:
            print(f"Input tidak valid: {e}")
            return None

    @staticmethod
    def display_table(data):
        if not data:
            print("\nData kosong.")
            return

        print("\nDaftar Nilai Mahasiswa:")
        print("=" * 40)
        print(f"{'Nama':<15} {'NIM':<10} {'Nilai':<5}")
        print("-" * 40)
        for item in data:
            print(f"{item['Nama']:<15} {item['NIM']:<10} {item['Nilai']:<5}")
        print("=" * 40)