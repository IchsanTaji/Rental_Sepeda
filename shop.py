from datetime import datetime


class Shop:
    def __init__(self, stock=1):
        self.stock = stock if stock > 0 else 1 # Mengatur stok awal

    # Mengembalikan stok dari parameter
    @property
    def get_stock(self):
        return self.stock

    # Penyewaan Sepeda
    def rentBike(self, n_bikes=1):
        now = datetime.now() # Menandakan waktu saat ini

        if n_bikes >= 1:
            new_stock = self.stock - n_bikes # Mengganti jumlah sepeda yang disewa
            self.stock = new_stock # New stock
            return now
        else:
            raise ValueError # Menampilkan error untuk nilai yang tidak valid misalnya 0

    # Mengembalikan tagihan
    def issueBill(self, return_request=None):
        if return_request != None:
            rentalTime, num_of_bikes, rentalRate = return_request # Jumlah waktu sewa, sepeda dan tarif sewa

            if rentalRate == 1: # Per Jam
                bill = round(rentalTime.seconds / 3600) * 5 * num_of_bikes
            elif rentalRate == 2: # Per Hari
                bill = round(rentalTime.days) * 10 * num_of_bikes
            elif rentalRate == 3: # If it's weekly
                bill = round(rentalTime.days / 7) * 30 * num_of_bikes
            else:
                raise ValueError

            if num_of_bikes >= 3:
                bill *= 0.7 # Menerapkan diskon

            new_stock = self.stock + num_of_bikes # Sama seperti di atas
            self.stock = new_stock # Menetapkan stok baru
            return round(bill)
        else:
            return None


class Customer():
    def __init__(self): # nilai-nilai ini bisa diganti
        self.rentalBasis = 0
        self.rented_bikes = 0

    # Mengirim permintaan sewa
    # Fungsi ini berjalan dengan metode rentBike()
    def requestBike(self, rentalBasis=1, n_bikes=1):
        if 1 <= rentalBasis <= 3 and n_bikes >= 1:
            self.rentalBasis = rentalBasis
            self.rented_bikes = n_bikes
            return self.rentalBasis, self.rented_bikes # Mengembalikan parameter
        else:
            raise ValueError
    
    @property
    def num_of_bikes(self):
        return self.rented_bikes
        
    @property
    def rental_basis(self):
        return self.rental_basis
    
    # Pelanggan mengembalikan sepeda
    def returnBike(self, when_rented=None):
        if when_rented != None:
            rented_time = datetime.now() - when_rented
            return rented_time, self.rented_bikes, self.rentalBasis # Mengembalikan permintaan untuk issue_bill()
        else:
            return None
