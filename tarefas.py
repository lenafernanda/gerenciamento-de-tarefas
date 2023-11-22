import json

def add_tarefas():
        try:
            with open ('data.json','r') as arquivos:
                tarefas = json.load(arquivos)
        except FileNotFoundError:
            tarefas = []

        while True:
            tarefa = input(f"Qual seria a tarefa?\n")
            dia = input(f"Dia:")
            mes = input(f"Mês:")
            ano = input(f"ano:")

            dados = {
                "tarefa": tarefa,
                "dia": dia,
                "mes": mes,
                "ano": ano
            }

            tarefas.append(dados)
            print(tarefas)

            continuar = input(" Deseja adicionar mais tarefas? (s/n): ")
            if continuar.lower() != "s":
                break
        with open('data.json', 'w') as arquivos:
            json.dump(tarefas,arquivos,indent=1)
            add_tarefas()


def apagar():
    try:
        with open('data.json','r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
        print(" você não tem tarefas salvas.")
        return

    tarefa_para_remover = input("digite a tarefa que deseja remover:" )
    tarefas = [tarefa for  tarefa in tarefas if tarefa.get('tarefa') != tarefa_para_remover]

    with open ('data.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=1)

    print(f"tarefa com nome {tarefa_para_remover} removida do json.")


def feito():
    try:
        with open('data.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
        print("você não tem tarefas salvas.")
        return

    try:
        with open('feito.json','r') as arquivo:
            concluido = json.load(arquivo)
    except FileNotFoundError:
        concluido = []

    while True:
        feito = input( (f'Qual tarefa você concluiu?')

        tarefa_encontrada = None
    for tarefa in tarefas:
            if tarefa.get('tarefa') == feito:
                tarefa_encontrada = tarefa
                break
    if tarefa_encontrada:
                concluido.append(tarefa_encontrada)
                tarefas.remove(tareda_encontrada)
            else:
            print("Não existe essa tarefa.")
            print("tarefas concluidas:")
            for item in concluido:
            print(item['tarefa'])