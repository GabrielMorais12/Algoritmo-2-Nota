lista_pacientes = [["Rubens", "4444", "111", "000", "Nenhuma"]]
lista_administradores = [["adimininastro", "555"]]
lista_dentistas = [["1", "Dr.Yugi", "KUUGA123", "Ortodontia"], ["2", "Dra. Jeanne", "AGITO234", "Endodontia"]]
lista_consultorios = [["Sala 1", "Dr.Yugi"], ["Sala 2", "Dra.Jeanne"]]
lista_consultas = []

while True:
    print("\n    -------Clinica-------")
    print(" 1 - Módulo Paciente")
    print(" 2 - Módulo Administração / Secretaria")
    print(" 0 - Encerrar Sistema")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("\n----------ACESSO AO PACIENTE----------")
        cpf_login = input("Digite o seu CPF: ")

        paciente_encontrado = False
        indice_paciente = 0

        while indice_paciente < len(lista_pacientes):
            if cpf_login == lista_pacientes[indice_paciente][1]:
                paciente_encontrado = True
                break
            indice_paciente += 1

        if paciente_encontrado:
            senha_login = input("Digite sua senha: ")
            if senha_login == lista_pacientes[indice_paciente][2]:
                print(f"\nLogin efetuado com sucesso! Bem-vindo(a), {lista_pacientes[indice_paciente][0]}")

                while True:
                    print("\n----------Menu do Paciente----------")
                    print("1 - Ver Corpo Clínico")
                    print("2 - Agendar Consulta")
                    print("3 - Minhas Consultas")
                    print("4 - Cancelar Consulta")
                    print("0 - Sair da Conta")

                    op_pac = int(input("Escolha uma opção: "))

                    if op_pac == 1:
                        print("\n-------Profissionais em Expediente-------")
                        i = 0
                        while i < len(lista_dentistas):
                            print(f"ID: {lista_dentistas[i][0]} | Nome: {lista_dentistas[i][1]} | CRO: {lista_dentistas[i][2]} | Especialidade: {lista_dentistas[i][3]}")
                            i += 1

                    elif op_pac == 2:
                        print("\n----------Agendar Consulta----------")
                        i = 0
                        while i < len(lista_dentistas):
                            print(f"- {lista_dentistas[i][1]} ({lista_dentistas[i][3]})")
                            i += 1

                        nome_dentista = input("Digite o nome do dentista desejado: ")
                        data = input("Digite a data desejada (DD/MM/AAAA): ")
                        horario = input("Digite o horário desejado (HH:MM): ")

                        conflito = False
                        i = 0
                        while i < len(lista_consultas):
                            if lista_consultas[i][1] == nome_dentista and lista_consultas[i][2] == data and lista_consultas[i][3] == horario:
                                conflito = True
                                break
                            i += 1

                        if conflito:
                            print("Erro: O dentista já possui consulta marcada neste horário!")
                        else:
                            lista_consultas.append([lista_pacientes[indice_paciente][1], nome_dentista, data, horario])
                            print("Consulta agendada com sucesso!")

                    elif op_pac == 3:
                        print("\n----------Minhas Proximas Consultas----------")
                        encontrou = False
                        i = 0
                        while i < len(lista_consultas):
                            if lista_consultas[i][0] == lista_pacientes[indice_paciente][1]:
                                print(f"Dentista: {lista_consultas[i][1]} | Data: {lista_consultas[i][2]} | Horário: {lista_consultas[i][3]}")
                                encontrou = True
                            i += 1
                        if not encontrou:
                            print("Nenhuma consulta encontrada para o seu CPF.")

                    elif op_pac == 4:
                        print("\n--- Cancelar Consulta ---")
                        data_canc = input("Digite a data da consulta a cancelar (DD/MM/AAAA): ")
                        hor_canc = input("Digite o horário da consulta (HH:MM): ")

                        removido = False
                        i = 0
                        while i < len(lista_consultas):
                            if lista_consultas[i][0] == lista_pacientes[indice_paciente][1] and lista_consultas[i][2] == data_canc and lista_consultas[i][3] == hor_canc:
                                lista_consultas.pop(i)
                                print("Consulta cancelada com sucesso!")
                                removido = True
                                break
                            i += 1
                        if not removido:
                            print("Consulta não encontrada")

                    elif op_pac == 0:
                        print("Voltando...")
                        break
                    else:
                        print("Opção Não existe.")
            else:
                print("Senha esta errada.")
        else:
            print("\nCPF não registrado")
            resp = int(input("Deseja realizar seu registro? (1 - Sim, 2 - Não): "))
            if resp == 1:
                nome = input("Digite seu nome completo: ")
                senha = input("sua senha: ")
                telefone = input("seu telefone: ")
                observacoes = "Nenhuma"
                lista_pacientes.append([nome, cpf_login, senha, telefone, observacoes])
                print("cadastro realizado! Faça o login.")

    elif opcao == 2:
        print("\n----------Acesso a Secretaria----------")
        login_adm = input("Digite o usuário ADM: ")
        senha_adm = input("Digite a senha ADM: ")

        adm_logado = False
        i = 0
        while i < len(lista_administradores):
            if login_adm == lista_administradores[i][0] and senha_adm == lista_administradores[i][1]:
                adm_logado = True
                break
            i += 1

        if adm_logado:
            print(f"\nLogin feito! Bem-vindo(a), {login_adm}")

            while True:
                print("\n----------Menu Da Administração----------")
                print("1 - Gestão de Dentistas (CRUD)")
                print("2 - Gestão de Consultórios")
                print("3 - Gestão de Pacientes (CRUD Completo)")
                print("4 - Gestão da Agenda Geral")
                print("0 - Sair da Conta")

                op_adm = int(input("Escolha uma opção: "))

                if op_adm == 1:
                    while True:
                        print("\n----------Gestão De Dentistas----------")
                        print("1 - Cadastrar Dentista")
                        print("2 - Listar Dentistas")
                        print("3 - Remover Dentista")
                        print("0 - Voltar")
                        op_dent = int(input("Escolha: "))

                        if op_dent == 1:
                            did = input("ID do dentista: ")
                            dnome = input("Nome: ")
                            dcro = input("CRO: ")
                            desp = input("Especialidade: ")
                            lista_dentistas.append([did, dnome, dcro, desp])
                            print("Dentista cadastrado com sucesso!")
                        elif op_dent == 2:
                            i = 0
                            while i < len(lista_dentistas):
                                print(f"ID: {lista_dentistas[i][0]} | Nome: {lista_dentistas[i][1]} | CRO: {lista_dentistas[i][2]} | Esp: {lista_dentistas[i][3]}")
                                i += 1
                        elif op_dent == 3:
                            did = input("Digite o ID do dentista a remover: ")
                            i = 0
                            removido = False
                            while i < len(lista_dentistas):
                                if lista_dentistas[i][0] == did:
                                    lista_dentistas.pop(i)
                                    print("Removido com sucesso!")
                                    removido = True
                                    break
                                i += 1
                            if not removido:
                                print("Dentista não encontrado.")
                        elif op_dent == 0:
                            break

                elif op_adm == 2:
                    while True:
                        print("\n----------Gestão De Consultorios----------")
                        print("1 - Cadastrar/Vincular Sala")
                        print("2 - Listar Consultórios")
                        print("0 - Voltar")
                        op_cons = int(input("Escolha: "))

                        if op_cons == 1:
                            sala = input("Nome/Número da Sala: ")
                            dentista_vinc = input("Nome do Dentista responsável: ")
                            lista_consultorios.append([sala, dentista_vinc])
                            print("Consultório vinculado!")
                        elif op_cons == 2:
                            i = 0
                            while i < len(lista_consultorios):
                                print(f"Sala: {lista_consultorios[i][0]} | Dentista: {lista_consultorios[i][1]}")
                                i += 1
                        elif op_cons == 0:
                            break

                elif op_adm == 3:
                    while True:
                        print("\n----------Gestão De Pacientes----------")
                        print("1 - Listar Pacientes")
                        print("2 - Buscar por Nome ou CPF")
                        print("3 - Atualizar Dados e Inserir Observações sobre o paciente")
                        print("0 - Voltar")
                        op_gpac = int(input("Escolha: "))

                        if op_gpac == 1:
                            i = 0
                            while i < len(lista_pacientes):
                                print(f"Nome: {lista_pacientes[i][0]} | CPF: {lista_pacientes[i][1]} | Tel: {lista_pacientes[i][3]} | Obs: {lista_pacientes[i][4]}")
                                i += 1
                        elif op_gpac == 2:
                            busca = input("Digite o Nome ou CPF: ")
                            i = 0
                            encontrou = False
                            while i < len(lista_pacientes):
                                if busca in lista_pacientes[i][0] or busca in lista_pacientes[i][1]:
                                    print(f"Encontrado -> Nome: {lista_pacientes[i][0]} | CPF: {lista_pacientes[i][1]} | Tel: {lista_pacientes[i][3]} | Obs: {lista_pacientes[i][4]}")
                                    encontrou = True
                                i += 1
                            if not encontrou:
                                print("Nenhum paciente encontrado.")
                        elif op_gpac == 3:
                            cpf_busca = input("Digite o CPF do paciente para atualizar: ")
                            i = 0
                            atualizado = False
                            while i < len(lista_pacientes):
                                if lista_pacientes[i][1] == cpf_busca:
                                    lista_pacientes[i][0] = input("Novo nome: ")
                                    lista_pacientes[i][3] = input("Novo telefone: ")
                                    lista_pacientes[i][4] = input("Adicionar observações/alergias: ")
                                    print("Dados atualizados com sucesso!")
                                    atualizado = True
                                    break
                                i += 1
                            if not atualizado:
                                print("Paciente não encontrado.")
                        elif op_gpac == 0:
                            break

                elif op_adm == 4:
                    while True:
                        print("\n----------GESTÃO DA AGENDA GERAL----------")
                        print("1 - Ver Agenda Completa")
                        print("2 - Cancelar Consulta de Paciente")
                        print("0 - Voltar")
                        op_ag = int(input("Escolha: "))

                        if op_ag == 1:
                            if len(lista_consultas) == 0:
                                print("Não há consultas agendadas.")
                            else:
                                i = 0
                                while i < len(lista_consultas):
                                    print(f"Paciente CPF: {lista_consultas[i][0]} | Dentista: {lista_consultas[i][1]} | Data: {lista_consultas[i][2]} | Horário: {lista_consultas[i][3]}")
                                    i += 1
                        elif op_ag == 2:
                            cpfc = input("CPF do paciente da consulta: ")
                            datac = input("Data (DD/MM/AAAA): ")
                            horc = input("Horário (HH:MM): ")
                            remv = False
                            i = 0
                            while i < len(lista_consultas):
                                if lista_consultas[i][0] == cpfc and lista_consultas[i][2] == datac and lista_consultas[i][3] == horc:
                                    lista_consultas.pop(i)
                                    print("Consulta cancelada pela administração com sucesso!")
                                    remv = True
                                    break
                                i += 1
                            if not remv:
                                print("Consulta não encontrada.")
                        elif op_ag == 0:
                            break

                elif op_adm == 0:
                    print("Saindo do ambiente administrativo...")
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Login ou senha de administrador incorretos...")

    elif opcao == 0:
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
