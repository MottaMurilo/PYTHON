hora = int(input())

if hora >= 0 and hora <= 11:
    print('Bom dia!')

elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
    
elif hora > 24:
    print('Erro!')

else:
    print('Boa noite!')
