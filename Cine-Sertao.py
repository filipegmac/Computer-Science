import os
import matplotlib.pyplot as plt
# DUPLA: Filipe Gonçalves Maciel E Jesseh Albuquerque

# Dicionário para armazenar usuários cadastrados
users = {"abc": ["abc", "123"]}

# Dicionário para armazenar admins cadastrados
admins = {"Filipe": ["Filipe", "Maciel"], "Jesseh": ["Jesseh", "Albuquerque"]}

# Dicionário para armazenar os filmes no catálogo
movies = {
   "Interestelar": {
       "Diretor": "Christopher Nolan",
       "Gênero": "Ficção Científica",
       "Sala": "1",
       "Horário": "20:00",
       "Ingressos": 5,
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
   "Forrest Gump O Contador de Histórias": {
       "Diretor": "Robert Zemeckis",
       "Gênero": "Comédia",
       "Sala": "3",
       "Horário": "20:00",
       "Ingressos": 30,
       "Preço": "15,00"
   },
}

sold_tickets = [] # Lista para armazenar os ingressos vendidos
user_preferences = {} # Dicionário para armazenar as preferências dos usuários

def save_ticket_to_file(ticket_info):
   with open(f"compra_{ticket_info['user']}_{ticket_info['movie']}.txt", "w") as file:
       file.write(f"Usuário: {ticket_info['user']}\n")
       file.write(f"Filme: {ticket_info['movie']}\n")
       file.write(f"Quantidade: {ticket_info['quantity']}\n")
       file.write(f"Preço Total: {ticket_info['total_price']}\n")

def generate_report():
   with open("relatorio_vendas.txt", "w") as file:
       for ticket in sold_tickets:
           file.write(f"Usuário: {ticket['user']}, Filme: {ticket['movie']}, Quantidade: {ticket['quantity']}, Preço Total: {ticket['total_price']}\n")

def generate_movie_report(movie_name):
    with open(f"relatorio_{movie_name}.txt", "w") as file:
        found = False
        for ticket in sold_tickets:
            if ticket['movie'] == movie_name:
                found = True
                file.write(f"Usuário: {ticket['user']}, Quantidade: {ticket['quantity']}, Preço Total: {ticket['total_price']}\n")
        if not found:
            file.write("Nenhum ingresso vendido para este filme.\n")

def recommend_movies(user):
   if user in user_preferences:
       preferred_genre = user_preferences[user]
       recommendations = [movie for movie, details in movies.items() if details["Gênero"] == preferred_genre]
       return recommendations
   return []

def plot_sales_report():
   movie_sales = {}
   for ticket in sold_tickets:
       movie = ticket['movie']
       quantity = ticket['quantity']
       if movie in movie_sales:
           movie_sales[movie] += quantity
       else:
           movie_sales[movie] = quantity

   movies = list(movie_sales.keys())
   quantities = list(movie_sales.values())

   plt.figure(figsize=(10, 5))
   plt.bar(movies, quantities, color='blue')
   plt.xlabel('Filmes')
   plt.ylabel('Ingressos Vendidos')
   plt.title('Relatório de Vendas por Filme')
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.show()

while True:
   print("""
 ██████╗██╗███╗  ██╗███████╗   ███████╗███████╗██████╗ ████████╗ █████╗ ██████╗ 
██╔════╝██║████╗ ██║██╔════╝   ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗
██║    ██║██╔██╗ ██║█████╗     ███████╗█████╗ ██████╔╝  ██║  ███████║██║  ██║
██║    ██║██║╚██╗██║██╔══╝     ╚════██║██╔══╝ ██╔══██╗  ██║  ██╔══██║██║  ██║
╚██████╗██║██║ ╚████║███████╗   ███████║███████╗██║ ██║  ██║  ██║ ██║╚██████╔╝
 ╚═════╝╚═╝╚═╝ ╚═══╝╚══════╝   ╚══════╝╚══════╝╚═╝ ╚═╝  ╚═╝  ╚═╝ ╚═╝ ╚═════╝
BEM VINDO AO CINE SERTÃO! ENTRE NA CONTA PARA COMPRAR INGRESSOS!
""")

   options = int(input("Escolha uma das opções abaixo:\n1 - Entrar na conta\n2 - Criar conta\n3 - Filmes disponíveis\n0 - Sair\n\nDigite a opção: "))

   if options == 1:
       os.system('cls')
       print("""
┏┓                        
┣ ┏┓╋┏┓┏┓┏┓ ┏┓┏┓ ┏┏┓┏┓╋┏┓
┗┛┛┗┗┛ ┗┻┛  ┛┗┗┻ ┗┗┛┛┗┗┗┻
""")
       user_login = str(input('Digite seu usuário: '))
       password_login = str(input('Digite sua senha: '))

       if user_login in users and users[user_login][1] == password_login:
           os.system('cls')
           print('Login realizado com sucesso!\n')

           while True:
               optionsUser = int(input("Escolha uma das opções abaixo:\n1 - Comprar Ingressos\n2 - Filmes disponíveis\n3 - Ver recomendações\n0 - Voltar\n\nDigite a opção: "))
               if optionsUser == 0:
                   break

               elif optionsUser == 1:
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

                       if tickets <= movies[selected_movie]["Ingressos"]:
                           movies[selected_movie]["Ingressos"] -= tickets
                           total_price = tickets * float(movies[selected_movie]["Preço"].replace(",", "."))
                           print(f"\nCompra realizada com sucesso! {tickets} ingressos para {selected_movie}.")
                           sold_tickets.append({
                               "user": user_login,
                               "movie": selected_movie,
                               "quantity": tickets,
                               "total_price": total_price
                           })
                           save_ticket_to_file({
                               "user": user_login,
                               "movie": selected_movie,
                               "quantity": tickets,
                               "total_price": total_price
                           })
                           user_preferences[user_login] = movies[selected_movie]["Gênero"]
                       else:
                           print(f"\nDesculpe, não há ingressos suficientes disponíveis para {selected_movie}.")

                       input("\nPressione Enter para voltar...")
                   os.system('cls')

               elif optionsUser == 2:
                   os.system('cls')
                   print("Filmes disponíveis:")
                   for movie, infos in movies.items():
                       print(f"\nFilme: {movie}")
                       print(f"Diretor: {infos['Diretor']}")
                       print(f"Gênero: {infos['Gênero']}")
                       print(f"Sala: {infos['Sala']}")
                       print(f"Horário: {infos['Horário']}")
                       print(f"Ingressos: {infos['Ingressos']}")
                       print(f"Preço: {infos['Preço']}")
                   input("\nPressione Enter para voltar...")
                   os.system('cls')

               elif optionsUser == 3:
                   os.system('cls')
                   recommendations = recommend_movies(user_login)
                   if recommendations:
                       print("Recomendações baseadas nas suas preferências:")
                       for movie in recommendations:
                           print(f"- {movie}")
                   else:
                       print("Nenhuma recomendação disponível.")
                   input("\nPressione Enter para voltar...")
                   os.system('cls')

               else:
                   print("Opção inválida.")

       elif user_login in admins and admins[user_login][1] == password_login:
           os.system('cls')
           print('Login realizado com sucesso!\n')

           while True:
               optionsAdmin = int(input("Escolha uma das opções abaixo:\n1 - Gerenciar Filmes\n2 - Gerenciar usuários\n3 - Criar conta admin\n4 - Relatórios\n5 - Promoções\n0 - Sair\n\nDigite a opção: "))
               os.system('cls')
               if optionsAdmin == 0:
                   break

               elif optionsAdmin == 1:
                   while True:
                       manage_movies = int(input("Escolha uma das opções abaixo:\n1 - Adicionar filme\n2 - Remover filme\n3 - Atualizar dados do filme\n0 - Voltar\n\nDigite a opção: "))
                       os.system("cls")

                       if manage_movies == 0:
                           break

                       if manage_movies == 1:
                           add_movie = str(input('Digite o nome do filme: '))
                           if add_movie in movies:
                               input('\nFilme já existe! Pressione Enter para continuar...')
                               continue
                           add_director = str(input('Digite o nome do diretor: '))
                           add_genre = str(input('Digite o nome do gênero: '))
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
                   while True:
                       manage_users = int(input("Escolha uma das opções abaixo:\n1 - Remover Usuário\n2 - Atualizar Dados de Usuário\n3 - Buscar Usuário\n0 - Sair\n\nDigite a opção: "))

                       if manage_users == 0:
                           break

                       elif manage_users == 1:
                            os.system('cls')
                            search_user = str(input('Digite o nome do usuário que deseja remover: '))
                            found_users = [user for user in users.keys() if search_user.lower() in user.lower()]
                            if found_users:
                                print("\nUsuários encontrados:")
                                for idx, user in enumerate(found_users):
                                    print(f"{idx + 1} - {user}")
                                user_choice = int(input("\nDigite o número do usuário que deseja remover: "))
                                if 1 <= user_choice <= len(found_users):
                                    selected_user = found_users[user_choice - 1]
                                    users.pop(selected_user)
                                    print(f"\nUsuário {selected_user} removido com sucesso!")
                                else:
                                    print("\nOpção inválida.")
                            else:
                                print("\nNenhum usuário encontrado com esse nome.")
                            input("\nPressione Enter para voltar...")
                            os.system('cls')

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

                       elif manage_users == 3:
                           os.system('cls')
                           search_user = str(input('Digite o nome do usuário: '))
                           found_users = [user for user in users.keys() if search_user.lower() in user.lower()]
                           if found_users:
                                print("\nUsuários encontrados:")
                                for user in found_users:
                                    print(f"- {user}")
                           else:
                                print("\nNenhum usuário encontrado com esse nome.")
                           input("\nPressione Enter para voltar...")
                           os.system('cls')

               elif optionsAdmin == 3:
                   user = str(input('Digite seu usuário: '))
                   password = str(input('Digite sua senha: '))
                   if user in users:
                       input('\nUsuário já existe! Pressione Enter para voltar...')
                   else:
                       admins[user] = [user, password]
                       input('\nCadastro realizado! Pressione Enter para voltar...\n')
                   os.system('cls')

               elif optionsAdmin == 4:
                   while True:
                       report_options = int(input("Escolha uma das opções abaixo:\n1 - Relatório de Vendas\n2 - Relatório de Vendas por Filme\n3 - Visualizar Gráfico de Vendas\n0 - Voltar\n\nDigite a opção: "))
                       if report_options == 0:
                           break
                       elif report_options == 1:
                           generate_report()
                           print("Relatório de vendas gerado com sucesso!")
                       elif report_options == 2:
                           movie_name = str(input("Digite o nome do filme: "))
                           generate_movie_report(movie_name)
                           print(f"Relatório de vendas para {movie_name} gerado com sucesso!")
                       elif report_options == 3:
                           plot_sales_report()
                       input("\nPressione Enter para voltar...")
                       os.system('cls')

               elif optionsAdmin == 5:
                   while True:
                       promo_options = int(input("Escolha uma das opções abaixo:\n1 - Criar Promoção\n2 - Gerenciar Promoções\n0 - Voltar\n\nDigite a opção: "))
                       if promo_options == 0:
                           break
                       elif promo_options == 1:
                           promo_name = str(input("Digite o nome da promoção: "))
                           promo_discount = float(input("Digite o desconto (em %): "))
                           print(f"Promoção {promo_name} com {promo_discount}% de desconto criada com sucesso!")
                       elif promo_options == 2:
                           print("Gerenciar promoções ainda não implementado.")
                       input("\nPressione Enter para voltar...")
                       os.system('cls')

               else:
                   print("Opção inválida.")

   if options == 2:
       os.system('cls')
       print("""
┏┓ •             
┃ ┏┓┓┏┓┏┓ ┏┏┓┏┓╋┏┓
┗┛┛ ┗┗┻┛  ┗┗┛┛┗┗┗┻
""")
       user = str(input('Digite seu usuário: '))
       password = str(input('Digite sua senha: '))
       if user in users:
           input('\nUsuário já existe! Pressione Enter para voltar...')
       else:
           users[user] = [user, password]
           input('\nCadastro realizado! Pressione Enter para voltar...\n')
       os.system('cls')

   if options == 3:
       os.system('cls')
       print("Filmes disponíveis:")
       for movie, infos in movies.items():
           print(f"\nFilme: {movie}")
           print(f"Diretor: {infos['Diretor']}")
           print(f"Gênero: {infos['Gênero']}")
           print(f"Sala: {infos['Sala']}")
           print(f"Horário: {infos['Horário']}")
           print(f"Ingressos: {infos['Ingressos']}")
           print(f"Preço: R${infos['Preço']}")
       input("\nPressione Enter para voltar...")
       os.system('cls')

   if options == 0:
       print("\nObrigado!\n")
       break