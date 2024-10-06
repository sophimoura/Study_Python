A = 0
B = int(input ( 'Digite um número: '))
def div(B):  #função 
    resultado = [i for i in range(1, B + 1) 
    if B % i == 0]
    return resultado 
Div = (div(B))
print (Div)
for d in Div: 
  while A < sum(Div):
   A += d
print (A) 