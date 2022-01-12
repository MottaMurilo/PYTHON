salario_bruto = int(input('Quanto você ganha por mês?'))

imposto_renda = salario*0.11 #11% de  IR

inss = salario*0.08 #8% do INSS

sindicato = salario*0.05 #5% do sindicato

salario_liquido = salario-inss - imposto_renda - sindicato

print(f'Seu salário bruto é {salario_bruto}, com os descontos fica {salario_liquido}!')
