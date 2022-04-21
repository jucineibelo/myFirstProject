ganhoHora = float(input("Informe qual o valor da remuneração por hora? "))
horasTrabalhadas = float(input("Informe quantas horas você trabalhou no mês? "))
salarioBruto = ganhoHora * horasTrabalhadas

#Calculo INSS
inss = 0
if salarioBruto <= 1212:
    inss = 7.5
elif salarioBruto <= 2427.35:
    inss = 9
elif salarioBruto <= 3641.03:
    inss = 12
elif salarioBruto <= 7087.22:
    inss = 14
inss = salarioBruto * (inss / 100)
#Calculo IR
ir = 0
if salarioBruto <= 1903.98:
    ir = 0
elif salarioBruto <= 2826.65:
    ir = 7.5
elif salarioBruto <= 3751.05:
    ir = 15
elif salarioBruto <= 4664.68:
    ir = 22.5
elif salarioBruto >= 4664.69:
    ir = 27.5
ir = salarioBruto * (ir/ 100)
#Calculo Salario Liquido
salarioLiquido = salarioBruto - inss - ir

print("----------- FOLHA DE PAGAMENTO EMPRESA FULLSTACK NINJA LTDA -----------")
print('\n')
print("Seu salário Bruto é de R$: ",salarioBruto)
print("Foram descontados R$:",inss,"de INSS sob seu salário.")
print("Foram descontados R$:",ir,"de IR sob seu salário.")
print("O valor de seu salário liquido é de R$:",salarioLiquido, "Aproveite e faça bons gastos")
print(2*'\n')
print("----------- A EMPRESA FULL STACK TEM O PRAZER DE TER VOCÊ COMO COLABORADOR -----------")


