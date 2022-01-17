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
