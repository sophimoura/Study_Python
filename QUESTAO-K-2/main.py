print ('Cálculo Soma dos divisores de um número ')
K = int(input('Digite o número que deseja fatorar: '))
for i in range(1,K+1):
  if K % i==0:
    print (i)
S= i+1