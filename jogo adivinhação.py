from random import randint
print ('='*30)
print ("Estou pensando em um numero entre 0 e 10 , tente adivinhar qual!!\n")

computador = randint(0,10)

jogador = int(input("Digite seu palpite:"))

if computador == jogador:
    print("Parabéns voce acertou o numero que pensei")
else:
    print(" voce errou :( \n eu estava pensando em {} e voce digitou {}!".format(computador , jogador)) #nn

print ("="*30)
