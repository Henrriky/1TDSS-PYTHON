# DADOS
nome_paciente = "Hanielle"
idade = 30
peso = 64
altura = 1.80
batimentos = 110
temperatura = 35.7
pressao = 12.8
pontuacao = 0

#PROCESSAMENTO
imc = peso/altura**2
if (batimentos > 140 or batimentos <= 45) or (temperatura <= 34 or temperatura > 40.5) or (imc <= 15 or imc > 40) or (idade <= 1 or idade > 70):
    pontuacao = pontuacao + 10
elif ((batimentos > 45 and batimentos <= 60) or (batimentos > 115 or batimentos <= 140)) \
    or ((temperatura > 34 and temperatura <= 36) or (temperatura > 38 and temperatura <= 40.5)) \
    or (imc <= 20 and (imc > 32.5 and imc <= 40)) \
    or ((idade > 1 and idade <= 10) or (idade > 50 and idade <= 70)):
    pontuacao = pontuacao + 5
elif ((batimentos > 50 and batimentos <= 59) or (batimentos > 100 or batimentos <= 115)) \
    or ((temperatura > 35 and temperatura <= 35.9) or (temperatura > 37 and temperatura <= 38)) \
    or ((imc > 18 and imc <= 19.9) and (imc > 25 and imc <= 32.5)) \
    or ((idade > 8 and idade <= 18) or (idade > 40 or idade <= 50)):
    pontuacao = pontuacao + 1
elif (batimentos > 59 and batimentos <= 100) \
    or (temperatura > 35.9 or temperatura <= 37) \
    or (imc > 19 and imc <= 25) \
    or (idade > 18 or idade <= 40):
    pontuacao = pontuacao + 0
else: 
    print("Condição inválida")









# SAÍDA
if (pontuacao >= 10): 
    print("Emergência")
elif (pontuacao >= 5 and pontuacao < 10):
    print("Muito Urgente")
elif (pontuacao >= 2 and pontuacao < 5):
    print("Pouco urgente")
elif (pontuacao >= 0 and pontuacao < 2):
    print("Atendimento Normal")
else: 
    print("Opção Inválida")



