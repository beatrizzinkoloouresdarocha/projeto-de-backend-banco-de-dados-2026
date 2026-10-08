from atualizacao import atualizar_pagamentos
from relatorio import gerar_relatorio


def executar():

    print("Sistema de Gestão de Clientes")
    print()

    atualizar_pagamentos()

    print()

    gerar_relatorio()


if __name__ == "__main__":
    executar()