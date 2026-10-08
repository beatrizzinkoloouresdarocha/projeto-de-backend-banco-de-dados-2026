from banco import conectar
from datetime import date


def atualizar_pagamentos():

    conexao = conectar()

    cursor = conexao.cursor()

    hoje = date.today().isoformat()

    print("=" * 50)
    print("ATUALIZAÇÃO AUTOMÁTICA")
    print("=" * 50)

    print(f"Data atual: {hoje}")
    print()


    comando = """
    UPDATE pagamentos

    SET status = 'ATRASADO'

    WHERE data_vencimento < DATE('now')

    AND data_pagamento IS NULL

    AND status = 'PENDENTE';
    """

    cursor.execute(comando)

    quantidade_atrasados = cursor.rowcount


    conexao.commit()


    print(
        f"Pagamentos marcados como atrasados: "
        f"{quantidade_atrasados}"
    )


    conexao.close()


if __name__ == "__main__":

    atualizar_pagamentos()