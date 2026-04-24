import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("✅ Tarefa adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa.")
        return
    for i, t in enumerate(tarefas):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i + 1}. {t['titulo']} [{status}]")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para concluir: ")) - 1
        tarefas[i]["concluida"] = True
        print("🎉 Tarefa concluída!")
    except:
        print("⚠️ Entrada inválida!")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para remover: ")) - 1
        tarefas.pop(i)
        print("🗑️ Tarefa removida!")
    except:
        print("⚠️ Entrada inválida!")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n📌 MENU")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar_tarefa(tarefas)
        elif op == "2":
            listar_tarefas(tarefas)
        elif op == "3":
            concluir_tarefa(tarefas)
        elif op == "4":
            remover_tarefa(tarefas)
        elif op == "0":
            salvar_tarefas(tarefas)
            print("💾 Dados salvos. Saindo...")
            break
        else:
            print("❌ Opção inválida!")

menu()
