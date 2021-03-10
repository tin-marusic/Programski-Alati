while True:
    try:
        x = int(input("Unesite prvi x: "))
        y = int(input("Unesite prvi y: "))
    except ValueError:
        print("Netočan unos,unesite ponovo! Napomena x i y moraju biti cijeli brojevi")
        continue
    else:
        break

while True:
    try:
        x2 = int(input("Unesite drugi x: "))
        y2 = int(input("Unesite drugi y: "))
    except ValueError:
        print("Netočan unos,unesite ponovo! Napomena x i y moraju biti cijeli brojevi")
        continue
    else:
        break

nagib = (y2-y)/(x2-x)
nagib = round(nagib,3)
sl_koeficjent = -x*nagib + y
if sl_koeficjent>0:
    sl_koeficjent = str(sl_koeficjent)
    sl_koeficjent = "+ " + sl_koeficjent
print (f"y = {nagib}x {sl_koeficjent}")