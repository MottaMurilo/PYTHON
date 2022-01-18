# Caso o valor seja divisivel por 2, imprima 'fizz', caso seja por 5, imprima 'buzz', caso seja 5 e 3, imprima 'fizz buzz'
# Caso contrário, imprima o (valor)

def fizz()
 valor = int(input('Digite um valor: '))
  
  if valor % 2 == 0:
    print('Fizz')
    
  elif valor % 5 == 0:
    print ('Buzz')
   
  elif valor % 5 == 0 and valor % 3 == 0:
    print('Fizz Buzz')
    
  else:
    print(valor)

fizz()
