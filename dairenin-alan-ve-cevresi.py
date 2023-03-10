"""
    daire alanı  : pi*r**2
    daire çevresi: 2*pi*r
    
    * yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (pi:3.14)
"""

r  = float(input("yarı çap: "))
pi = 3.14

alan  = pi * r ** 2
cevre = 2 * pi * r

print("Alan: " , alan)
print("Çevre: ", cevre)
