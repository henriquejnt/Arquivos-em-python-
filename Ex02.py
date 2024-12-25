import math

quant_linhas = 1
lista_bytes = []
resultado_bytes = []
pega_nomes = []
percentuais = []
nr = [1,2,3,4,5,6]

with open('Arquivos-em-python-/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        # Pega os valores
        if quant_linhas % 2 == 0:
            lista_bytes.append(linha.strip())  # Remove novos caracteres de linha
        else:
            pega_nomes.append(linha.strip())  # Remove novos caracteres de linha
        quant_linhas += 1

# Pega valores e transforma em bytes
for valor in lista_bytes:
    num = float(valor)
    converte = num / 1048.576  # Certifique-se da fórmula correta
    resultado_bytes.append(math.ceil(converte))

#pega a soma e a porcentagem dos valores
soma = sum(resultado_bytes)
for valor in resultado_bytes:
    porcentagem = (valor/soma)*100
    percentuais.append(porcentagem)
# Imprime os itens lado a lado
with open('Arquivos-em-python-/usuarios_saida.txt', 'w') as arquivo:
    arquivo.writelines('Uso do espaço em disco pelos usuários\n')
    
    arquivo.writelines('Nr.  Usuário        Espaço utilizado     % do uso\n')
    for item1, item2, item3, item4 in zip(pega_nomes, resultado_bytes,percentuais,nr):
        arquivo.writelines(f'{item4}        {item1}        {item2}MB        {item3}%\n')
    
    arquivo.writelines(f'Espaço total ocupado: {math.ceil(soma)}MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {math.ceil(soma/6)}MB\n')