print('=============== SISTEMA DE MÉDIAS BIMESTRAIS ===============')

nota_1 = float(input('Digite a primeira nota: ').replace(',', '.'))
while nota_1 < 0 or nota_1 > 10:
    print("[ERRO] A nota deve ser entre 0 e 10.")
    nota_1 = float(input('Digite a primeira nota: ').replace(',', '.'))

nota_2 = float(input('Digite a segunda nota: ').replace(',', '.'))
while nota_2 < 0 or nota_2 > 10:
    print("[ERRO] A nota deve ser entre 0 e 10.")
    nota_2 = float(input('Digite a segunda nota: ').replace(',', '.'))

soma = nota_1 + nota_2
media = soma / 2

if media >= 6:
    print(f'\nParabéns! Sua média foi de {media:.1f}. Você está APROVADO!!')
elif 3 <= media <= 5.9:
    print(f"\nCuidado! Sua média foi de {media:.1f}. Você está de EXAME!")
else:
    print(f'\nQue pena! Sua média foi de {media:.1f}. Você está REPROVADO!')

print("\n==================== OBRIGADO POR USAR O SISTEMA ====================")