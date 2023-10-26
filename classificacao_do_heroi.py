nome = input("Qual é o nome do herói? ")
xp = int(input("Qual é o a quantidade de XP do herói? "))
if(xp <= 1000):
    nivel = "Ferro"
elif(xp <= 2000):
    nivel = "Bronze"
elif(xp <= 5000):
    nivel = "Prata"
elif(xp <= 7000):
    nivel = "Ouro"
elif(xp <= 8000):
    nivel = "Platina"
elif(xp <= 9000):
    nivel = "Ascendente"
elif(xp <= 10000):
    nivel = "Imortal"
else:
    nivel = "Radiante"
print(f"O herói de nome {nome} está no nível de {nivel}")
#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 6.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante]