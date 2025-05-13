lado_1 = float(input("digite o valor do lado 1:"))
lado_2 = float(input("digite o valor do lado 2:"))
lado_3 = float(input("digite o valor do lado 3:"))  
 
real1 = lado_1 + lado_2 > lado_3

real2 = lado_1 > lado_2 +lado_3 

real3 = lado_2 + lado_1 >lado_3 

if real1 or real2 or real3: 
    print("Permitido") 
else : 
    print
