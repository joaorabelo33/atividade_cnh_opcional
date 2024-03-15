

from datetime import datetime

class CarteiraDeHabilitacao:
    contador_cnh = 0

    def __init__(self, nome, rg, cpf, filiacao, primeira_habilitacao, categoria, validade, acc=False, permissao=False):
        CarteiraDeHabilitacao.contador_cnh += 1
        self.id_cnh = CarteiraDeHabilitacao.contador_cnh
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__filiacao = filiacao
        self.__primeira_habilitacao = self.validar_data(primeira_habilitacao)
        self.categoria = categoria
        self.validade = self.validar_data(validade)
        self.observacoes = ""
        self.acc = acc
        self.permissao = permissao

    def validar_data(self, data_em_texto):
        try:
            return datetime.strptime(data_em_texto, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Formato de data inválido. Utilize o formato dd/mm/aaaa.")

    def mudar_categoria(self, nova_categoria):
        self.categoria = nova_categoria

    def atualizar_validade(self, nova_validade):
        self.validade = self.validar_data(nova_validade)

    def adicionar_observacoes(self, observacao):
        self.observacoes += observacao + '\n'

    def alterar_acc(self, novo_acc):
        self.acc = novo_acc

    def alterar_permissao(self, nova_permissao):
        self.permissao = nova_permissao

    def __str__(self):
        return (f"CNH ID: {self.id_cnh}\nNome: {self.__nome}\nRG: {self.__rg}\nCPF: {self.__cpf}\n"
                f"Filiação: {self.__filiacao}\nPrimeira Habilitação: {self.__primeira_habilitacao.strftime('%d/%m/%Y')}\n"
                f"Categoria: {self.categoria}\nValidade: {self.validade.strftime('%d/%m/%Y')}\n"
                f"ACC: {'Sim' if self.acc else 'Não'}\nPermissão: {'Sim' if self.permissao else 'Não'}\n"
                f"Observações: {self.observacoes}")

cnh1 = CarteiraDeHabilitacao("Ana Beatriz", "MG-10.123.456", "123.456.789-00", "Carlos Beatriz e Joana Beatriz", "20/03/2010", "B", "20/03/2025",acc=False,permissao=True)

cnh2 = CarteiraDeHabilitacao("joao", "pi-10.123.123", "123.098.789-00", "Carlos Beatriz e Joana Beatriz", "20/03/2020", "A", "20/03/2030",acc=True,permissao=True)

print(cnh1)
print("\nApós atualizações:")
print(cnh2)
print("\nApós atualizações:")

cnh1.mudar_categoria("AB")
cnh1.atualizar_validade("20/03/2030")
cnh1.adicionar_observacoes("Inclusão de categoria A.")
cnh1.alterar_acc(False)
cnh1.alterar_permissao(False)

cnh2.mudar_categoria("A")
cnh2.atualizar_validade("20/03/2030")
cnh2.adicionar_observacoes("Inclusão de categoria AB.")
cnh2.alterar_acc(True)
cnh2.alterar_permissao(False)
print(cnh1)
print(cnh2)