# Controle de Estoque

Projeto acadêmico individual desenvolvido em Python e Django para a disciplina Software by Data Specification.

## Funcionalidade da AC1

CRUD de produtos integrado à interface web e ao banco de dados:

- Cadastrar produtos.
- Listar e buscar produtos por nome, código ou categoria.
- Editar os dados de um produto existente.
- Excluir produtos após confirmação.
- Validar campos e impedir códigos repetidos.

## Tecnologias

- Python 3.14.
- Django 5.2.17.
- SQLite.
- HTML com templates do Django e CSS.

## Executar no Windows com VS Code

Tenha o Python 3.14 instalado. Abra a pasta do projeto no VS Code; a raiz deve conter o arquivo `manage.py`.

Abra **Terminal > New Terminal** e execute os comandos abaixo, um de cada vez:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador. Mantenha o terminal aberto enquanto usa o sistema. Para encerrar o servidor, pressione **Ctrl + C** no terminal.

O comando `migrate` cria o banco e as tabelas. Em uma instalação nova, o catálogo começa vazio; cadastre um produto pela interface.

## Iniciar novamente

Depois da primeira instalação, abra a pasta do projeto e execute:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

## Campos do produto

| Campo | Descrição |
|---|---|
| Código / SKU | Identificador único, sem espaços. Letras maiúsculas e minúsculas representam o mesmo código. |
| Nome do produto | Nome obrigatório. |
| Categoria | Informação opcional. |
| Unidade de contagem | Unidade, peça ou caixa. |
| Preço de referência | Valor maior ou igual a zero. Use vírgula para os centavos, como `125,90`. |
| Estoque mínimo | Quantidade inteira maior ou igual a zero. |
| Saldo | Começa em zero nesta entrega. |

## Como verificar a funcionalidade

1. Cadastre um produto com código `TEC-001`, nome `Teclado USB`, unidade `Unidade`, preço `125,90` e estoque mínimo `3`.
2. Recarregue a página e confira se o produto permanece na lista.
3. Edite o nome e o preço. Salve e confira se o mesmo produto foi atualizado.
4. Tente cadastrar outro produto com o código `tec-001`. O sistema deve bloquear a duplicação e apresentar uma mensagem.
5. Abra a confirmação de exclusão e clique em **Cancelar**. O produto deve continuar cadastrado.
6. Abra novamente a confirmação e clique em **Confirmar exclusão**. O produto deve sair da lista.

## Organização do código

| Parte | Arquivos |
|---|---|
| Interface | `estoque/templates/estoque/` e `estoque/static/estoque/` |
| Formulário e validação | `estoque/forms.py` e `estoque/models.py` |
| Processamento das requisições | `estoque/views.py` |
| Rotas | `estoque/urls.py` e `config/urls.py` |
| Estrutura do banco | `estoque/models.py` e `estoque/migrations/` |

## Próximas entregas planejadas

| Entrega | Nova funcionalidade |
|---|---|
| AC2 | Entradas de estoque, atualização do saldo e histórico. |
| AC3 | Saídas de estoque com bloqueio de saldo insuficiente. |
| Prova | Relatório filtrado de estoque, indicação de estoque baixo e exportação CSV. |