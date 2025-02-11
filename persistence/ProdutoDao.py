from persistence.Database import Database
from model.Produto import Produto
from model.Categoria import Categoria
from persistence.GenericDao import GenericDao

class ProdutoDao(GenericDao):
    def save(self, produto):
        with Database() as db:
            return db.query("""
                INSERT INTO produto (nome, preco, categoria_id, quantidade, unidade_medida)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id, cadastrado
            """, (produto.nome, produto.preco, produto.categoria.id, produto.quantidade, produto.unidadeMedida))

    def update(self, produto):
        with Database() as db:
            return db.query("""
                UPDATE produto SET
                    nome = %s,
                    preco = %s,
                    categoria_id = %s,
                    quantidade = %s,
                    unidade_medida = %s,
                    editado = NOW()
                WHERE id = %s
            """, (produto.nome, produto.preco, produto.categoria.id, produto.quantidade,
                produto.unidadeMedida, produto.id))

    def delete(self, id):
        with Database() as db:
            return db.query("DELETE FROM produto WHERE id = %s", (id,))

    def find_by_id(self, id):
        with Database() as db:
            result = db.query("""
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE p.id = %s
            """, (id,), fetch_one=True)

            if result:
                categoria = Categoria(id=result[3], nome=result[8])
                return Produto(
                    id=result[0],
                    nome=result[1],
                    preco=result[2],
                    categoria=categoria,
                    quantidade=result[4],
                    unidadeMedida=result[5],
                    cadastrado=result[6],
                    editado=result[7]
                )
            return None

    def find_all(self):
        with Database() as db:
            resultados = db.query("""
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
            """, fetch=True)

            produtos = []
            for result in resultados:
                categoria = Categoria(id=result[3], nome=result[8])
                produtos.append(Produto(
                    id=result[0],
                    nome=result[1],
                    preco=result[2],
                    categoria=categoria,
                    quantidade=result[4],
                    unidadeMedida=result[5],
                    cadastrado=result[6],
                    editado=result[7]
                ))
            return produtos

    def comprar(self, produto_id, quantidade):
        with Database() as db:
            return db.query("""
                UPDATE produto
                SET quantidade = quantidade + %s,
                    editado = NOW()
                WHERE id = %s
            """, (quantidade, produto_id))

    def vender(self, produto_id, quantidade):
        with Database() as db:
            return db.query("""
                UPDATE produto
                SET quantidade = quantidade - %s,
                    editado = NOW()
                WHERE id = %s AND quantidade >= %s
            """, (quantidade, produto_id, quantidade))

    def buscar_por_nome(self, nome):
        with Database() as db:
            resultados = db.query("""
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE p.nome ILIKE %s
            """, (f'%{nome}%',), fetch=True)

            return self._mapear_resultados(resultados)

    def buscar_por_categoria(self, categoria_id):
        with Database() as db:
            resultados = db.query("""
                SELECT p.*, c.nome as categoria_nome
                FROM produto p
                JOIN categoria c ON p.categoria_id = c.id
                WHERE c.id = %s
            """, (categoria_id,), fetch=True)

            return self._mapear_resultados(resultados)

    def _mapear_resultados(self, resultados):
        produtos = []
        for result in resultados:
            categoria = Categoria(id=result[3], nome=result[8])
            produtos.append(Produto(
                id=result[0],
                nome=result[1],
                preco=result[2],
                categoria=categoria,
                quantidade=result[4],
                unidadeMedida=result[5],
                cadastrado=result[6],
                editado=result[7]
            ))
        return produtos
