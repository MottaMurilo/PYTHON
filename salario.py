salario = int(input('Quanto você ganha por mês?'))
imposto_renda = salario*0.11
inss = salario*0.08
sindicato = salario*0.05

salario_liquido = salario-inss-imposto_renda-sindicato

print(f'Seu salário bruto é {salario}, com os descontos sobra {salario_liquido}')