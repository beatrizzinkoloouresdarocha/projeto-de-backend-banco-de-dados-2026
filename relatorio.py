from banco import conectar


def gerar_relatorio():

    conexao = conectar()

    cursor = conexao.cursor()


    consulta = """
    SELECT

        c.nome AS cliente,

        e.nome_empresa AS empresa,

        s.nome_servico AS servico,

        p.valor,

        p.data_vencimento,

        p.data_pagamento,

        p.status AS pagamento,

        ct.status AS contrato


    FROM clientes c

    JOIN empresas e
        ON e.id_cliente = c.id_cliente

    JOIN contratos ct
        ON ct.id_empresa = e.id_empresa

    JOIN servicos s
        ON s.id_servico = ct.id_servico

    JOIN pagamentos p
        ON p.id_contrato = ct.id_contrato

    ORDER BY p.data_vencimento;
    """


    cursor.execute(consulta)

    resultados = cursor.fetchall()


    print()
    print("=" * 80)
    print("RELATÓRIO DE CLIENTES")
    print("=" * 80)


    for item in resultados:

        print(
            f"""
Cliente: {item['cliente']}
Empresa: {item['empresa']}
Serviço: {item['servico']}
Valor: R$ {item['valor']:.2f}
Vencimento: {item['data_vencimento']}
Pagamento: {item['pagamento']}
Contrato: {item['contrato']}
----------------------------------------
"""
        )


    conexao.close()


if __name__ == "__main__":

    gerar_relatorio()