# Controle de Estoque

Projeto acadêmico individual desenvolvido em Python e Django para a disciplina **Software by Data Specification**.

O sistema permite gerenciar produtos, registrar entradas e saídas de estoque, consultar saldos e exportar relatórios em CSV. As funcionalidades integram interface web, processamento no backend e persistência no banco de dados.

## Acessar o sistema

- **Aplicação:** https://controle-estoque-kappa-liart.vercel.app
- **Relatório:** https://controle-estoque-kappa-liart.vercel.app/relatorio/
- **Repositório:** https://github.com/Dev-Borba/controle-estoque

A aplicação está publicada no **Vercel** e utiliza **PostgreSQL hospedado no Neon**.

## Funcionalidades e entregas

| Entrega | Funcionalidade | Desenvolvimento |
|---|---|---|
| AC1 | Cadastro, consulta, busca, edição e exclusão de produtos. | Concluído |
| AC2 | Entradas de estoque com atualização do saldo e histórico. | Concluído |
| AC3 | Saídas de estoque com validação do saldo disponível e histórico. | Concluído |
| Prova | Relatório de estoque com filtros, identificação de estoque baixo e exportação CSV. | Concluído |

As quatro funcionalidades foram implementadas e publicadas. Os vídeos de demonstração e as entregas pelo Classroom permanecem pendentes.

### AC1 — Produtos

- Cadastrar e listar produtos.
- Buscar por nome, código ou categoria.
- Editar informações de produtos existentes.
- Excluir produtos após confirmação.
- Validar campos obrigatórios e valores.
- Impedir códigos duplicados, inclusive com diferenças entre letras maiúsculas e minúsculas.
- Impedir a exclusão de produtos com saldo ou movimentações vinculadas.

### AC2 — Entradas de estoque

- Selecionar um produto e informar a quantidade recebida.
- Registrar uma observação opcional.
- Aceitar somente quantidades inteiras maiores que zero.
- Aumentar o saldo automaticamente.
- Registrar a entrada e atualizar o saldo na mesma transação.
- Consultar o histórico com produto, quantidade, observação e data/hora.
- Buscar no histórico por código, nome do produto ou observação.

### AC3 — Saídas de estoque

- Selecionar um produto e informar a quantidade retirada.
- Registrar uma observação opcional.
- Aceitar somente quantidades inteiras maiores que zero.
- Bloquear retiradas superiores ao saldo disponível.
- Reduzir o saldo automaticamente.
- Registrar a saída e atualizar o saldo na mesma transação.
- Consultar e buscar no histórico de saídas.
- Preservar o saldo e o histórico quando uma tentativa for rejeitada.

### Prova — Relatório de estoque

- Consultar código, nome, categoria, unidade, saldo e estoque mínimo.
- Buscar produtos por nome ou código.
- Filtrar por categoria.
- Identificar estoque baixo quando o saldo é igual ou inferior ao estoque mínimo.
- Mostrar somente produtos com estoque baixo.
- Combinar os filtros de busca, categoria e situação do estoque.
- Exportar todos os resultados filtrados em CSV, incluindo produtos de outras páginas.
- Gerar o arquivo com cabeçalhos, acentos e separador ponto e vírgula.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem do backend. |
| Django 5.2.17 | Formulários, validações, rotas, templates e acesso ao banco. |
| PostgreSQL / Neon | Banco de dados utilizado em produção. |
| SQLite | Alternativa local quando `DATABASE_URL` não está configurada. |
| HTML e templates Django | Interface web. |
| CSS | Estilização da aplicação. |
| psycopg | Conexão com PostgreSQL. |
| dj-database-url | Configuração do banco pela URL de conexão. |
| python-dotenv | Leitura das variáveis do arquivo `.env`. |
| Git e GitHub | Versionamento do código e organização das funcionalidades. |
| Vercel | Hospedagem da aplicação. |
| DBeaver | Consulta e conferência dos registros no banco. |

O ambiente local utilizado no desenvolvimento foi Windows, VS Code e Python 3.14.

## Executar no Windows com VS Code

### 1. Obter o projeto

Com Git instalado, execute:

```powershell
git clone https://github.com/Dev-Borba/controle-estoque.git
cd controle-estoque
```

Abra a pasta `controle-estoque` no VS Code.

A raiz da pasta deve conter o arquivo `manage.py`. Abra **Terminal → Novo Terminal** e utilize o PowerShell.

### 2. Criar o ambiente virtual e instalar as dependências

Com Python 3.14 instalado, execute um comando por vez:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Os comandos deste README utilizam diretamente o Python do ambiente virtual; não é necessário ativá-lo manualmente.

### 3. Escolher o banco de dados local

O projeto seleciona o banco de acordo com a variável `DATABASE_URL`.

#### Executar com SQLite

Quando `DATABASE_URL` não está definida ou está vazia, o Django utiliza o arquivo local `db.sqlite3`.

Essa opção permite iniciar uma instalação independente, sem configurar PostgreSQL. Os dados desse arquivo são separados dos dados do site publicado.

#### Executar com PostgreSQL

Para utilizar PostgreSQL, crie um arquivo `.env` na mesma pasta do `manage.py` e configure:

```dotenv
DATABASE_URL="postgresql://USUARIO:SENHA@HOST/NOME_DO_BANCO?sslmode=require"
DJANGO_SECRET_KEY="SUBSTITUA_POR_UMA_CHAVE_SECRETA"
```

Substitua os valores de exemplo pelas configurações do seu banco. Para Neon, utilize a URL de conexão fornecida pelo serviço.

Se o arquivo `.env` já estiver configurado, mantenha os valores existentes.

O projeto carrega esse arquivo automaticamente. Não é necessário instalar um servidor PostgreSQL no computador quando o banco está hospedado no Neon.

**Não publique senhas, chaves ou URLs com credenciais.** O arquivo `.env` está incluído no `.gitignore`.

As migrações e operações serão executadas no banco configurado. Se utilizar a mesma conexão do site publicado, as alterações também aparecerão nele.

### 4. Criar as tabelas e iniciar o servidor

Execute um comando por vez:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Abra:

http://127.0.0.1:8000/

Mantenha o terminal aberto enquanto utiliza o sistema. Para encerrar o servidor, pressione **Ctrl + C**.

Em um banco novo, o catálogo começa vazio. Cadastre os produtos pela interface.

## Iniciar novamente

Depois da instalação, abra a pasta do projeto no VS Code e execute:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Após atualizar o código e instalar eventuais alterações nas dependências, aplique novas migrações antes de iniciar:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## Campos do produto

| Campo | Descrição |
|---|---|
| Código / SKU | Identificador obrigatório e único, sem espaços. É normalizado para letras maiúsculas. |
| Nome | Nome obrigatório do produto. |
| Categoria | Informação opcional utilizada na busca e no relatório. |
| Unidade | Unidade, peça ou caixa. |
| Preço de referência | Valor maior ou igual a zero. No formulário, utilize vírgula para os centavos, como `125,90`. |
| Estoque mínimo | Quantidade inteira maior ou igual a zero. |
| Saldo atual | Começa em zero e é atualizado pelas entradas e saídas. |
| Cadastrado em | Data e hora do cadastro. |
| Atualizado em | Data e hora da última atualização. |

O saldo não é editado diretamente no formulário do produto.

## Regras de negócio

- Cada produto possui um código único.
- Preços não podem ser negativos.
- Entradas e saídas exigem quantidades inteiras maiores que zero.
- Uma saída não pode superar o saldo disponível.
- A atualização do saldo e o registro da movimentação ocorrem na mesma transação.
- No PostgreSQL, o produto é bloqueado durante a movimentação para coordenar atualizações simultâneas.
- Produtos com saldo ou movimentações vinculadas não podem ser excluídos.
- Um produto é classificado com **estoque baixo** quando `saldo <= estoque_minimo`.
- O CSV utiliza os mesmos filtros aplicados ao relatório e exporta todos os resultados, sem paginação.

## Como verificar as funcionalidades

Utilize produtos de demonstração com códigos ainda não cadastrados.

### Produtos — AC1

1. Cadastre um produto com código `DEMO-001`, nome `Teclado USB`, categoria `Periféricos`, unidade `Unidade`, preço `125,90` e estoque mínimo `3`.
2. Recarregue a página e confira se o produto permanece cadastrado.
3. Busque pelo código ou pelo nome.
4. Edite o nome ou o preço e confira a atualização.
5. Tente cadastrar outro produto com código `demo-001`. A duplicação deve ser bloqueada.
6. Para testar a exclusão, utilize outro produto sem saldo e sem movimentações. Confira as opções de cancelar e confirmar.

### Entradas — AC2

1. Selecione o produto `DEMO-001` e registre uma entrada de `10` unidades.
2. Confira o saldo atualizado para `10` e a movimentação no histórico.
3. Recarregue a página e confira a persistência.
4. Tente registrar uma entrada com quantidade `0`. O sistema deve rejeitar a operação.

### Saídas — AC3

1. Registre uma saída de `7` unidades do produto `DEMO-001`.
2. Confira o saldo atualizado para `3` e a movimentação no histórico.
3. Tente retirar `4` unidades. O sistema deve informar estoque insuficiente.
4. Tente registrar uma saída com quantidade `0`. A operação deve ser rejeitada.
5. Confira que as tentativas inválidas não alteraram o saldo nem criaram movimentações.

### Relatório e CSV — Prova

1. Abra o relatório e confira o produto `DEMO-001` com saldo `3` e mínimo `3`.
2. Ele deve aparecer como **Estoque baixo**, pois o saldo é igual ao mínimo.
3. Cadastre outro produto, `DEMO-002`, com categoria `Papelaria` e mínimo `5`. Sem entradas, seu saldo será `0`, também classificado como estoque baixo.
4. Teste a busca por nome ou código e o filtro por categoria.
5. Selecione **Somente estoque baixo** e clique em **Aplicar filtros**.
6. Combine esse filtro com a categoria `Papelaria`.
7. Clique em **Exportar CSV** e compare os produtos exportados com os resultados da tela.
8. Abra o arquivo no Excel ou em um editor de texto e confira os cabeçalhos, acentos, saldos e mínimos.

Os resultados refletem os dados existentes no momento da consulta ou da exportação.

## Conferir os dados no DBeaver

Conecte o DBeaver ao mesmo banco PostgreSQL utilizado pela aplicação.

No esquema `public`, consulte:

| Tabela | Conteúdo |
|---|---|
| `estoque_produto` | Dados dos produtos, saldos e estoques mínimos. |
| `estoque_entradaestoque` | Histórico de entradas. |
| `estoque_saidaestoque` | Histórico de saídas. |

Após cadastrar um produto ou registrar uma movimentação pelo site, atualize a grade de dados no DBeaver.

O relatório consulta essas tabelas existentes; não utiliza uma tabela própria.

## Rotas principais

| Caminho | Funcionalidade |
|---|---|
| `/` | Listagem e busca de produtos. |
| `/produtos/novo/` | Cadastro de produto. |
| `/produtos/<id>/editar/` | Edição de produto. |
| `/produtos/<id>/excluir/` | Confirmação de exclusão. |
| `/entradas/` | Histórico de entradas. |
| `/entradas/nova/` | Registro de entrada. |
| `/saidas/` | Histórico de saídas. |
| `/saidas/nova/` | Registro de saída. |
| `/relatorio/` | Relatório com filtros. |
| `/relatorio/exportar/` | Exportação CSV com os filtros recebidos. |

## Organização do código

| Parte | Arquivos |
|---|---|
| Interface | `estoque/templates/estoque/` |
| Estilos e ícones | `estoque/static/estoque/` |
| Formulários | `estoque/forms.py` |
| Modelos e restrições do banco | `estoque/models.py` |
| Processamento, movimentações, relatório e CSV | `estoque/views.py` |
| Rotas | `estoque/urls.py` e `config/urls.py` |
| Migrações | `estoque/migrations/` |
| Configurações locais | `config/settings.py` |
| Configurações de produção | `config/settings_producao.py` |
| Dependências | `requirements.txt` |

## Configuração de produção

O ambiente de produção utiliza:

| Variável | Finalidade |
|---|---|
| `DJANGO_SETTINGS_MODULE` | Deve ser `config.settings_producao`. |
| `DJANGO_SECRET_KEY` | Chave secreta da aplicação. |
| `DATABASE_URL` | URL de conexão PostgreSQL do Neon. |
| `DJANGO_ALLOWED_HOSTS` | Lista opcional de domínios adicionais, separados por vírgula e sem `https://`. |

O módulo de produção exige uma chave secreta e um banco PostgreSQL configurados. Também desativa o modo de depuração e habilita cookies seguros.

Os domínios do Vercel são obtidos pelas variáveis de sistema disponíveis no ambiente da plataforma.

## Versões das entregas

| Entrega | Commit da implementação |
|---|---|
| AC2 — Entradas e histórico | `d9f2cd0` |
| AC3 — Saídas e validação de saldo | `e8e5f28` |
| Prova — Relatório e CSV | `e9c3643` |

O histórico completo está disponível na seção de commits do repositório.

## Organização acadêmica

As funcionalidades são acompanhadas no GitHub Projects, no quadro **Controle de Estoque — Faculdade**.

Cada entrega acadêmica deve incluir:

- Nome completo do participante.
- Vídeo demonstrando a funcionalidade correspondente.
- Link do código-fonte no GitHub.
- Link do board de funcionalidades.
- Envio e confirmação da entrega pelo Classroom.

A Prova corresponde à funcionalidade nova de relatório com filtros e exportação CSV.

## Autor

**Gabriel Borba**

Projeto acadêmico individual do curso de Análise e Desenvolvimento de Sistemas.