import random

def sort(array):
    # É necessario um array auxiliar para "segurar" essas alterações
    array_aux = array[:]
    sort_half(array, array_aux, 0, len(array) - 1) #Parametros ->

# Quebra o array em pequenas partes para aplicar a função merge
def sort_half(array, array_aux, inicio, final):
    if inicio >= final:
        return

    # Pegando o valor do meio da função
    meio = (inicio + final) // 2

    # Dividindo do inico até a metade do array
    sort_half(array, array_aux, inicio, meio)
    # Da metade até o final
    sort_half(array, array_aux, meio + 1, final)

    merge(array, array_aux, inicio, final)

def merge(array, array_aux, inicio, final):

    # inicio do lado esquerdo
    esquerda = inicio
    # fim do lado esquerdo
    esquerdo_fin = (inicio + final) // 2

    # inicio do lado direito
    direita = esquerdo_fin + 1
    # fim do lado direito
    direita_fin = final

    posição = inicio

    # Fazendo as comparações

    for posição in range(inicio, final + 1):
        # Se não tiver mais nenhum elemento do lado esquerdo para ser processado
        if esquerda > esquerdo_fin:
            array_aux[posição] = array[direita]
            direita += 1

        # Se não tiver mais nenhum elemento do lado direito para ser processado
        elif direita > direita_fin:
            array_aux[posição] = array[esquerda]
            esquerda += 1

        # Comparando o lado esquerdo com o direito
        elif array[esquerda] < array[direita]:
            array_aux[posição] = array[esquerda]
            esquerda += 1

        else:
            array_aux[posição] = array[direita]
            direita += 1


    for k in range(inicio, final + 1):
        array[k] = array_aux[k]



# Testa o algoritmo.
# random.sample para sortear de forma aleatoria
# Função range, retorna uma serie aletaria dentro dos paramentros (-10 até 10)
array = random.sample(range(-10, 10), 10)

# Mostrando o array fora de ordem
print("O array fora de ordem: ", array)
copy = array[:]   # array auxiliar

sort(array)
# O array em ordem
print("O array em ordem: ", array)

assert array == sorted(copy)