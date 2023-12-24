from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento'))
idade = atual - nasc
if(idade<= 9):
    print('Mirim')
elif(idade<=19):
    print('Junior')
elif(idade<=25):
    print('Sênior')
elif(idade>25):
    print('Master')


