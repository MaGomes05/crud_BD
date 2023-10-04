import json

def add_data_livro():
    
    livro_ID = input("Digite o ID do livro: ")
    titulo = input("Digite o titulo: ")
    ISBN = input("Digite o ISBN: ")
    ano_publicacao = input("Digite o ano de publicacao: ")
    genero_ID = input("Digite o genero: ")
    sinopse = input("Digite a sinopse: ")
    preco = input("Digite o preco: ")
    num_paginas = input("Digite o numero de paginas: ")
    idioma = input("Digite o idioma: ")
    classificacao = input("Digite a classificacao: ")
    estoque = input("Digite o estoque: ")
    fornecedor_ID = input("Digite o fornecedor: ")
    publisher_ID = input("Digite a editora: ")
    autor_ID = input("Digite o autor: ")

    dic = {
        "livro_ID" : livro_ID,
        "titulo" : titulo,
        "ISBN" : ISBN,
        "ano_publicacao" : ano_publicacao,
        "genero_ID" : genero_ID,
        "sinopse" : sinopse,
        "preco" : preco,
        "num_paginas" : num_paginas,
        "idioma" : idioma,
        "classificacao" : classificacao,
        "estoque" : estoque,
        "fornecedor_ID" : fornecedor_ID,
        "publisher_ID" : publisher_ID,
        "autor_ID" : autor_ID
    }

    with open("livros.json", "r") as getdata:
        data = json.load(getdata)

        data[livro_ID] = dic

        with open("livros.json", "w") as save:
            json.dump(data, save)
            print("Livro salvo")

def add_data_cliente():
    
    cliente_ID = input("Digite o ID do cliente: ")
    CPF = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    endereco_ID = input("Digite o endereco: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    info_pagamento = input("Digite a forma de pagamento: ")

    dic = {
        "cliente_ID" : cliente_ID,
        "CPF" : CPF,
        "nome" : nome,
        "endereco_ID" : endereco_ID,
        "telefone" : telefone,
        "email" : email,
        "info_pagamento" : info_pagamento
    }

    with open("clientes.json", "r") as getdata:
        data = json.load(getdata)

        data[cliente_ID] = dic

        with open("clientes.json", "w") as save:
            json.dump(data, save)
            print("Cliente salvo")

def add_data_fornecedor():
    
    fornecedor_ID = input("Digite o ID do fornecedor: ")
    nome = input("Digite o nome: ")
    endereco_ID = input("Digite o endereco: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    info_pagamento = input("Digite a forma de pagamento: ")

    dic = {
        "fornecedor_ID" : fornecedor_ID,
        "nome" : nome,
        "endereco_ID" : endereco_ID,
        "telefone" : telefone,
        "email" : email,
        "info_pagamento" : info_pagamento
    }

    with open("fornecedores.json", "r") as getdata:
        data = json.load(getdata)

        data[fornecedor_ID] = dic

        with open("fornecedores.json", "w") as save:
            json.dump(data, save)
            print("Fornecedor salvo")

def add_data_editora():
    
    publisher_ID = input("Digite o ID da editora: ")
    nome = input("Digite o nome: ")
    endereco_ID = input("Digite o endereco: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    registro = input("Digite o registro: ")

    dic = {
        "publisher_ID" : publisher_ID,
        "nome" : nome,
        "endereco_ID" : endereco_ID,
        "telefone" : telefone,
        "email" : email,
        "registro" : registro
    }

    with open("editoras.json", "r") as getdata:
        data = json.load(getdata)

        data[publisher_ID] = dic

        with open("editoras.json", "w") as save:
            json.dump(data, save)
            print("Editora salva")


def delete_data_livro():
    livro_ID = input("Digite o ID do cliente: ")

    with open("livros.json", "r") as getdata:
        data = json.load(getdata)

    if livro_ID in data:
        data.pop(livro_ID)

        with open("livros.json", "w") as delete:
            data1 = json.dump(data, delete)
            print("Livro deletado")

def delete_data_cliente():
    cliente_ID = input("Digite o ID do cliente: ")

    with open("clientes.json", "r") as getdata:
        data = json.load(getdata)

        if cliente_ID in data:
            data.pop(cliente_ID)

            with open("clientes.json", "w") as delete:
                data1 = json.dump(data, delete)
                print("Cliente deletado")

def delete_data_fornecedor():
    fornecedor_ID = input("Digite o ID do fornecedor: ")

    with open("fornecedores.json", "r") as getdata:
        data = json.load(getdata)

        if fornecedor_ID in data:
            data.pop(fornecedor_ID)

            with open("fornecedores.json", "w") as delete:
                data1 = json.dump(data, delete)
                print("Fornecedor deletado")                

