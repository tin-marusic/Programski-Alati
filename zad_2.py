def pravac(x,y,x2,y2):

    nagib = (y2-y)/(x2-x)
    nagib = round(nagib,3)
    sl_koeficjent = -x*nagib + y
    if sl_koeficjent>0:
        sl_koeficjent = str(sl_koeficjent)
        sl_koeficjent = "+ " + sl_koeficjent
    print (f"y = {nagib}x {sl_koeficjent}")

pravac(12,23,11,64)