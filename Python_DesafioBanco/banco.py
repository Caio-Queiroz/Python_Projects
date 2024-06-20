class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.movimentos = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentos.append(f'Depósito: +R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido. Por favor, insira um valor positivo.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.movimentos.append(f'Saque: -R$ {valor:.2f}')
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Valor de saque inválido. Por favor, insira um valor positivo.')

    def visualizar_extrato(self):
        print('Extrato:')
        for movimento in self.movimentos:
            print(movimento)
        print(f'Saldo atual: R$ {self.saldo:.2f}')


conta = ContaBancaria()

conta.depositar(1000.50)
conta.sacar(300)
conta.depositar(500.25)

conta.visualizar_extrato()
