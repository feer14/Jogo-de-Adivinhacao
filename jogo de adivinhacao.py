print("**********")
print("Bem Vindo ao jogo de Adivinhação!")
print("**********")
numero_secreto = 50 
total_de_tentativas = 5
rodadas = 2 

while(rodada >= total_de_tentativas):
    print("Tentativa{} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número:")
    print("Você digitou:", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

     if (acertou ):
    print("Parabens Você acertou!")
    else:
    if(maior):
        print ("O seu chute é maior que o número secreto!")
    elif(menor):   
        print("O seu chute é menor que o número secreto!")

    rodada =  rodada + 2
    
   print("Fim de jogo")
