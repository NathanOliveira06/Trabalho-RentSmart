# RentSmart - Sistema de Orçamento de Locação
# Projeto desenvolvido em Python utilizando Programação Orientada a Objetos.

import csv


class Imovel:
    """Representa um imóvel disponível para locação."""

    def __init__(self, tipo, quartos=0, vagas=0, sem_criancas=False):
        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas
        self.sem_criancas = sem_criancas

    def calcular_aluguel(self):
        """Calcula o aluguel com base no tipo, quartos e estacionamento."""
        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200
            if self.vagas == 1:
                valor += 300

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250
            if self.vagas == 1:
                valor += 300

        else:  # estúdio
            valor = 1200
            if self.vagas >= 2:
                valor += 250
                if self.vagas > 2:
                    valor += (self.vagas - 2) * 60

        # O desconto é aplicado somente para apartamentos.
        if self.tipo == "apartamento" and self.sem_criancas:
            valor -= valor * 0.05

        return valor


class Orcamento:
    """Organiza os valores e gera a projeção financeira da locação."""

    def __init__(self, imovel, parcelas):
        self.imovel = imovel
        self.parcelas = parcelas
        self.taxa_contrato = 2000
        self.aluguel_mensal = imovel.calcular_aluguel()
        self.valor_parcela = self.taxa_contrato / parcelas

    def mostrar_resumo(self):
        print("\n========== ORÇAMENTO RENTSMART ==========")
        print(f"Tipo de imóvel: {self.imovel.tipo.capitalize()}")

        if self.imovel.tipo != "estúdio":
            print(f"Quantidade de quartos: {self.imovel.quartos}")

        print(f"Quantidade de vagas: {self.imovel.vagas}")
        print(f"Aluguel mensal: R$ {self.aluguel_mensal:.2f}")

        if self.imovel.tipo == "apartamento" and self.imovel.sem_criancas:
            print("Desconto aplicado: 5%")

        print(f"Taxa contratual: R$ {self.taxa_contrato:.2f}")
        print(f"Parcelamento: {self.parcelas}x de R$ {self.valor_parcela:.2f}")
        print("-----------------------------------------")
        print(f"Total nos meses com parcela do contrato: "
              f"R$ {self.aluguel_mensal + self.valor_parcela:.2f}")
        print("=========================================\n")

    def gerar_csv(self):
        """Cria um arquivo com a previsão dos pagamentos dos 12 meses."""
        with open("projecao_rentsmart.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([
                "Mes", "Aluguel mensal (R$)",
                "Parcela da taxa contratual (R$)", "Total previsto (R$)"
            ])

            for mes in range(1, 13):
                if mes <= self.parcelas:
                    parcela = self.valor_parcela
                else:
                    parcela = 0

                total = self.aluguel_mensal + parcela
                escritor.writerow([
                    mes,
                    f"{self.aluguel_mensal:.2f}".replace(".", ","),
                    f"{parcela:.2f}".replace(".", ","),
                    f"{total:.2f}".replace(".", ",")
                ])

        print("Arquivo 'projecao_rentsmart.csv' gerado com sucesso.")


def pedir_inteiro(mensagem, minimo, maximo):
    """Solicita um número inteiro e verifica se está dentro do limite."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def escolher_imovel():
    print("=== RENTSMART: ORÇAMENTO DE LOCAÇÃO ===")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    opcao = pedir_inteiro("Escolha o tipo de imóvel: ", 1, 3)

    if opcao == 1:
        tipo = "apartamento"
    elif opcao == 2:
        tipo = "casa"
    else:
        tipo = "estúdio"

    quartos = 0
    if tipo in ["apartamento", "casa"]:
        quartos = pedir_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)

    vagas = 0
    if tipo in ["apartamento", "casa"]:
        print("Deseja uma vaga de garagem?")
        print("0 - Não")
        print("1 - Sim")
        vagas = pedir_inteiro("Escolha: ", 0, 1)
    else:
        while True:
            vagas = pedir_inteiro(
                "Quantidade de vagas para o estúdio (0 ou de 2 a 20): ", 0, 20
            )
            if vagas != 1:
                break
            print("Para estúdios, o estacionamento é vendido em pacote inicial de 2 vagas.")
            print("Digite 0 para não contratar ou 2 ou mais para contratar o pacote.")

    sem_criancas = False
    if tipo == "apartamento":
        resposta = pedir_inteiro(
            "O cliente informou que não possui crianças? (1-Sim / 0-Não): ",
            0, 1
        )
        sem_criancas = resposta == 1

    return Imovel(tipo, quartos, vagas, sem_criancas)


def main():
    imovel = escolher_imovel()
    parcelas = pedir_inteiro(
        "Em quantas parcelas deseja pagar a taxa contratual (1 a 5)? ",
        1, 5
    )

    orcamento = Orcamento(imovel, parcelas)
    orcamento.mostrar_resumo()
    orcamento.gerar_csv()


if __name__ == "__main__":
    main()
