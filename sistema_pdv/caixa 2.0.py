import mysql.connector


def caixa_2():
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='cadastro')
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        print('Conectado  ao Mysql versão ', db_info)

    cursor = conexao.cursor()

    comando_sql = "SELECT * FROM produtos;"
    cursor.execute(comando_sql)
    linhas = cursor.fetchall()

    print('''\n[1] CADASTRO\n[2] BALCÃO DE VENDAS''')

    opcao_balcao_ou_cadastro = int(input("Digite a opção: "))

    if opcao_balcao_ou_cadastro == 1:

        print('''\n[1] CADASTRAR PRODUTOS\n[2] DELETAR PRODUTOS\n[3] ALTERAR PRODUTOS''')

        opcao_cadastrar_deletar_alterar = int(input("Digite a opção: "))

        if opcao_cadastrar_deletar_alterar == 1:
            while True:

                comando_sql = "SELECT * FROM produtos;"
                cursor.execute(comando_sql)
                linhas = cursor.fetchall()

                mostra_o_ultimo_produto_cadastrado(linhas)

                cadastra_no_banco_dados(cursor)

                novo_produto = input("[S/N] :").upper()

                if novo_produto == "S":

                    comando_sql = "SELECT * FROM produtos;"
                    cursor.execute(comando_sql)
                    linhas = cursor.fetchall()

                    mostra_o_ultimo_produto_cadastrado(linhas)

                    cadastra_no_banco_dados(cursor)

                if novo_produto == "N":
                    break

        if opcao_cadastrar_deletar_alterar == 2:

            print(10 * "*", "PRODUTOS CADASTRADO", 10 * "*")
            for linha in linhas:
                print(linha[0], linha[1], "-" * 20, linha[2])

            codigo_id = int(input("\nCód: "))

            for linha in linhas:
                id_cod = linha[0]
                if codigo_id == id_cod:
                    print("Produto:", linha[0], linha[1], linha[2])
            comando_sql = f"DELETE FROM produtos WHERE id = '{codigo_id}' ;"
            dados = codigo_id
            cursor.execute(comando_sql, dados)

    if opcao_balcao_ou_cadastro == 2:
        pass


def mostra_o_ultimo_produto_cadastrado(linhas):
    cont = 0
    for linha in linhas:
        cont += 1
    for linha in linhas:
        id_cod = linha[0]
        if cont == id_cod:
            print(f"\núltimo produto cadastrado Cód: {linha[0]} Produto: {linha[1]} R$ {linha[2]}")
    print(f"\nQuantidade de produtos cadastrado: {cont}")



def cadastra_no_banco_dados(cursor):
    codigo_id = int(input("\nCód: "))
    descricao_produto = input("Produto: ").upper()
    preco_produto = float(input("Preço: "))

    comando_sql = "INSERT INTO produtos (id, descricao_produto, preco_produto) VALUES (%s, %s, %s)"
    dados = (codigo_id, descricao_produto, preco_produto)
    cursor.execute(comando_sql, dados)


if __name__ == "__main__":
    caixa_2()
