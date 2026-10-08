from datetime import datetime
from zoneinfo import ZoneInfo

from banco import conectar


def atualizar_pagamentos():

    conexao = conectar()

    cursor = conexao.cursor()

    hoje = datetime.now(
        ZoneInfo("America/Sao_Paulo")
    ).date().isoformat()

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