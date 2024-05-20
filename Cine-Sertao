import os # Importa um módulo chamado "os"

# DUPLA: Filipe Gonçalves Maciel E Jesseh Albuquerque

users = {"abc": ["abc", "123"]} # Cria um dicionário para armazenar usuários e suas senhas, com um predefinido.

admins = {"Filipe": ["Filipe", "Maciel"], "Jesseh": ["Jesseh", "Albuquerque"]} # Cria um dicionário com dois administradores pré-definidos e suas senhas.

movies = {"Interestelar": { # Cria um dicionário para filmes, com alguns filmes pré-definidos.
        "Diretor": "Christopher Nolan",
        "Gênero": "Ficção Científica",
        "Sala": "1",
        "Horário": "20:00",
        "Ingressos": 0,
        "Preço": "20,00"
    },
    "Django Livre": {
        "Diretor": "Quentin Tarantino",
        "Gênero": "Faroeste",
        "Sala": "2",
        "Horário": "20:00",
        "Ingressos": 25,
        "Preço": "25,00"
    },
    "Forrest Gump: O Contador de Histórias": {
        "Diretor": "Robert Zemeckis",
        "Gênero": "Comédia",
        "Sala": "3",
        "Horário": "20:00",
        "Ingressos": 30,
        "Preço": "15,00"
    },
}


while (True): # Cria um loop infinito, garantindo que o sistema continue rodando até que o usuário decida sair.

    print("""
 ██████╗██╗███╗   ██╗███████╗    ███████╗███████╗██████╗ ████████╗ █████╗  ██████╗ 
██╔════╝██║████╗  ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗
██║     ██║██╔██╗ ██║█████╗      ███████╗█████╗  ██████╔╝   ██║   ███████║██║   ██║
██║     ██║██║╚██╗██║██╔══╝      ╚════██║██╔══╝  ██╔══██╗   ██║   ██╔══██║██║   ██║
╚██████╗██║██║ ╚████║███████╗    ███████║███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝
 ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
BEM VINDO AO CINE SERTÃO! ENTRE NA CONTA PARA COMPRAR INGRESSOS!
""")

    options = int(input("Escolha uma das opções abaixo:\n1 - Entrar na conta\n2 - Criar conta\n3 - Filmes disponíveis\n0 - Sair\n\nDigite a opção: ")) # Menu Principal

    if (options == 1): # Opção 1, entrar na conta.
        os.system('cls')
        print("""
┏┓                         
┣ ┏┓╋┏┓┏┓┏┓  ┏┓┏┓  ┏┏┓┏┓╋┏┓
┗┛┛┗┗┛ ┗┻┛   ┛┗┗┻  ┗┗┛┛┗┗┗┻
""")
        user_login = str(input('Digite seu usuário: ')) # Solicita o nome de usuário e converte para str(String).
        password_login = str(input('Digite sua senha: ')) # Solicita a senha e converte para str(String).

        if user_login in users and users[user_login][1] == password_login: # Verifica se o usuário existe no dicionário users e se a senha está correta.
            os.system('cls')
            print('Login realizado com sucesso!\n')

            while (True): # Cria um loop infinito para o menu de usuário.
                optionsUser = int(input("Escolha uma das opções abaixo:\n1 - Comprar Ingressos\n2 - Filmes disponíveis\n0 - Voltar\n\nDigite a opção: "))
                if (optionsUser == 0): # Quebra o loop e volta para o menu principal.
                    break

                elif optionsUser == 1:  # Opção de Comprar Ingressos
                    os.system('cls')
                    print("Escolha um filme para comprar ingressos:")
                    counter = 0
                    for movie in movies.keys():
                        counter += 1
                        print(f"{counter} - {movie}")
                    movie_choice = int(input("\nDigite o número do filme: "))
                    movie_list = list(movies.keys())


                    if 1 <= movie_choice <= len(movies):
                        selected_movie = movie_list[movie_choice - 1]
                        print(f"\nVocê selecionou {selected_movie}.")
                        tickets = int(input("Quantos ingressos você gostaria de comprar?: "))


                        # Verificação de disponibilidade de ingressos
                        if tickets <= movies[selected_movie]["Ingressos"]:
                            movies[selected_movie]["Ingressos"] -= tickets
                            print(f"\nCompra realizada com sucesso! {tickets} ingressos para {selected_movie}.")
                        else:
                            print(f"\nDesculpe, não há ingressos suficientes disponíveis para {selected_movie}.")

                        input("\nPressione Enter para voltar...")
                    os.system('cls')


                elif optionsUser == 2: # Ver os filmes disponiveis
                    os.system('cls')
                    print("Filmes disponíveis:")
                    for movie, infos in movies.items():
                        print(f"\nFilme: {movie}")
                        print(f"Diretor: {infos['Diretor']}")
                        print(f"Gênero: {infos['Gênero']}")
                        print(f"Sala: {infos['Sala']}")
                        print(f"Horário: {infos["Horário"]}")
                        print(f"Ingressos: {infos["Ingressos"]}")
                        print(f"Preço: {infos['Preço']}")
                    input("\nPressione Enter para voltar...")
                    os.system('cls')

                else:
                    print("Filme não encontrado.")



        elif user_login in admins and admins[user_login][1] == password_login: # Verifica se o usuário existe no dicionário admins e se a senha está correta.
            os.system('cls')
            print('Login realizado com sucesso!\n')

            while (True):
                optionsAdmin = int(input("Escolha uma das opções abaixo:\n1 - Gerenciar Filmes\n2 - Gerenciar usuários\n3 - Criar conta admin\n0 - Sair\n\nDigite a opção: "))
                os.system('cls')
                if (optionsAdmin == 0):
                    break

                elif optionsAdmin == 1:
                    while (True):
                        manage_movies = int(input("Escolha uma das opções abaixo:\n1 - Adicionar filme\n2 - Remover filme\n3 - Atualizar dados do filme\n0 - Voltar\n\nDigite a opção: "))
                        os.system("cls")

                        if (manage_movies == 0): #
                            break

                        if manage_movies == 1:
                            add_movie = str(input('Digite o nome do filme: ')) 
                            if add_movie in movies:
                                input('\nFilme já existe! Pressione Enter para continuar...')
                                continue
                            add_director = str(input('Digite o nome do diretor: ')) 
                            add_genre =  str(input('Digite o nome do gênero: '))
                            add_room = str(input('Digite o número da sala: '))
                            add_price = str(input('Digite o preço do filme: '))
                            add_ticket = str(input('Digite quantos ingressos tem: '))
                            add_time = str(input('Digite o horário do filme: '))
                            if add_movie in movies:
                                input('\nFilme já existe! Pressione Enter para voltar...')
                                continue
                            else:
                                movies[add_movie] = {
                                    "Diretor": add_director,
                                    "Gênero": add_genre,
                                    "Sala": add_room,
                                    "Horário": add_time,
                                    "Ingressos": add_ticket,
                                    "Preço": add_price
                                }  
                                input('\nFilme adicionado! Pressione Enter para voltar...\n')

                        elif manage_movies == 2:
                            search_movie = str(input('Digite o nome do filme: '))
                            if search_movie in movies.keys():
                                movies.pop(search_movie)
                                os.system('cls')
                                print("Filme removido!\n")
                            elif search_movie not in movies.keys():
                                input('Filme não está no catálogo ou não está escrito corretamente!\nPressione Enter para voltar...\n')


                        elif manage_movies == 3:
                            movie_to_update = str(input('Digite o nome do filme que deseja atualizar: '))
                            if movie_to_update in movies:
                                print("\nQual informação você gostaria de atualizar?")
                                print("1 - Diretor")
                                print("2 - Gênero")
                                print("3 - Sala")
                                print("4 - Horário")
                                print("5 - Ingressos")
                                print("6 - Preço")
                                update_option = int(input("\nDigite a opção: "))

                                if update_option == 1:
                                    new_director = str(input("Digite o novo diretor: "))
                                    movies[movie_to_update]["Diretor"] = new_director
                                elif update_option == 2:
                                    new_genre = str(input("Digite o novo gênero: "))
                                    movies[movie_to_update]["Gênero"] = new_genre
                                elif update_option == 3:
                                    new_room = str(input("Digite a nova sala: "))
                                    movies[movie_to_update]["Sala"] = new_room
                                elif update_option == 4:
                                    new_time = str(input("Digite o novo horário: "))
                                    movies[movie_to_update]["Horário"] = new_time
                                elif update_option == 5:
                                    new_tickets = int(input("Digite a nova quantidade de ingressos: "))
                                    movies[movie_to_update]["Ingressos"] = new_tickets
                                elif update_option == 6:
                                    new_price = str(input("Digite o novo preço: "))
                                    movies[movie_to_update]["Preço"] = new_price
                                else:
                                    print("Opção inválida.")

                                print("\nInformações atualizadas com sucesso!")
                            else:
                                print("\nFilme não encontrado.")
                            input("\nPressione Enter para voltar...")
                            os.system('cls')


                elif optionsAdmin == 2:
                    while(True):
                        manage_users = int(input("Escolha uma das opções abaixo:\n1 - Remover Usuário\n2 - Atualizar Dados de Usuário\n3 - Buscar Usuário\n0 - Sair\n\nDigite a opção: "))

                        if manage_users == 0:
                            break


                        elif manage_users == 1:
                            search_user = str(input('Digite o nome do usuário: '))
                            if search_user in users.keys():
                                users.pop(search_user)
                                os.system('cls')
                                print("\nUsuário Removido!\n")
                            elif search_user not in users.keys():
                                input('Usuário não existe ou não foi escrito corretamente!\nPressione Enter para voltar...\n')

                        elif manage_users == 2:
                            user_to_update = str(input('Digite o nome do usuário que deseja atualizar: '))
                            if user_to_update in users:
                                print("\nQual informação você gostaria de atualizar?")
                                print("1 - Nome de Usuário")
                                print("2 - Senha")
                                update_option = int(input("\nDigite a opção: "))

                                if update_option == 1:
                                    new_username = str(input("Digite o novo nome de usuário: "))
                                    if new_username in users:
                                        print("\nEste nome de usuário já existe. Tente outro.")
                                    else:
                                        users[new_username] = users.pop(user_to_update)
                                        print("\nNome de usuário atualizado com sucesso!")
                                elif update_option == 2:
                                    new_password = str(input("Digite a nova senha: "))
                                    users[user_to_update][1] = new_password
                                    print("\nSenha atualizada com sucesso!")
                                else:
                                    print("Opção inválida.")
                            else:
                                print("\nUsuário não encontrado.")
                            input("\nPressione Enter para voltar...")
                            os.system('cls')


                        elif (manage_users == 3):
                            os.system('cls')
                            counter = 0
                            for searching in users.keys():
                                counter += 1
                                print(f"{counter}. {searching}")
                            input("\nPressione Enter para voltar...")
                            os.system('cls')


                elif optionsAdmin == 3: 
                    user = str(input('Digite seu usuário: ')) # Solicita o nome de usuário e converte para str(String).
                    password = str(input('Digite sua senha: ')) # Solicita a senha e converte para str(String).
                    if user in users:
                        input('\nUsuário já existe! Pressione Enter para voltar...')
                    else:
                        admins[user] = [user, password] # Armazena user como chave, e como valor, armazena user e password em lista.
                        input('\nCadastro realizado! Pressione Enter para voltar...\n')
                    os.system('cls')

                else:
                    print('\nUsuário ou senha incorretos!\n')



    if (options == 2): # Opção 2, criar conta.
        os.system('cls')

        print("""
┏┓  •              
┃ ┏┓┓┏┓┏┓  ┏┏┓┏┓╋┏┓
┗┛┛ ┗┗┻┛   ┗┗┛┛┗┗┗┻
""")
        user = str(input('Digite seu usuário: ')) # Solicita o nome de usuário e converte para str(String).
        password = str(input('Digite sua senha: ')) # Solicita a senha e converte para str(String).
        if user in users:
            input('\nUsuário já existe! Pressione Enter para voltar...')
        else:
            users[user] = [user, password] # Armazena user como chave, e como valor, armazena user e password em lista.
            input('\nCadastro realizado! Pressione Enter para voltar...\n')
        os.system('cls')

    if (options == 3):
        os.system('cls')
        print("Filmes disponíveis:")
        for movie, infos in movies.items():
            print(f"\nFilme: {movie}")
            print(f"Diretor: {infos['Diretor']}")
            print(f"Gênero: {infos['Gênero']}")
            print(f"Sala: {infos['Sala']}")
            print(f"Horário: {infos["Horário"]}")
            print(f"Ingressos: {infos["Ingressos"]}")
            print(f"Preço: R${infos['Preço']}")
        input("\nPressione Enter para voltar...")
        os.system('cls')

    if (options == 0):
        print("\nObrigado!\n")
        break
