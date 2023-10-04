import json

class Pedido:
    def __init__(self, pedido_ID, data, endereco_id, info_pagamento, data_envio, metodo_envio, taxa_envio, cod_rastreamento, status):
        self.pedido_ID = pedido_ID
        self.data = data
        self.endereco_id = endereco_id
        self.info_pagamento = info_pagamento
        self.data_envio = data_envio
        self.metodo_envio = metodo_envio
        self.taxa_envio = taxa_envio
        self.cod_rastreamento = cod_rastreamento
        self.status = status

    def salvar_pedido(self):
        with open("pedidos.json", "r") as getdata:
            data = json.load(getdata)

        data[self.pedido_ID] = self.to_dict()

        with open("pedidos.json", "w") as save:
            json.dump(data, save)
            print("Pedido salvo")
    
    def excluir_pedido(pedido_ID):
        with open("pedidos.json", "r") as getdata:
            data = json.load(getdata)

        if pedido_ID in data:
            data.pop(pedido_ID)

            with open("pedidos.json", "w") as delete:
                json.dump(data, delete)
                print("Pedido deletado")
    
    def alterar_pedido(self, pedido_ID):
        with open("pedidos.json", "r") as getdata:
            data = json.load(getdata)

        if pedido_ID in data:
            # Solicitar ao usuário os novos dados
            self.data = input("Digite a nova data: ")
            self.endereco_id = input("Digite o novo ID do endereço: ")
            self.info_pagamento = input("Digite a nova forma de pagamento: ")
            self.data_envio = input("Digite a nova data de envio: ")
            self.metodo_envio = input("Digite o novo método de envio: ")
            self.taxa_envio = input("Digite a nova taxa de envio: ")
            self.cod_rastreamento = input("Digite o novo código de rastreamento: ")
            self.status = input("Digite o novo status: ")

            # Atualizar os dados no dicionário do pedido
            data[pedido_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("pedidos.json", "w") as save:
                json.dump(data, save)
                print("Pedido atualizado com sucesso")
    
    def to_dict(self):
        return {
            "pedido_ID": self.pedido_ID,
            "data": self.data,
            "endereco_id": self.endereco_id,
            "info_pagamento": self.info_pagamento,
            "data_envio": self.data_envio,
            "metodo_envio": self.metodo_envio,
            "taxa_envio": self.taxa_envio,
            "cod_rastreamento": self.cod_rastreamento,
            "status": self.status
        }

class Livro:
    def __init__(self, livro_ID, titulo, ISBN, ano_publicacao, genero_ID, sinopse, preco, num_paginas, idioma, classificacao, estoque, fornecedor_ID, publisher_ID, autor_ID):
        self.livro_ID = livro_ID
        self.titulo = titulo
        self.ISBN = ISBN
        self.ano_publicacao = ano_publicacao
        self.genero_ID = genero_ID
        self.sinopse = sinopse
        self.preco = preco
        self.num_paginas = num_paginas
        self.idioma = idioma
        self.classificacao = classificacao
        self.estoque = estoque
        self.fornecedor_ID = fornecedor_ID
        self.publisher_ID = publisher_ID
        self.autor_ID = autor_ID

    def salvar_livro(self):
        with open("livros.json", "r") as getdata:
            data = json.load(getdata)

        data[self.livro_ID] = self.to_dict()

        with open("livros.json", "w") as save:
            json.dump(data, save)
            print("Livro salvo")

    def excluir_livro(livro_ID):
        with open("livros.json", "r") as getdata:
            data = json.load(getdata)

        if livro_ID in data:
            data.pop(livro_ID)

            with open("livros.json", "w") as delete:
                data1 = json.dump(data, delete)
                print("Livro deletado")

    def alterar_livro(self, livro_ID):
        with open("livros.json", "r") as getdata:
            data = json.load(getdata)

        if livro_ID in data:
            # Solicitar ao usuário os novos dados
            self.titulo = input("Digite o novo título: ")
            self.ISBN = input("Digite o novo ISBN: ")
            self.ano_publicacao = input("Digite o novo ano de publicação: ")
            self.genero_ID = input("Digite o novo gênero: ")
            self.sinopse = input("Digite a nova sinopse: ")
            self.preco = input("Digite o novo preço: ")
            self.num_paginas = input("Digite o novo número de páginas: ")
            self.idioma = input("Digite o novo idioma: ")
            self.classificacao = input("Digite a nova classificação: ")
            self.estoque = input("Digite o novo estoque: ")
            self.fornecedor_ID = input("Digite o novo fornecedor: ")
            self.publisher_ID = input("Digite a nova editora: ")
            self.autor_ID = input("Digite o novo autor: ")

            # Atualizar os dados no dicionário do livro
            data[livro_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("livros.json", "w") as save:
                json.dump(data, save)
                print("Livro atualizado com sucesso")

    def to_dict(self):
        return {
            "livro_ID": self.livro_ID,
            "titulo": self.titulo,
            "ISBN": self.ISBN,
            "ano_publicacao": self.ano_publicacao,
            "genero_ID": self.genero_ID,
            "sinopse": self.sinopse,
            "preco": self.preco,
            "num_paginas": self.num_paginas,
            "idioma": self.idioma,
            "classificacao": self.classificacao,
            "estoque": self.estoque,
            "fornecedor_ID": self.fornecedor_ID,
            "publisher_ID": self.publisher_ID,
            "autor_ID": self.autor_ID
        }

class Cliente:
    def __init__(self, cliente_ID, CPF, nome, endereco_ID, telefone, email, info_pagamento):
        self.cliente_ID = cliente_ID
        self.CPF = CPF
        self.nome = nome
        self.endereco_ID = endereco_ID
        self.telefone = telefone
        self.email = email
        self.info_pagamento = info_pagamento

    def salvar_cliente(self):
        with open("clientes.json", "r") as getdata:
            data = json.load(getdata)

        data[self.cliente_ID] = self.to_dict()

        with open("clientes.json", "w") as save:
            json.dump(data, save)
            print("Cliente salvo")

    def excluir_cliente(cliente_ID):
        with open("clientes.json", "r") as getdata:
            data = json.load(getdata)

        if cliente_ID in data:
            data.pop(cliente_ID)

            with open("clientes.json", "w") as delete:
                json.dump(data, delete)
                print("Cliente deletado")

    def alterar_cliente(self, cliente_ID):
        with open("clientes.json", "r") as getdata:
            data = json.load(getdata)

        if cliente_ID in data:
            # Solicitar ao usuário os novos dados
            self.CPF = input("Digite o novo CPF: ")
            self.nome = input("Digite o novo nome: ")
            self.endereco_ID = input("Digite o novo ID do endereço: ")
            self.telefone = input("Digite o novo telefone: ")
            self.email = input("Digite o novo email: ")
            self.info_pagamento = input("Digite a nova forma de pagamento: ")

            # Atualizar os dados no dicionário do cliente
            data[cliente_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("clientes.json", "w") as save:
                json.dump(data, save)
                print("Cliente atualizado com sucesso")

    def to_dict(self):
        return {
            "cliente_ID": self.cliente_ID,
            "CPF": self.CPF,
            "nome": self.nome,
            "endereco_ID": self.endereco_ID,
            "telefone": self.telefone,
            "email": self.email,
            "info_pagamento": self.info_pagamento
        }

class Fornecedor:
    def __init__(self, fornecedor_ID, nome, endereco_ID, telefone, email, info_pagamento):
        self.fornecedor_ID = fornecedor_ID
        self.nome = nome
        self.endereco_ID = endereco_ID
        self.telefone = telefone
        self.email = email
        self.info_pagamento = info_pagamento

    def salvar_fornecedor(self):
        with open("fornecedores.json", "r") as getdata:
            data = json.load(getdata)

        data[self.fornecedor_ID] = self.to_dict()

        with open("fornecedores.json", "w") as save:
            json.dump(data, save)
            print("Fornecedor salvo")

    def excluir_fornecedor(fornecedor_ID):
        with open("fornecedores.json", "r") as getdata:
            data = json.load(getdata)

        if fornecedor_ID in data:
            data.pop(fornecedor_ID)

            with open("fornecedores.json", "w") as delete:
                json.dump(data, delete)
                print("Fornecedor deletado")

    def alterar_fornecedor(self, fornecedor_ID):
        with open("fornecedores.json", "r") as getdata:
            data = json.load(getdata)

        if fornecedor_ID in data:
            # Solicitar ao usuário os novos dados
            self.nome = input("Digite o novo nome: ")
            self.endereco_ID = input("Digite o novo ID do endereço: ")
            self.telefone = input("Digite o novo telefone: ")
            self.email = input("Digite o novo email: ")
            self.info_pagamento = input("Digite a nova forma de pagamento: ")

            # Atualizar os dados no dicionário do fornecedor
            data[fornecedor_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("fornecedores.json", "w") as save:
                json.dump(data, save)
                print("Fornecedor atualizado com sucesso")

    def to_dict(self):
        return {
            "fornecedor_ID": self.fornecedor_ID,
            "nome": self.nome,
            "endereco_ID": self.endereco_ID,
            "telefone": self.telefone,
            "email": self.email,
            "info_pagamento": self.info_pagamento
        }

class Editora:
    def __init__(self, publisher_ID, nome, endereco_ID, telefone, email, registro):
        self.publisher_ID = publisher_ID
        self.nome = nome
        self.endereco_ID = endereco_ID
        self.telefone = telefone
        self.email = email
        self.registro = registro

    def salvar_editora(self):
        with open("editoras.json", "r") as getdata:
            data = json.load(getdata)

        data[self.publisher_ID] = self.to_dict()

        with open("editoras.json", "w") as save:
            json.dump(data, save)
            print("Editora salva")

    def excluir_editora(publisher_ID):
        with open("editoras.json", "r") as getdata:
            data = json.load(getdata)

        if publisher_ID in data:
            data.pop(publisher_ID)

            with open("editoras.json", "w") as delete:
                json.dump(data, delete)
                print("Editora deletada")

    def alterar_editora(self, publisher_ID):
        with open("editoras.json", "r") as getdata:
            data = json.load(getdata)

        if publisher_ID in data:
            # Solicitar ao usuário os novos dados
            self.nome = input("Digite o novo nome: ")
            self.endereco_ID = input("Digite o novo ID do endereço: ")
            self.telefone = input("Digite o novo telefone: ")
            self.email = input("Digite o novo email: ")
            self.registro = input("Digite o novo registro: ")

            # Atualizar os dados no dicionário da editora
            data[publisher_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("editoras.json", "w") as save:
                json.dump(data, save)
                print("Editora atualizada com sucesso")

    def to_dict(self):
        return {
            "publisher_ID": self.publisher_ID,
            "nome": self.nome,
            "endereco_ID": self.endereco_ID,
            "telefone": self.telefone,
            "email": self.email,
            "registro": self.registro
        }

class Autor:
    def __init__(self, autor_ID, nome, nascimento, nacionalidade, biografia):
        self.autor_ID = autor_ID
        self.nome = nome
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.biografia = biografia

    def salvar_autor(self):
        with open("autores.json", "r") as getdata:
            data = json.load(getdata)

        data[self.autor_ID] = self.to_dict()

        with open("autores.json", "w") as save:
            json.dump(data, save)
            print("Autor salvo")

    def excluir_autor(autor_ID):
        with open("autores.json", "r") as getdata:
            data = json.load(getdata)

        if autor_ID in data:
            data.pop(autor_ID)

            with open("autores.json", "w") as delete:
                json.dump(data, delete)
                print("Autor deletado")
    
    def alterar_autor(self, autor_ID):
        with open("autores.json", "r") as getdata:
            data = json.load(getdata)

        if autor_ID in data:
            # Solicitar ao usuário os novos dados
            self.nome = input("Digite o novo nome: ")
            self.nascimento = input("Digite a nova data de nascimento: ")
            self.nacionalidade = input("Digite a nova nacionalidade: ")
            self.biografia = input("Digite a nova biografia: ")

            # Atualizar os dados no dicionário do autor
            data[autor_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("autores.json", "w") as save:
                json.dump(data, save)
                print("Autor atualizado com sucesso")

    def to_dict(self):
        return {
            "autor_ID": self.autor_ID,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "nacionalidade": self.nacionalidade,
            "biografia": self.biografia
        }

class Endereco:
    def __init__(self, endereco_ID, rua, bairro, CEP, numero, referencia):
        self.endereco_ID = endereco_ID
        self.rua = rua
        self.bairro = bairro
        self.CEP = CEP
        self.numero = numero
        self.referencia = referencia

    def salvar_endereco(self):
        with open("enderecos.json", "r") as getdata:
            data = json.load(getdata)

        data[self.endereco_ID] = self.to_dict()

        with open("enderecos.json", "w") as save:
            json.dump(data, save)
            print("Endereço salvo")

    def excluir_endereco(endereco_ID):
        with open("enderecos.json", "r") as getdata:
            data = json.load(getdata)

        if endereco_ID in data:
            data.pop(endereco_ID)

            with open("enderecos.json", "w") as delete:
                json.dump(data, delete)
                print("Endereço deletado")

    def alterar_endereco(self, endereco_ID):
        with open("enderecos.json", "r") as getdata:
            data = json.load(getdata)

        if endereco_ID in data:
            # Solicitar ao usuário os novos dados
            self.rua = input("Digite a nova rua: ")
            self.bairro = input("Digite o novo bairro: ")
            self.CEP = input("Digite o novo CEP: ")
            self.numero = input("Digite o novo número: ")
            self.referencia = input("Digite o novo ponto de referência: ")

            # Atualizar os dados no dicionário do endereço
            data[endereco_ID] = self.to_dict()

            # Reescrever os dados no arquivo JSON
            with open("enderecos.json", "w") as save:
                json.dump(data, save)
                print("Endereço atualizado com sucesso")

    def to_dict(self):
        return {
            "endereco_ID": self.endereco_ID,
            "rua": self.rua,
            "bairro": self.bairro,
            "CEP": self.CEP,
            "numero": self.numero,
            "referencia": self.referencia
        }
