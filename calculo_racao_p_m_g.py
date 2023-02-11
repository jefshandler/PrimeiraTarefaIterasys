
# Descrição da tarefa
# retornando a quantidade de ração em gramas.
# A funcionalidade não deve aceitar outras letras para
# porte ou valores menores ou iguais a zero,
# ou maiores que 100kg para o peso do animal.


def cao_p(n1, n2):
    # 10g para P 1 a 15
    if n1 > 15 or n1 < 1:
        print("\033[91mPet fora da Categoria ou peso igual a Zero\033[m")

    n2 = 10
    return int(n1 * n2)


def cao_m(n1, n2):
    # 20g para M 15 a 25
    if n1 > 25 or n1 < 15:
        print("\033[91mPet fora da Categoria ou peso igual a Zero\033[m")

    n2 = 20
    return int(n1 * n2)


def cao_g(n1, n2):
    # 30g para G 25 a 45
    if n1 > 45 or n1 < 25:
        print("\033[91mPet fora da Categoria ou peso igual a Zero\033[m")

    n2 = 30
    return int(n1 * n2)


def cao_gg(n1, n2):
    # 45 g para GG 45 a 90
    if n1 > 90 or n1 < 45:
        print("\033[91mPet fora da Categoria ou peso igual a Zero\033[m")

    n2 = 45
    return int(n1 * n2)


if __name__ == '__main__':


    ## Calculadora AN Pet ##
    pet = ''
    print('\033[91m## CALCULADORA AN DE PET ##\033[m')
    print('\033[94m1. Pet Pequeno Porte de 1 a 15 kilos\033[m')
    print('\033[93m2. Pet Medio Porte de 15 a 25 kilos\033[m')
    print('\033[92m3. Pet Grande Porte de 25 a 45 kilos\033[m')
    print('\033[95m4. Pet Gigante Porte de 45 a 90 kilos\033[m')
    print('\033[91mX. Sair\033[m')

    while True:

        pet_an_calc = input('\033[92mEscolha a categoria do pet ou X para sair: \033[m')

        match pet_an_calc:
            case '1':
                pet = 'um pet de pequeno porte '
            case '2':
                pet = 'um pet de médio porte'
            case '3':
               pet = 'um pet de grande porte'
            case '4':
                pet = 'um pet de gigante porte'
            case 'x':
                print('Fim da execução')
                break
            case _:
                print('Escolha inválida')

        if pet != '':

            n1 = int(input('\033[93mQual peso do seu pet: \033[m'))
            n2 = 0
            match pet_an_calc:
                case '1':
                    resultado = cao_p(n1, n2)
                case '2':
                    resultado = cao_m(n1,n2)
                case '3':
                    resultado = cao_g(n1, n2)
                case '4':
                    resultado = cao_gg(n1, n2)

            if n1 == 0:
                print("Peso nao pode ser Zero")
            else:
                print(f'\033[97mSeu pet pesa {n1} Kilos é {pet} ele vai consumir {resultado} gramas de ração dia\033[m')
                # limpando oper pro caso de enviarem vazio no numero da operacao

                pet = ''