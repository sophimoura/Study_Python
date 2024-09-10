def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

print('CALCULADORA DE MÉDIAS!') 
print( 'CÁLCULO DA MÉDIA DA N1')
N1_1 = float(input('Insira sua nota da N1.1: ')) 
N1_2 = float(input('Insira sua nota da N1.2: '))
Soma = N1_1 + N1_2
M_C3_A9dia_N1 = Soma / 2
print('Sua média da N1:  ' + str(M_C3_A9dia_N1))
print('CÁLCULO DA MÉDIA DA N2')
N2_1 = float(input('Insira sua da nota N2.1: '))
N2_2 = float(input('Insira sua da nota N2.2: '))
Soma = N2_1 + N2_2
M_C3_A9dia_N2 = Soma / 2
print('Sua média da N2:  ' + str(M_C3_A9dia_N2))
print('CÁLCULO DA MÉDIA PARCIAL (MP)')
Res__1 = M_C3_A9dia_N1 * 2
print(' (Resultado da multiplicação da N1 por 2) ' + str(Res__1))
Res__2 = M_C3_A9dia_N2 * 3
print(' (Resultado da multiplicação da N2 por 3) ' + str(Res__2))
Res__3 = Res__1 + Res__2
print(' (Resultado da soma das notas dividido por 5) ' + str(Res__3))
M_C3_A9dia_ponderada = Res__3 / 5
print(' Média Ponderada: ' + str(M_C3_A9dia_ponderada))
if M_C3_A9dia_ponderada >= 6:
  print('Você foi: APROVADO')
elif M_C3_A9dia_ponderada >= 3:
  print('Você deverá realizar a Avaliação Final (AF) para ober uma média de aprovação!') 
  AF = float(text_prompt('Insira sua nota da AF: '))
  Soma = AF + M_C3_A9dia_ponderada
  MF = Soma / 2
  if MF > 5: print('Você foi: APROVADO ')
  else: print('Você foi REPROVADO')
else: print( 'Você foi: REPROVADO ')