from random import randint
import os

#comando usado para limpar a tela
def limpar():
    os.system("cls")

acertos=0

#laco do programa principal
while True:

    #sorteia um numero para ser verificado a raiz
    resposta_correta=randint(1,100)
    limpar()
    questao=f"Qual é a raiz de {resposta_correta**2}"
    print(questao)

    #tratamento de erro da resposta
    while True:

        try:

            resposta_dada=input("Digite a sua resposta:")
            resposta_dada=int(resposta_dada)

            #verifica se a resposta está no intervalo válido
            if 0 < resposta_dada < 101:
                break
        except:
            pass
        
        #reiprime os pints caso a entrada não seja válida
        limpar()
        print(questao)
        print(f"Resposta {resposta_dada} não é válido")
    
    #verifica se a resposta é correta
    if resposta_dada == resposta_correta:
        acertos+=1
        continue
    break
    
#mensagem de quando erra a questão
limpar()
print(f"Você teve {acertos} acertos")
print(resposta_correta)
