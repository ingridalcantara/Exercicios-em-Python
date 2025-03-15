# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15% 
salario = float(input('Salário atual: R$'))
novo_sal = salario + (15/100)*salario
print(f'O novo salário com aumento de 15% será R$ {novo_sal:.2f}')