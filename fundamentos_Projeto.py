class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.limite_saque = 500
        self.extrato = ""
        self.num_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if self._pode_sacar(valor):
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.num_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação de saque falhou.")

    def _pode_sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite_saque
        excedeu_saques = self.num_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Limite de saque excedido.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido.")
        elif valor <= 0:
            print("Operação falhou! O valor do saque é inválido.")
        else:
            return True

        return False

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Nenhuma movimentação realizada." if not self.extrato else self.extrato)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==========================================")


if __name__ == "__main__":
    conta_bancaria = ContaBancaria()

    while True:
        menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """

        opcao = input(menu)

        if opcao == "d":
            valor_deposito = float(input("Informe o valor do depósito: "))
            conta_bancaria.depositar(valor_deposito)
        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))
            conta_bancaria.sacar(valor_saque)
        elif opcao == "e":
            conta_bancaria.exibir_extrato()
        elif opcao == "q":
            print("Sessão encerrada. Obrigado por utilizar nossos serviços.")
            break
        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")
