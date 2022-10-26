ddd = dict ({
    61 : "Brasília",
    71 : "Salvador",
    11 : "São Paulo",
    21 : "Rio de Janeiro",
    32 : "Juiz de Fora",
    19 : "Campinas",
    27 : "VItória",
    31 : "Belo Horizonte",
})

cod = 1

print("="*10)
print("Busca DDD")
print("="*10)

while cod != 0:
    try:
        print("="*25)
        cod = int(input("Digite o ddd para descobrir a cidade ou 0 para sair do aplicativo: "))
        print(f'{cod} pertence a {ddd[cod]}')
        print("="*10)
    except:
        if cod == 0:
            print("="*10)
            print("Bye!")
            print("="*10)
        else:
            print("="*10)
            print("DDD não cadastrado!")
            print("="*10)

# Bruno Marques, José Marcos, Kelvin Gomes, Lucas Mendes, Vinícius de Assis