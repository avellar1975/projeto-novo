# Setup de ambiente
Passo-a-passo para criar um ambiente de projeto python

## pipx

Ferramenta para instalação do Poetry.

O pipx é uma ferramenta que permite instalar e executar pacotes Python em ambientes isolados, fornecendo um ecossistema limpo e independente para cada ferramenta. Ele foi projetado para resolver o problema comum de conflitos de dependências entre ferramentas Python, permitindo que você instale e use facilmente ferramentas em um ambiente isolado sem afetar o ambiente global do Python.

- Para instalar o PIPX pode utilizar o pip:

```bash
pip install pipx
```

## Poetry

### Para instalar o Poetry:

```bash
pipx install poetry
pipx ensurepath
```
Reiniciar o terminal para fazer efeito a adição das variáveis de ambientes, criadas com o último comando.

### Criando o novo projeto

```bash
poetry new novo-projeto
```

Isso criará o `novo-projeto` diretório com o seguinte conteúdo:

```
novo_projeto
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```
> Note que ele mudou o nome do projeto para novo_projeto (com underline)

## Criando o projeto no GIT

Partindo da premissa que você já está dentro do diretório criado para o projeto.

```bash
git init .
```

Instalar o `gh` do github para facilitar o envio para o repositório: 

```bash
sudo apt update
sudo apt install gh
```
> Trazer mais informações sobre o cli gh

Caso seja a primeira vez que vai vincular o computador à sua conta no github, vai precisar executar o comando abaixo:

```bash
gh auth login
```

Criar repositório através do comando abaixo, seguindo as instruções:

```bash
gh repo create
```

- Push an existing local repository to GitHub
- Path to local repository `.`
- Repository name `novo-projeto`
- Description `<vazio>`
- Visibility `Public`
- Add a remote `Yes`
- What should the new remote be called? `origin`

```bash
git add .
git commit -m 'Primeiro commit, estrutura do projeto'
git git push
```

## Ferramentas para desenvolvimento

```bash
poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add --group dev blue
poetry add --group dev isort
poetry add --group dev taskipy
```

## Ferramentas para documentação

```bash
poetry add --group doc mkdocs-material
poetry add --group doc mkdocstrings
poetry add --group doc mkdocstrings-python
```

## Ativar ambiente virtual com Poetry

```bash
poetry shell
```

## Criar documentação

```bash
mkdocs new .
```

Rodar o servidor

```bash
mkdocs serve
```

Para configurar o Mkdocs ver arquivo docs/mkdocs.yml

## Configuração do Pytest

Dentro do arquivo `pyproject.toml` ver configuração da sessão `[tool.pytest.ini_options]`

## Configuração do Isort e Blue

Dentro do arquivo `pyproject.toml` ver configuração da sessão `[tool.isort]`

## Configuração do taskipy

Dentro do arquivo `pyproject.toml` ver configuração da sessão  `[tool.taskipy.tasks]`

Executar comando `task l` para verificar todas as tarefas criadas
