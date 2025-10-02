#VALOR DA DIARIA DE UM CARRO É 60$
# 0.15$ POR KILOMETRO RODADO


diaria = float(input("Quantos dias o carro foi alugado :\n"))

diaria = float(60) * diaria

kmrodado = float(input("Quantos kilometros o carro andou durante o periodo de aluguel:"))

kmrodado = kmrodado * 0.15



valortotal = kmrodado +  diaria 

print(f"O valor total a ser pago é:{valortotal}")