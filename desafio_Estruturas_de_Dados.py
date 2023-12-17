import textwrap

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= 3

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
    
    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)

        print("=== Usuário criado com sucesso! ===")
    
    def filtrar_usuario(self, cpf):
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario.cpf == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None
    
    def criar_conta(self, usuario):
        numero_conta = len(self.contas) + 1
        nova_conta = Conta(self.agencia, numero_conta, usuario)
        self.contas.append(nova_conta)

        print("\n=== Conta criada com sucesso! ===")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def main():
    banco = Banco()

    while True:
        opcao = input(
            """\n
            ================ MENU ================
            [d]\tDepositar
            [s]\tSacar
            [e]\tExtrato
            [nc]\tNova conta
            [lc]\tListar contas
            [nu]\tNovo usuário
            [q]\tSair
            => """
        )

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            banco.contas[0].depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            banco.contas[0].sacar(valor)

        elif opcao == "e":
            banco.contas[0].exibir_extrato()

        elif opcao == "nu":
            banco.criar_usuario()

        elif opcao == "nc":
            usuario_cpf = input("Informe o CPF do usuário para criar a conta: ")
            usuario = banco.filtrar_usuario(usuario_cpf)

            if usuario:
                banco.criar_conta(usuario)
            else:
                print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
            
        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
