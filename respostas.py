#A sequência de Fibonacci é um padrão numérico em que o primeiro e o segundo termo são iguais a 1 e cada termo a partir do terceiro é a soma dos dois termos anteriores.

def fibonacci(valor):
    if valor <= 0:
        return "O valor deve ser maior que 0."
    
    if valor == 1:
        return 0

    if valor in [2,3]:
        return 1
    else:
        primeiro_termo = 0
        segundo_termo = 1
        for i in range(2,valor):
            #print(f"i = {i}")
            #print(f"primeiro_termo = {primeiro_termo},  segundo_termo = {segundo_termo}")
            proximo_termo = primeiro_termo + segundo_termo
            primeiro_termo = segundo_termo
            segundo_termo = proximo_termo
            #print(f"proximo_termo = {proximo_termo}")   
        return proximo_termo

print(fibonacci(1))  # Deve retornar 0
print(fibonacci(2))  # Deve retornar 1
print(fibonacci(3))  # Deve retornar 1
print(fibonacci(4))  # Deve retornar 2
print(fibonacci(5))  # Deve retornar 3
print(fibonacci(6))  # Deve retornar 5
print(fibonacci(7))  # Deve retornar 8
print(fibonacci(8))  # Deve retornar 13
print(fibonacci(9))  # Deve retornar 21
print(fibonacci(10)) # Deve retornar 34


# Listas vs. Tuplas
# Explique brevemente a diferença entre uma lista e uma tupla em Python e dê um exemplo
# prático de uso de cada uma.

# Listas eu posso modificar, atualizar, adicionar ou remover valores
# Tuplas não mudam, eu não posso alterar seus valores, por exemplo um tupla pode conter dias da semana ou meses do ano.  

# Exemplo de Lista
compras_mes = ['arroz', 'feijão', 'carne']
print(compras_mes)
# Adicionando um item na lista
compras_mes.append('farinha')
print(compras_mes)
# Removendo um item da lista
compras_mes.remove('arroz')
print(compras_mes)
# Atulizando um item da lista
compras_mes[1]= 'carne de gado'
print(compras_mes)

# Exemplo de Tupla
dias_da_semana = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
print(dias_da_semana)  



# SQL
# 1. Consulta Avançada
# Escreva uma consulta SQL para encontrar o número total de pedidos feitos por cada cliente em
# uma tabela chamada 'Pedidos', incluindo apenas os clientes que fizeram mais de 5 pedidos.


# SELECT cliente, COUNT(pedido_id) AS total_pedidos
# FROM Pedidos
# GROUP BY cliente
# HAVING COUNT(pedido_id) > 5;



