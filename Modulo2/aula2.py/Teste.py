## Escreva e execute seu código aqui

salario_hora = 20
horas_semana = 40

#Salário semanal
salario_semanal = salario_hora * horas_semana

#Descontos
inss      = salario_semanal * 0.10 #INSS(10% do bruto)
sindicato = salario_semanal * 0.05  #Sindicato(5% do bruto)
descontos = inss + sindicato

#Salário líquido
salario_liquido = salario_semanal - descontos

#Saída
#print(f"O salário semanal bruto é de {salario_semanal}")
#print(f"O valor descontado pelo inss é de {inss}")
#print(f"O valor descontado pelo sindicato é de {sindicato}")
#print(f"O salário semanal líquido é de {salario_liquido}")

## Escreva e execute seu código aqui
salario_hora = 20
horas_semana = 40

#Salário semanal
salario_semanal = salario_hora * horas_semana

#Salário líquido
salario_liquido = salario_semanal * (1 - (0.10 + 0.05))

#Saída
#print(salario_liquido)

## Escreva e execute seu código aqui
cny      = 1
moeda_br = 50
taxa     = 0.69

#conversão
moeda_cny = moeda_br / taxa

#Saída
#print(moeda_cny)

## Escreva e execute seu código aqui

#Dados
distancia_km      = 42.195
horas_necessarias = 3

#conversão
distancia_m          = distancia_km * 1000
segundos_necessarios = horas_necessarias *  3600
v_media = distancia_m / segundos_necessarios

#Saída
print(v_media)






