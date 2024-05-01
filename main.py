import json

def mostrar_menu_principal():
    # Menu principal
    print("Bem-vindo ao menu principal!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    return int(input("Digite uma opção válida: "))

def mostrar_menu_operacoes(menu_principal):
    # Mostrando o menu secundário
    print(f"Menu de operações - Opção: {menu_principal}")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior.")
    return int(input("Digite uma opção válida: "))

def cadastrar(lista, dados, nome_arquivo):
    lista.append(dados)
    salvar_dados(lista, f"lista_{nome_arquivo}.json")

def atualizar(lista, campo_chave, nome_arquivo):
    codigo_para_editar = int(input(f"Qual código que deseja editar? ({campo_chave}): "))
    item_editado = None

    for item in lista:
        if item[campo_chave] == codigo_para_editar:
            item_editado = item
            break

    if item_editado is None:
        print(f"Não encontrei o item de código {codigo_para_editar} na lista")
    else:
        for chave in item_editado.keys():
            novo_valor = input(f"Digite o novo valor para {chave}: ")
            item_editado[chave] = novo_valor
        salvar_dados(lista, f"lista_{nome_arquivo}.json")

def excluir(lista, campo_chave, nome_arquivo):
    codigo_excluir = int(input(f"Qual é o código do item que deseja excluir ({campo_chave}): "))
    item_removido = None

    for item in lista:
        if item[campo_chave] == codigo_excluir:
            item_removido = item
            break
    if item_removido is None:
        print(f"Não encontrei o item de código {codigo_excluir} na lista")
    else:
        lista.remove(item_removido)
        salvar_dados(lista, f"lista_{nome_arquivo}.json")

def salvar_dados(lista, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False)
    except PermissionError:
        print(f"Erro ao salvar dados no arquivo {nome_arquivo}: permissão negada.")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo {nome_arquivo}: {e}")

def ler_arquivo(nome_arquivo):
    lista = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {nome_arquivo} como JSON.")

    return lista

def cadastrar_estudante(lista_estudantes):
    codigo = int(input("Por favor, digite o código: "))
    nome_estudante = input("Digite o nome do estudante que deseja incluir: ")
    cpf = input("Por favor, digite o CPF: ")

    dados_estudantes = {
        "cod_estudante": codigo,
        "nome_estudante": nome_estudante,
        "cpf": cpf
    }
    return dados_estudantes

def cadastrar_professor(lista_professores):
    codigo = int(input("Por favor, digite o código: "))
    nome_professor = input("Digite o nome do professor que deseja incluir: ")
    cpf = input("Por favor, digite o CPF: ")

    dados_professor = {
        "cod_professor": codigo,
        "nome_professor": nome_professor,
        "cpf": cpf
    }
    return dados_professor

def cadastrar_disciplina(lista_disciplinas):
    codigo = int(input("Por favor, digite o código: "))
    nome_disciplina = input("Digite o nome da disciplina que deseja incluir: ")

    dados_disciplina = {
        "cod_disciplina": codigo,
        "nome_disciplina": nome_disciplina
    }
    return dados_disciplina

def cadastrar_turma(lista_turmas, lista_professores, lista_disciplinas):
    codigo = int(input("Por favor, digite o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))
    codigo_disciplina = int(input("Digite o código da disciplina: "))

    # Verificando se os códigos do professor e da disciplina existem
    if not any(professor["cod_professor"] == codigo_professor for professor in lista_professores):
        print("Código do professor não encontrado.")
        return None
    if not any(disciplina["cod_disciplina"] == codigo_disciplina for disciplina in lista_disciplinas):
        print("Código da disciplina não encontrado.")
        return None

    dados_turma = {
        "cod_turma": codigo,
        "cod_professor": codigo_professor,
        "cod_disciplina": codigo_disciplina
    }
    return dados_turma

def cadastrar_matricula(lista_matriculas, lista_turmas):
    codigo_turma = int(input("Por favor, digite o código da turma: "))
    codigo_estudante = int(input("Por favor, digite o código do estudante: "))

    # Verificando se o código da turma existe
    if not any(turma["cod_turma"] == codigo_turma for turma in lista_turmas):
        print("Código da turma não encontrado.")
        return None

    dados_matricula = {
        "cod_turma": codigo_turma,
        "cod_estudante": codigo_estudante
    }
    return dados_matricula

# Nome dos arquivos
nome_arquivo_estudantes = "estudantes"
nome_arquivo_professores = "professores"
nome_arquivo_disciplinas = "disciplinas"
nome_arquivo_turmas = "turmas"
nome_arquivo_matriculas = "matriculas"

while True:
    menu_principal = mostrar_menu_principal()

    if menu_principal == 1:
        print("Você escolheu a opção de Estudantes")

        while True:
            opcao_secundaria = mostrar_menu_operacoes(menu_principal)

            if opcao_secundaria == 1:
                lista_estudantes = ler_arquivo(f"lista_{nome_arquivo_estudantes}.json")
                cadastrar(lista_estudantes, cadastrar_estudante(lista_estudantes), nome_arquivo_estudantes)
            elif opcao_secundaria == 2:
                lista_estudantes = ler_arquivo(f"lista_{nome_arquivo_estudantes}.json")
                if len(lista_estudantes) == 0:
                    print("Não há estudantes cadastrados")
                else:
                    for estudante in lista_estudantes:
                        print(estudante)
            elif opcao_secundaria == 3:
                lista_estudantes = ler_arquivo(f"lista_{nome_arquivo_estudantes}.json")
                atualizar(lista_estudantes, "cod_estudante", nome_arquivo_estudantes)
            elif opcao_secundaria == 4:
                lista_estudantes = ler_arquivo(f"lista_{nome_arquivo_estudantes}.json")
                excluir(lista_estudantes, "cod_estudante", nome_arquivo_estudantes)
            elif opcao_secundaria == 5:
                break
            else:
                print("Opção inválida")

    elif menu_principal == 2:
        print("Você escolheu a opção de Professores")

        while True:
            opcao_secundaria = mostrar_menu_operacoes(menu_principal)

            if opcao_secundaria == 1:
                lista_professores = ler_arquivo(f"lista_{nome_arquivo_professores}.json")
                cadastrar(lista_professores, cadastrar_professor(lista_professores), nome_arquivo_professores)
            elif opcao_secundaria == 2:
                lista_professores = ler_arquivo(f"lista_{nome_arquivo_professores}.json")
                if len(lista_professores) == 0:
                    print("Não há professores cadastrados")
                else:
                    for professor in lista_professores:
                        print(professor)
            elif opcao_secundaria == 3:
                lista_professores = ler_arquivo(f"lista_{nome_arquivo_professores}.json")
                atualizar(lista_professores, "cod_professor", nome_arquivo_professores)
            elif opcao_secundaria == 4:
                lista_professores = ler_arquivo(f"lista_{nome_arquivo_professores}.json")
                excluir(lista_professores, "cod_professor", nome_arquivo_professores)
            elif opcao_secundaria == 5:
                break
            else:
                print("Opção inválida")

    elif menu_principal == 3:
        print("Você escolheu a opção de Disciplinas")

        while True:
            opcao_secundaria = mostrar_menu_operacoes(menu_principal)

            if opcao_secundaria == 1:
                lista_disciplinas = ler_arquivo(f"lista_{nome_arquivo_disciplinas}.json")
                cadastrar(lista_disciplinas, cadastrar_disciplina(lista_disciplinas), nome_arquivo_disciplinas)
            elif opcao_secundaria == 2:
                lista_disciplinas = ler_arquivo(f"lista_{nome_arquivo_disciplinas}.json")
                if len(lista_disciplinas) == 0:
                    print("Não há disciplinas cadastradas")
                else:
                    for disciplina in lista_disciplinas:
                        print(disciplina)
            elif opcao_secundaria == 3:
                lista_disciplinas = ler_arquivo(f"lista_{nome_arquivo_disciplinas}.json")
                atualizar(lista_disciplinas, "cod_disciplina", nome_arquivo_disciplinas)
            elif opcao_secundaria == 4:
                lista_disciplinas = ler_arquivo(f"lista_{nome_arquivo_disciplinas}.json")
                excluir(lista_disciplinas, "cod_disciplina", nome_arquivo_disciplinas)
            elif opcao_secundaria == 5:
                break
            else:
                print("Opção inválida")

    elif menu_principal == 4:
        print("Você escolheu a opção de Turmas")

        while True:
            opcao_secundaria = mostrar_menu_operacoes(menu_principal)

            if opcao_secundaria == 1:
                lista_turmas = ler_arquivo(f"lista_{nome_arquivo_turmas}.json")
                turma_cadastrada = cadastrar_turma(lista_turmas, lista_professores, lista_disciplinas)
                if turma_cadastrada is not None:
                    cadastrar(lista_turmas, turma_cadastrada, nome_arquivo_turmas)
            elif opcao_secundaria == 2:
                lista_turmas = ler_arquivo(f"lista_{nome_arquivo_turmas}.json")
                if len(lista_turmas) == 0:
                    print("Não há turmas cadastradas")
                else:
                    for turma in lista_turmas:
                        print(turma)
            elif opcao_secundaria == 3:
                lista_turmas = ler_arquivo(f"lista_{nome_arquivo_turmas}.json")
                atualizar(lista_turmas, "cod_turma", nome_arquivo_turmas)
            elif opcao_secundaria == 4:
                lista_turmas = ler_arquivo(f"lista_{nome_arquivo_turmas}.json")
                excluir(lista_turmas, "cod_turma", nome_arquivo_turmas)
            elif opcao_secundaria == 5:
                break
            else:
                print("Opção inválida")

    elif menu_principal == 5:
        print("Você escolheu a opção de Matrículas")

        while True:
            opcao_secundaria = mostrar_menu_operacoes(menu_principal)

            if opcao_secundaria == 1:
                lista_matriculas = ler_arquivo(f"lista_{nome_arquivo_matriculas}.json")
                matricula_cadastrada = cadastrar_matricula(lista_matriculas, lista_turmas)
                if matricula_cadastrada is not None:
                    cadastrar(lista_matriculas, matricula_cadastrada, nome_arquivo_matriculas)
            elif opcao_secundaria == 2:
                lista_matriculas = ler_arquivo(f"lista_{nome_arquivo_matriculas}.json")
                if len(lista_matriculas) == 0:
                    print("Não há matrículas cadastradas")
                else:
                    for matricula in lista_matriculas:
                        print(matricula)
            elif opcao_secundaria == 3:
                lista_matriculas = ler_arquivo(f"lista_{nome_arquivo_matriculas}.json")
                atualizar(lista_matriculas, "cod_turma", nome_arquivo_matriculas)
            elif opcao_secundaria == 4:
                lista_matriculas = ler_arquivo(f"lista_{nome_arquivo_matriculas}.json")
                excluir(lista_matriculas, "cod_turma", nome_arquivo_matriculas)
            elif opcao_secundaria == 5:
                break
            else:
                print("Opção inválida")

    elif menu_principal == 0:
        print("Você pediu para sair")
        break
    else:
        print("Opção inválida")
