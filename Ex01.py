#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, 
# contendo um relatório dos endereços IP válidos e inválidos.
corretos = 1
quant_linhas = 0
lista_ips_invalidos = []
lista_ips_validos = []
with open('Arquivos-em-python-/Ips.txt', 'r') as arquivo:
    for linha in arquivo:
        corretos = 0
        devide = linha.split('.')#divide para verificar cada número do ip
        for valor in devide:# para cada número do ip
                if int(valor) <= 255: #verifica se cada número do ip esta correto
                    corretos += 1
                    if corretos == 4:
                        lista_ips_validos.append(linha)
                        quant_linhas += 1
                        corretos = 0
                else:
                    corretos = 0
                    lista_ips_invalidos.append(linha)

with open('Arquivos-em-python-/Ips_saida.txt', 'w') as arquivo:
     arquivo.writelines('ENDEREÇOS INVÁLIDOS:\n')
     for ip in lista_ips_invalidos:
            arquivo.writelines(f'{ip}\n')
     arquivo.writelines('\n')
     arquivo.writelines('\n')
     arquivo.writelines('ENDEREÇOS VÁLIDOS:\n')
     
     for ip in lista_ips_validos:
            arquivo.writelines(f'{ip}\n')
