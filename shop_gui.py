import tkinter as tk
from shop import Shop, Customer

# Root window
root = tk.Tk()

# Daftar Opsi
optionList = ['Per Jam', 'Harian', 'Mingguan']

# Variabel Toko dan Pelanggan
customer = Customer()
shop = Shop(stock=10)
global when_rented

# metode Switch-like untuk mendapatkan OptionMenu index
def get_list_index(argument):
    switcher = {
        'Per Jam': 1,
        "Harian": 2,
        "Mingguan": 3,
    }
    return switcher.get(argument)

# kegunaan return_bike
def rent_bike():
    global when_rented

    if bike_entry.get() == "":
        set_status("Tidak Boleh Kosong(0)!", "red") # Apabila nilai kosong, akan menunjukkan tulisan tersebut
    else:
        try:
            num_of_bikes = int(bike_entry.get()) # Apabila bukan angka
        except ValueError:
            set_status("Masukkan Angka!", "red") # Akan muncul peringatan untuk memasukkan angka

        # Status tombol
        if rent_button['state'] == tk.NORMAL:
            rent_button['state'] = tk.DISABLED
        
        if return_button['state'] == tk.DISABLED:
            return_button['state'] = tk.NORMAL

        # Menggunakan metode get_list_index
        rental_basis = get_list_index(variable.get())
        
        # Penyewaan sepeda sebenarnya
        customer.requestBike(rental_basis, num_of_bikes)
        when_rented = shop.rentBike(customer.num_of_bikes)

        # Update stock label
        display_stock()

def return_bike():
    return_request = customer.returnBike(when_rented)
    bill = shop.issueBill(return_request)

    # Mengembalikan tagihan
    set_status(f"Tagihanmu adalah {bill}", "green")

    # Status tombol
    if return_button['state'] == tk.NORMAL:
        return_button['state'] = tk.DISABLED

    if rent_button['state'] == tk.DISABLED:
        rent_button['state'] = tk.NORMAL
    
    display_stock()

def set_status(message, color="black"):
    status = tk.Label(root, text=message, fg=color)
    status.grid(row=2, column=0)

def display_stock():# Tampilan Stok
    stock_label = tk.Label(root, text=f"Stok dalam Toko: {shop.stock}")
    stock_label.grid(row=4, column=0)

# variabel Tkinter
variable = tk.StringVar(root)
variable.set(optionList[0])

# Baris pertama
bike_label = tk.Label(root, text="Masukkan Jumlah Sepeda:")
bike_entry = tk.Entry(root)

# Baris kedua
rental_label = tk.Label(root, text="Pilih opsi berapa lama:")
rental_list = tk.OptionMenu(root, variable, *optionList)

# Baris Ketiga
rent_button = tk.Button(root, text='Rental', command=rent_bike)
return_button = tk.Button(root, text='Kembalikan', command=return_bike, state=tk.DISABLED)

# Elemen tampilan
bike_label.grid(row=0, column=0)
bike_entry.grid(row=0, column=1)

rental_label.grid(row=1, column=0)
rental_list.grid(row=1, column=1)

# * Ini baris keempat karena label akan disisipkan nanti di
# baris ketiga yang sebenarnya
rent_button.grid(row=3, column=0)
return_button.grid(row=3, column=1)

# Tampilan stok
display_stock()

# Main loop
root.mainloop()
