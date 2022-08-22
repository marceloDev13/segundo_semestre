from random import sample


# Embaralha a string passada como parametro
def shuffle_word(word):
    return ''.join(sample(word, len(word)))


# Retorna um array com a tabuada do '1' ao '10' do número passado como parametro
# Caso o número passado como parametro não seja um número retorna uma mensagem de erro
def multiplication_table(number):
    table = []

    num = int(number)
    if isinstance(num, int):
        for index in range(1, 11):
            multiply = index * num
            table.append(f'{num} X {index} = {multiply}')
        return table
    else:
        print('Entrada invalida!')


# Imprime a palavra digita embaralhada
print('\n>>>',shuffle_word(input('Digite uma palavra...\n\n')).upper(),'<<<\n\n')

try:
    print('\n'.join(map(str, multiplication_table(input('Digite um numero...\n\n')))))

except:
    print("Deu ruim!")
