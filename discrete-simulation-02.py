# Funcionamento do yield
l = [1,2,3,4,5]

for i in l:
    print(i)
#Lembrando que estamos usando o operador de compressão []
l2 = [i ** 2 for i in range(5)]
for i in l2:
    print(i)

#Com o gerator não é alocado espaço espaço na memória, apenas quando for chamado para cada iteração em tempo de execução, consegue trabalhar com listas infinitas ()

#Perda de tempo de processamento, não guarda o valor na mémoria, gera e depois elimina, só é gerado uma vez.
g = (i** 2 for i in range(5))
for i in g:
    print(i)

#Yield funciona como return, mas não destroi a função, ele salvo o estado da função 
print('# Funcionamento do yield:')    
def lista_elementos():
    i = 0
    yield(i)
    i = 1
    yield(i)
    i = 2
    yield(3)

y = lista_elementos()

#Retorna valor de interable
print(next(y))

print(next(y))
