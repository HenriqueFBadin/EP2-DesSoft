import math

def haversine(r, fi1, lamb1, fi2, lamb2):
    f1=math.radians(fi1)
    f2=math.radians(fi2)
    l1=math.radians(lamb1)
    l2=math.radians(lamb2)
    a1=((f2-f1)/2)
    a2=(math.sin(a1))**2
    a3=((l2-l1)/2)
    a4=(math.sin(a3))**2
    a5=math.cos(f1)*math.cos(f2)*a4
    a6=math.sqrt(a2+a5)
    d=2*r*math.asin(a6)
    return d
    
#FIM