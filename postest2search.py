# list yang akan dicari
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# fungsi binary search untuk mencari nilai name pada list var
def binary_search(name, var):
    # set nilai awal untuk indeks kiri (left) dan kanan (right)
    left = 0
    right = len(var) - 1

    # loop hingga indeks kiri (left) lebih kecil atau sama dengan indeks kanan (right)
    while left <= right:
        # cari nilai tengah (mid) dari indeks kiri dan kanan
        mid = (left + right) // 2

        # jika nilai pada indeks mid adalah sebuah list
        if isinstance(var[mid], list):
            # jika nilai name lebih besar dari nilai terakhir pada list tersebut, set indeks kiri ke mid + 1
            if name > var[mid][-1]:
                left = mid + 1
            # jika nilai name lebih kecil dari nilai pertama pada list tersebut, set indeks kanan ke mid - 1
            elif name < var[mid][0]:
                right = mid - 1
            # jika nilai name ditemukan pada list, kembalikan indeks dengan menggunakan rumus mid * len(var) + i
            else:
                for i in range(len(var[mid])):
                    if var[mid][i] == name:
                        return mid * len(var) + i
        # jika nilai pada indeks mid bukan sebuah list
        else:
            # jika nilai name lebih kecil dari nilai pada indeks mid, set indeks kanan ke mid - 1
            if name < var[mid]:
                right = mid - 1
            # jika nilai name lebih besar dari nilai pada indeks mid, set indeks kiri ke mid + 1
            elif name > var[mid]:
                left = mid + 1
            # jika nilai name ditemukan pada list, kembalikan nilai indeks mid
            else:
                return mid


# list nama yang akan dicari pada list var menggunakan binary search
nama = ["Arsel", "Avivah", "Daiva", "Wahyu", "Wibi"]

# loop untuk mencari setiap nama pada list nama menggunakan binary search
for n in nama:
    # panggil fungsi binary search untuk mencari indeks dari nama tersebut pada list var
    index = binary_search(n, var)
    # jika indeks ditemukan, cari baris dan kolom dari nilai tersebut
    if isinstance(index, int):
        # hitung baris dan kolom menggunakan rumus index // len(var) dan index % len(var[i])
        i = index // len(var)
        a = index % len(var[i])
        # jika nilai pada indeks i adalah sebuah list
        if isinstance(var[i], list):
            print("Elemen",n, "berada pada index ke", i, "di kolom", a)
        # jika nilai pada indeks i bukan sebuah list
        else:
            print("Elemen",n, "berada pada index ke", a)


#############################################################################################################################

print("="*35)
# list yang akan dicari
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def fibonacciSearch(var, x):

    n = len(var)
    # Menentukan nilai awal variabel untuk algoritma Fibonacci Search
    fib2 = 0  # fib(n-2)
    fib1 = 1  # fib(n-1)
    fibn = fib1 + fib2  # fib(n)

    # Mencari bagian dari list yang mengandung elemen yang dicari
    while fibn < n:
        fib2, fib1 = fib1, fibn
        fibn = fib1 + fib2

    # Melakukan pencarian pada bagian dari list yang dipilih
    offset = -1
    while fibn > 1:
        i = min(offset + fib2, n - 1)
        if var[i] < x:
            fibn, fib1 = fib1, fib2
            fib2 = fibn - fib1
            offset = i
        elif var[i] > x:
            fibn, fib1 = fib2, fib1 - fib2
            fib2 = fibn - fib1
        else:
            return i

    # Jika elemen tidak ditemukan
    if fib1 and var[offset + 1] == x:
        return offset + 1
    else:
        return -1


# Mencari indeks dari setiap elemen dalam list var
for i in range(len(var)):
    # Memeriksa apakah elemen pada indeks ke-i merupakan sebuah list
    nama = var[i]
    if isinstance(nama, list):
        # Jika elemen merupakan list, maka dilakukan iterasi pada setiap elemen di dalamnya
        for column in range(len(nama)):
            item = nama[column]
            idx = fibonacciSearch(nama, item) # Mencari indeks dari elemen tersebut di dalam list
            if idx != -1:  # Jika ditemukan
                print(f"Elemen '{item}' berada pada index ke {i} di kolom {column}")
    # Jika elemen bukan list, maka langsung mencari indeks dari elemen tersebut di dalam list            
    else:
        idx = fibonacciSearch(var, nama)
        if idx != -1:
            print(f"Elemen '{nama}' berada pada index ke {i}")