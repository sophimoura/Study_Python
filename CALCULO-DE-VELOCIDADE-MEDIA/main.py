print ('P2 Informática - Python')
print ('Equipe Thalita, Sophia, Sure e Isabelly')
print ('CALCULDORA DE VELOCIDADE MÉDIA ')
Km = int(input(' Informe a distância em Km:'))
t = int(input('Informe o tempo em horas:'))
Vm = (Km/t)
print ('A velocidade média é de:', Vm )
print ('Km/t')
if Vm<= 80: 
  print ('Você está na velocidade permitida!')
else:
  print('Você ultrapassou a velocidade!')
  
