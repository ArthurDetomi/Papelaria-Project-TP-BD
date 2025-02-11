"""Módulo ProdutoDao.

Contém a classe ProdutoDao, responsável pelas operações de acesso a dados da entidade Produto.
"""

from persistence.GenericDao import GenericDao
from persistence.Database import Database
from model.Produto import Produto
from model.Categoria import Categoria


class ProdutoDao(GenericDao):
    """DAO (Data Access Object) para a entidade Produto."""

    def find_by_nome(self, nome) -> Produto | None:
        """
        Recupera um produto com base no nome.

        :param nome: Nome do produto.
        :return: Objeto Produto se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query(
                "SELECT * FROM produto WHERE nome = %s",
                params=(nome,),
                fetch_one=True
            )

        if result is None:
            return None

        id_, nome, preco, categoria, quantidade, unidade_medida, cadastrado, editado = result
        return Produto(
            id=id_,
            nome=nome,
            preco=preco,
            categoria=categoria,
            quantidade=quantidade,
            unidade_medida=unidade_medida,
            cadastrado=cadastrado,
            editado=editado
        )

    def update_quantidade(self, produto: Produto):
        """
        Atualiza a quantidade e o timestamp de edição de um produto.

        :param produto: Objeto Produto com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            result = db.query(
                "UPDATE produto SET quantidade = %s, editado = %s WHERE id = %s",
                (produto.quantidade, produto.editado, produto.id,)
            )
        return result

    def save(self, produto):
        """
        Insere um novo produto no banco de dados.

        :param produto: Objeto Produto a ser salvo.
        :return: Resultado da operação de inserção.
        """
        with Database() as db:
            return db.query(
                """
                INSERT INTO produto (nome, preco, categoria_id, quantidade, unidade_medida)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id, cadastrado
                """,
                (produto.nome, produto.preco, produto.categoria.id, produto.quantidade, produto.unidade_medida)
            )

    def update(self, produto):
        """
        Atualiza os dados de um produto existente.

        :param produto: Objeto Produto com os dados atualizados.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            return db.query(
                """
                UPDATE produto SET
                    nome = %s,
                    preco = %s,
                    categoria_id = %s,
                    quantidade = %s,
                    unidade_medida = %s,
                    editado = NOW()
                WHERE id = %s
                """,
                (
                    produto.nome,
                    produto.preco,
                    produto.categoria.id,
                    produto.quantidade,
                    produto.unidade_medida,
                    produto.id
                )
            )

    def delete(self, id):
        """
        Remove um produto do banco de dados com base no seu ID.

        :param id: ID do produto a ser removido.
        :return: Resultado da operação de exclusão.
        """
        with Database() as db:
            return db.query("DELETE FROM produto WHERE id = %s", (id,))

    def find_by_id(self, id):
        """
        Recupera um produto com base no seu ID, incluindo o nome da categoria.

        :param id: ID do produto.
        :return: Objeto Produto se encontrado, caso contrário None.
        """
        with Database() as db:
            result = db.query(
                """
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE p.id = %s
                """,
                (id,),
                fetch_one=True
            )

            if result:
                categoria = Categoria(id=result[3], nome=result[8])
                return Produto(
                    id=result[0],
                    nome=result[1],
                    preco=result[2],
                    categoria=categoria,
                    quantidade=result[4],
                    unidade_medida=result[5],
                    cadastrado=result[6],
                    editado=result[7]
                )
            return None

    def find_all(self):
        """
        Recupera todos os produtos, incluindo o nome da categoria associada.

        :return: Lista de objetos Produto.
        """
        with Database() as db:
            resultados = db.query(
                """
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                """,
                fetch=True
            )

            produtos = []
            for result in resultados:
                categoria = Categoria(id=result[3], nome=result[8])
                produtos.append(Produto(
                    id=result[0],
                    nome=result[1],
                    preco=result[2],
                    categoria=categoria,
                    quantidade=result[4],
                    unidade_medida=result[5],
                    cadastrado=result[6],
                    editado=result[7]
                ))
            return produtos

    def comprar(self, produto_id, quantidade):
        """
        Incrementa a quantidade de um produto (compra).

        :param produto_id: ID do produto.
        :param quantidade: Quantidade a ser adicionada.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            return db.query(
                """
                UPDATE produto
                SET quantidade = quantidade + %s,
                    editado = NOW()
                WHERE id = %s
                """,
                (quantidade, produto_id)
            )

    def vender(self, produto_id, quantidade):
        """
        Decrementa a quantidade de um produto (venda), se houver estoque suficiente.

        :param produto_id: ID do produto.
        :param quantidade: Quantidade a ser subtraída.
        :return: Resultado da operação de atualização.
        """
        with Database() as db:
            return db.query(
                """
                UPDATE produto
                SET quantidade = quantidade - %s,
                    editado = NOW()
                WHERE id = %s AND quantidade >= %s
                """,
                (quantidade, produto_id, quantidade)
            )

    def buscar_por_nome(self, nome):
        """
        Busca produtos cujo nome contenha o termo especificado.

        :param nome: Termo a ser buscado no nome do produto.
        :return: Lista de objetos Produto que correspondem à busca.
        """
        with Database() as db:
            resultados = db.query(
                """
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE p.nome ILIKE %s
                """,
                (f'%{nome}%',),
                fetch=True
            )
            return self._mapear_resultados(resultados)

    def buscar_por_categoria(self, categoria_id):
        """
        Busca produtos que pertencem a uma categoria específica.

        :param categoria_id: ID da categoria.
        :return: Lista de objetos Produto que pertencem à categoria.
        """
        with Database() as db:
            resultados = db.query(
                """
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE c.id = %s
                """,
                (categoria_id,),
                fetch=True
            )
            return self._mapear_resultados(resultados)

    def _mapear_resultados(self, resultados):
        """
        Mapeia os resultados de uma consulta SQL para objetos Produto.

        :param resultados: Resultados da consulta SQL.
        :return: Lista de objetos Produto.
        """
        produtos = []
        for result in resultados:
            categoria = Categoria(id=result[3], nome=result[8])
            produtos.append(Produto(
                id=result[0],
                nome=result[1],
                preco=result[2],
                categoria=categoria,
                quantidade=result[4],
                unidade_medida=result[5],
                cadastrado=result[6],
                editado=result[7]
            ))
        return produtos
