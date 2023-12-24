from datetime import date 
atual= date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
dif = 18 - idade
print(f"quem nasceu em {nasc} tem {atual} anos em {idade}")
if (idade == 18):
    print('Voce tem que se alistar imediatamente')

elif(idade<18):
    print(f'Voce ainda não tem 18 anos faltam {dif} anos para o alistamento ')

elif(idade>18):
    dif = idade - 18
    print(f"Voce deveria ter se alistado há {dif} anos")
