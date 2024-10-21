from scipy.optimize import linprog

# Koefisien fungsi objektif (biaya)
c = [10, 8]

# Matriks koefisien kendala
A = [[-3, -2], [-2, -4]]  # Perhatikan tanda negatif karena kita mencari nilai minimal

# Vektor nilai kanan kendala
b = [-18, -24]

# Batasan bawah dan atas untuk variabel
bounds = [(0, float('inf')), (0, float('inf'))]

# Selesaikan masalah program linear
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

# Cetak hasil
print("Jumlah bahan pakan A:", res.x[0])
print("Jumlah bahan pakan B:", res.x[1])
print("Biaya minimum:", res.fun)