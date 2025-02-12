# Papelaria - Sistema de Gestão de Papelaria

Este projeto é um sistema de gestão para uma papelaria, desenvolvido em Python e utilizando PostgreSQL como sistema gerenciador de banco de dados (SGBD). O sistema permite a realização de operações de CRUD e outras funcionalidades para a gestão de produtos, clientes e vendas.

## Autores

- Lucas Valentim
- Isabelle Cristine
- Igor Serpa
- Geraldo Arthur Detomi

## 1. Visão Geral do Projeto

O projeto tem como objetivo gerenciar as operações de uma papelaria, realizando operações de CRUD (criação, leitura, atualização e exclusão) e outras funcionalidades inerentes à gestão dos produtos, clientes e vendas. Desenvolvido em Python, o sistema se conecta a um banco de dados PostgreSQL, onde as tabelas e dados são previamente estruturados e/ou populados através de scripts SQL.

## 2. Requisitos e Pré-requisitos

### 2.1. Requisitos do Projeto

- **Linguagem de Programação:** Python
- **Banco de Dados:** PostgreSQL
- **Dependências:** Listadas no arquivo `requirements.txt` (localizado no diretório principal)
- **Scripts SQL:**
  - `db_schema.sql` para criação das tabelas.
  - `populate_db.sql` para inserção de dados iniciais.
- **Configurações de Conexão:** Definidas no arquivo `db.properties`

### 2.2. Pré-requisitos para Execução

- **Python:** Versão compatível com o projeto (recomendado Python 3.8 ou superior).
- **PostgreSQL:** Instalado na máquina (para a opção de uso local) ou Docker instalado (para a opção via container).
- **Docker e Docker Compose:** Necessários para a configuração do banco via container, caso opte-se por essa abordagem.
- **Ambiente Virtual:** Recomendado para isolar as dependências do projeto.

## 3. Configuração do Ambiente de Desenvolvimento

### 3.1. Criação e Ativação do Ambiente Virtual

1. **Criar o ambiente virtual:**

   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual:**
   - **No Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **No Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

### 3.2. Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Configuração do Banco de Dados

Para que o sistema funcione corretamente, é necessário configurar o banco de dados PostgreSQL. Existem duas abordagens para essa configuração:

### 4.1. Configuração com PostgreSQL Local

1. **Instalar o PostgreSQL** e garantir que ele esteja em execução.
2. **Criar o banco de dados e executar os scripts SQL:**
   ```bash
   psql -U admin -d db_tp -f database_scripts/db_schema.sql
   psql -U admin -d db_tp -f database_scripts/populate_db.sql
   ```
3. **Configurar o arquivo `db.properties`:**
   ```properties
   user=admin
   password=123
   port=5432
   host=localhost
   database=db_tp
   ```

### 4.2. Configuração com Docker

1. **Navegar até a pasta `docker` e rodar o comando:**
   ```bash
   docker compose up -d
   ```
2. **Verificar as configurações no arquivo `db.properties`, garantindo que os valores sejam os mesmos do `docker-compose.yml`.**

## 5. Execução do Sistema

1. **Ativar o ambiente virtual** e garantir que as dependências estejam instaladas.
2. **Certificar-se de que o banco de dados está configurado corretamente.**
3. **Executar o sistema:**
   ```bash
   python main.py
   ```

Caso ocorra algum erro de conexão, verifique as configurações do `db.properties` e os scripts SQL.

## 6. Considerações Finais

Este README fornece as instruções necessárias para configurar e executar o sistema de gestão da papelaria. Seguindo corretamente os passos, o ambiente estará pronto para uso.

**Lucas Valentim, Isabelle Cristine, Igor Serpa, Geraldo Arthur Detomi**
