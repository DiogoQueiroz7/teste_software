print('=============== SISTEMA DE MÉDIAS BIMESTRAIS ===============')

while True:
    nota_str = input('Digite a primeira nota do bimestre: ').replace(',', '.')

    if nota_str.replace('.', '', 1).isdigit():
        nota_1 = float(nota_str)
        
        if 0 <= nota_1 <= 10:
            break  
        else:
            print("[ERRO]: A nota deve ser um número entre 0 e 10.")
    else:
        print("[ERRO] Por favor, digite um número.")

while True:
    nota_str = input('Digite a segunda nota do bimestre: ').replace(',', '.')

    if nota_str.replace('.', '', 1).isdigit():
        nota_2 = float(nota_str)
        
        if 0 <= nota_2 <= 10:
            break
        else:
            print("[ERRO]: A nota deve ser um número entre 0 e 10.")
    else:
        print("[ERRO]: Entrada inválida. Por favor, digite um número.")

soma = nota_1 + nota_2
media = soma / 2

if media >= 6:
    print(f'Parabéns! Sua média foi de {media:.1f}. Você está APROVADO!!')
elif 3 <= media <= 5.9:
    print(f"Cuidado! Sua média foi de {media:.1f}. Você está de EXAME!")
else:
    print(f'Que pena! Sua média foi de {media:.1f}. Você está REPROVADO!')


print("==================== OBRIGADO POR USAR O SISTEMA ====================")