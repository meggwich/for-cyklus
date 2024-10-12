width = int(input('?'))
height = int(input('?'))
word = input('?')
delimiters = input('?')
string = ''
n = '\n'

# Vytvorenie premenných pre ďalšie akcie
l1, word1, l2, word2, l3, word3, l4, word4, l5, l6, d1, d2 = '', '', '', '', '', '', '', '', '', '', '', ''
counter = 0
v = 0
z = 0
f = 0
q = 6

# Uloženie reťazca a oddeľovačov do samostatných premenných
r = 1
for letter in word:
    r -= 1
    for i in range(1):
        l1 += f'{letter * int((r - 1) * (r - 2) / 2)}'
        word1 += f'{letter * int(r * (r - 2) / (-1))}'
        r = 2

r = 1
for letter in word1:
    r -= 1
    for i in range(1):
        l2 += f'{letter * int((r - 1) * (r - 2) / 2)}'
        word2 += f'{letter * int(r * (r - 2) / (-1))}'
        r = 2

r = 1
for letter in word2:
    r -= 1
    for i in range(1):
        l3 += f'{letter * int((r - 1) * (r - 2) / 2)}'
        word3 += f'{letter * int(r * (r - 2) / (-1))}'
        r = 2

r = 1
for letter in word3:
    r -= 1
    for i in range(1):
        l4 += f'{letter * int((r - 1) * (r - 2) / 2)}'
        word4 += f'{letter * int(r * (r - 2) / (-1))}'
        r = 2

r = 1
for letter in word4:
    r -= 1
    for i in range(1):
        l5 += f'{letter * int((r - 1) * (r - 2) / 2)}'
        l6 += f'{letter * int(r * (r - 2) / (-1))}'
        r = 2

r = 1
for delimiter in delimiters:
    r -= 1
    for i in range(1):
        d1 += f'{delimiter * int((r - 1) * (r - 2) / 2)}'
        d2 += f'{delimiter * int(r * (r - 2) / (-1))}'
        r = 2

# Premenné-invertory pre jednotlivé prípady (width = 1, 2 a height = 1)
# Invertujú informácie podľa vzoru int(((f + n) / (f + n + 1)) + 1 / (n + 2)), ktorý vracia False pre výraz f = 0
# Takto je možné overiť rovnosť a = b, kde f = a - b
j = int(((width - 1) + 2) / ((width - 1) + 3) + 1 / 4)
i = int(((width - 2) + 3) / ((width - 2) + 4) + 1 / 5)
h = int(((height - 1) + 2) / ((height - 1) + 3) + 1 / 4)

# Cyklus pre všetky prípady okrem width = 1, 2 a height = 1 (vykonávajú sa samostatne)
# Cyklus po radoch sa vykonáva, ak j = i = h = 1, t.j. nie sú dotknuté špeciálne prípady
for i in range(height * j * i * h):

    # Počítadlo pre striedanie oddeľovačov
    counter = counter % 2

    # Vďaka premennej v, prvý priechod cyklu po riadkoch preskočí tento cyklus
    # Tento cyklus tlačí časť reťazca umiestnenú na konci riadku
    for b in range(12 - 2 * f, 12):

        counter += 0.5
        counter = counter % 2

        # Premenné vracajú jednotku alebo nulu v závislosti od hodnoty b. Označujú, kedy je rad na akom znaku
        k1 = int(((b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -39916800))
        k2 = int((b * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 3628800))
        k3 = int((b * (b - 1) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -725760))
        k4 = int((b * (b - 1) * (b - 2) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 241920))
        k5 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -120960))
        k6 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 86400))
        k7 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -86400))
        k8 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 120960))
        k9 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 9) * (b - 10) * (b - 11) / -241920))
        k10 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 10) * (b - 11) / 725760))
        k11 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 11) / -3628800))
        k12 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) / 39916800))

        # Kontrola, či je dĺžka reťazca, ktorý bude na konci aktuálneho riadku, deliteľná šiestimi
        c = int((((i * 2 * width + b - 12 + 2 * f + 1) % (2 * width * height)) + 1) / (((i * 2 * width + b - 12 + 2 * f + 1) % (2 * width * (i + 1))) + 2) + 1 /3) % 6
        z = 1 - int((((2 * height * width - (len(string) + 1)) + 1) / ((2 * height * width - (len(string) + 1)) + 2)) + 1/3)

        # Zlepenie s hlavným reťazcom pre výstup
        string += f'{v * (l1 * k1 + (d1 * int(counter) + d2 * (1 - int(counter))) * k2 * int((z - 1) / (-1)) + n * z + l2 * k3 + (d1 * int(counter) + d2 * (1 - int(counter))) * k4 * int((z - 1) / (-1)) + n * z + l3 * k5 + (d1 * int(counter) + d2 * (1 - int(counter))) * k6 * int((z - 1) / (-1)) + n * z + l4 * k7 + (d1 * int(counter) + d2 * (1 - int(counter))) * k8 * int((z - 1) / (-1)) + n * z + l5 * k9 + (d1 * int(counter) + d2 * (1 - int(counter))) * k10 * int((z - 1) / (-1)) + n * z + l6 * k11 + (d1 * int(counter) + d2 * (1 - int(counter))) * k12 * int((z - 1) / (-1)) * c + n * z + n * (1 - c))}'

    v = 1

    # Cyklus tlačí celé fragmenty 6-znakového reťazca v závislosti od už vytlačenej časti riadku a zadanej dĺžky pre každý riadok
    for a in range((2 * width - 2 * f) // 12):
        
        counter += 1
        counter = int(counter % 2)
        
        x = int((((a * 6 + (f + 6)) % (width)) + 1) / ((((a * 6 + (f + 6)) % (width))) + 2) + 1 /3)
        
        string += f'{l1 + (d1 * counter + d2 * (1 - counter)) + l2 + (d2 * counter + d1 * (1 - counter)) + l3 + (d1 * counter + d2 * (1 - counter)) + l4 + (d2 * counter + d1 * (1 - counter)) + l5 + (d1 * counter + d2 * (1 - counter)) + l6 + (d2 * counter + d1 * (1 - counter)) * x + n * (1 - x)}'

        counter += 1

    # Premenné q a f slúžia na uloženie informácií o tom, koľko znakov budú obsahovať necelé fragmenty na začiatku a na konci
    q =  (width - f) % 6
    f = (6 - q) % 6
    
    counter += 1
    counter = counter % 2

    # Cyklus pre necelý fragment na začiatku riadku
    for b in range(2 * q):
        
        counter += 0.5
        counter = counter % 2
        
        k1 = int(((b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -39916800))
        k2 = int((b * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 3628800))
        k3 = int((b * (b - 1) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -725760))
        k4 = int((b * (b - 1) * (b - 2) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 241920))
        k5 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -120960))
        k6 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 86400))
        k7 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -86400))
        k8 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 120960))
        k9 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 9) * (b - 10) * (b - 11) / -241920))
        k10 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 10) * (b - 11) / 725760))
        k11 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 11) / -3628800))
        k12 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) / 39916800))
        
        t1 = int((q - 2) / (-1) * (q - 3) / (-2) * (q - 4) / (-3) * (q - 5) / (-4) * (q - 6) / (-5))
        t2 = int((q - 1) * (q - 3) / (-1) * (q - 4) / (-2) * (q - 5) / (-3) * (q - 6) / (-4))
        t3 = int((q - 2) * (q - 1) / 2 * (q - 4) / (-1) * (q - 5) / (-2) * (q - 6) / (-3))
        t4 = int((q - 2) / 2 * (q - 3) * (q - 1) / 3 * (q - 5) / (-1) * (q - 6) / (-2))
        t5 = int((q - 2) / 3 * (q - 3) / 2 * (q - 4) * (q - 1) / 4 * (q - 6) / (-1))
        t6 = int((q - 2) / 4 * (q - 3) / 3 * (q - 4) / 2 * (q - 5) * (q - 1) / 5)
        
        string += f'{l1 * k1 + (d2 * int(counter) + d1 * (1 - int(counter))) * k2 * int((t1 - 1) / -1) + n * k2 * t1 + l2 * k3 + (d2 * int(counter) + d1 * (1 - int(counter))) * k4 * int((t2 - 1) / -1)  + n * k4 * t2 + l3 * k5 + (d2 * int(counter) + d1 * (1 - int(counter))) * k6 * int((t3 - 1) / -1) + n * k6 * t3 + l4 * k7 + (d2 * int(counter) + d1 * (1 - int(counter))) * k8 * int((t4 - 1) / -1) + n * k8 * t4 + l5 * k9 + (d2 * int(counter) + d1 * (1 - int(counter))) * k10 * int((t5 - 1) / -1) + n * k10 * t5 + l6 * k11 + (d2 * int(counter) + d1 * (1 - int(counter))) *k12 * int((t6 - 1) / -1) + n * k12 * t6}' 


#Cyklus pre width = 1
for y in range(height * (1 - j)):
    y = y % 6 + 1
    t1 = int((y - 2) / (-1) * (y - 3) / (-2) * (y - 4) / (-3) * (y - 5) / (-4) * (y - 6) / (-5))
    t2 = int((y - 1) * (y - 3) / (-1) * (y - 4) / (-2) * (y - 5) / (-3) * (y - 6) / (-4))
    t3 = int((y - 2) * (y - 1) / 2 * (y - 4) / (-1) * (y - 5) / (-2) * (y - 6) / (-3))
    t4 = int((y - 2) / 2 * (y - 3) * (y - 1) / 3 * (y - 5) / (-1) * (y - 6) / (-2))
    t5 = int((y - 2) / 3 * (y - 3) / 2 * (y - 4) * (y - 1) / 4 * (y - 6) / (-1))
    t6 = int((y - 2) / 4 * (y - 3) / 3 * (y - 4) / 2 * (y - 5) * (y - 1) / 5)
    string += f'{l1 * t1 + l2 * t2 + l3 * t3 + l4 * t4 + l5 * t5 + l6 * t6 + n}'


#Cyklus pre width = 2
counter = 0

for y in range(h * j * height * (1 - i)):
    
    counter += 1
    
    y = 2 * y % 6 + 1
    
    t1 = int((y - 2) / (-1) * (y - 3) / (-2) * (y - 4) / (-3) * (y - 5) / (-4) * (y - 6) / (-5))
    t2 = int((y - 1) * (y - 3) / (-1) * (y - 4) / (-2) * (y - 5) / (-3) * (y - 6) / (-4))
    t3 = int((y - 2) * (y - 1) / 2 * (y - 4) / (-1) * (y - 5) / (-2) * (y - 6) / (-3))
    t4 = int((y - 2) / 2 * (y - 3) * (y - 1) / 3 * (y - 5) / (-1) * (y - 6) / (-2))
    t5 = int((y - 2) / 3 * (y - 3) / 2 * (y - 4) * (y - 1) / 4 * (y - 6) / (-1))
    t6 = int((y - 2) / 4 * (y - 3) / 3 * (y - 4) / 2 * (y - 5) * (y - 1) / 5)
    
    string += f'{l1 * t1 + l2 * t2 + l3 * t3 + l4 * t4 + l5 * t5 + l6 * t6}'
    
    string += f'{d1 * (counter % 2) + d2 * (1 - (counter % 2))}'
    
    y += 1
    
    t1 = int((y - 2) / (-1) * (y - 3) / (-2) * (y - 4) / (-3) * (y - 5) / (-4) * (y - 6) / (-5))
    t2 = int((y - 1) * (y - 3) / (-1) * (y - 4) / (-2) * (y - 5) / (-3) * (y - 6) / (-4))
    t3 = int((y - 2) * (y - 1) / 2 * (y - 4) / (-1) * (y - 5) / (-2) * (y - 6) / (-3))
    t4 = int((y - 2) / 2 * (y - 3) * (y - 1) / 3 * (y - 5) / (-1) * (y - 6) / (-2))
    t5 = int((y - 2) / 3 * (y - 3) / 2 * (y - 4) * (y - 1) / 4 * (y - 6) / (-1))
    t6 = int((y - 2) / 4 * (y - 3) / 3 * (y - 4) / 2 * (y - 5) * (y - 1) / 5)
    
    string += f'{l1 * t1 + l2 * t2 + l3 * t3 + l4 * t4 + l5 * t5 + l6 * t6 + n}'


#Cyklus pre height = 1
for y in range(j * (1 - h)):
    
    for b in range(2 * width):
        
        counter += 1
        
        u = int(((2 * width - b - 1) + 1) / ((2 * width - b - 1) + 2) + 1 / 3)
        
        b = b % 12
        
        k1 = int(((b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -39916800))
        k2 = int((b * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 3628800))
        k3 = int((b * (b - 1) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -725760))
        k4 = int((b * (b - 1) * (b - 2) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 241920))
        k5 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -120960))
        k6 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 86400))
        k7 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 7) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / -86400))
        k8 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 8) * (b - 9) * (b - 10) * (b - 11) / 120960))
        k9 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 9) * (b - 10) * (b - 11) / -241920))
        k10 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 10) * (b - 11) / 725760))
        k11 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 11) / -3628800))
        k12 = int((b * (b - 1) * (b - 2) * (b - 3) * (b - 4) * (b - 5) * (b - 6) * (b - 7) * (b - 8) * (b - 9) * (b - 10) / 39916800))
        
        string += f'{u * (l1 * k1 + d1 * k2 + l2 * k3 + d2 * k4 + l3 * k5 + d1 * k6 + l4 * k7 + d2 * k8 + l5 * k9 + d1 * k10 + l6 * k11 + d2 * k12)}'

    
print(string)


