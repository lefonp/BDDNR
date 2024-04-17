from pymongo import MongoClient
from time import sleep

class ontato:
    def __init__(self, nome, sobrenome, numero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero = numero

class GerenciadorContatos:
    def __init__(self):
        try:
            self.cliente = MongoClient('localhost', 27017)
            self.db = self.cliente['Agenda']
            self.collection = self.db['Contato']
            print("Conectado ao banco de dados.")
        except Exception as e:
            print(f"ERRO: {e}")

    def adicionar_contato(self, nome, sobrenome, numero):
        try:
            contato = {"nome": nome, "sobrenome": sobrenome, "numero": numero}
            self.collection.insert_one(contato)
            print("Contato adicionado")
        except Exception as e:
            print(f"ERRO: {e}")

    def listar_contatos(self):
        try:
            contatos = list(self.collection.find())

            if len(contatos) > 0:
                print("=" * 100)
                print("Lista de Contatos:")
                print("-" * 100)
                for contato in contatos:
                    print("*" * 100)
                    print(f"NOME: {contato['nome']}, sobrenome: {contato['sobrenome']}, numero: {contato['numero']}")
                    print("*" * 100)
                print("=" * 100)
            else:
                print("Não há contatos")
        except Exception as e:
            print(f"ERRO: {e}")

    def atualizar_contato(self, sobrenome_antigo, novo_nome, novo_sobrenome, novo_numero):
        try:
            query = {"sobrenome": sobrenome_antigo}
            new_values = {"$set": {"nome": novo_nome, "sobrenome": novo_sobrenome, "numero": novo_numero}}
            self.collection.update_one(query, new_values)
            print("Atualizado!")
        except Exception as e:
            print(f"ERRO: {e}")

    def excluir_contato(self, nome):
        try:
            query = {"nome": nome}
            self.collection.delete_one(query)
            print("Sucesso ao deletar")
        except Exception as e:
            print(f"ERRO: {e}")

def exibir_menu():
    print("\nMENU:")
    print("1. Adicionar Contatos")
    print("2. Listar Contatos")
    print("3. Atualizar Contato")
    print("4. Excluir Contato")
    print("5. Sair")

def main():
    gerenciador = GerenciadorContatos()

    while True:
        exibir_menu()
        opcao = input("Selecione uma opção:\n>>>")

        if opcao == "1":
            nome = input("Nome:\n>>>")
            sobrenome = input("Sobrenome:\n>>>")
            numero = input("Numero:\n>>>")
            gerenciador.adicionar_contato(nome, sobrenome, numero)
        elif opcao == "2":
            gerenciador.listar_contatos()
        elif opcao == "3":
            nome_antigo = input("Nome antigo:\n>>>")
            novo_nome = input("Nome atual:\n>>>")
            novo_sobrenome = input("Sobrenome atual:\n>>>")
            novo_numero = input("Numero atual:\n>>>")
            gerenciador.atualizar_contato(nome_antigo, novo_nome, novo_sobrenome, novo_numero)
        elif opcao == "4":
            nome = input("Contato a ser excluído:\n>>>")
            gerenciador.excluir_contato(nome)
        elif opcao == "5":
            print("Sair")
            sleep(3)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
