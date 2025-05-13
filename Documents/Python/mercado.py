produto = float(input("Digite o valor do item:"))
quantidade = 0 
total = 0.0

while produto != 0:

    quantidade = quantidade +1 
    total = total + produto
    produto = float(input("Digite o valor do item:"))

print (f"Quantidade:{quantidade}") 
print (f"Total:{total:.2f}")