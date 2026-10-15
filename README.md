# Controle de Estoque

Projeto acadêmico individual desenvolvido por **Gabriel Rodrigues de Borba**, em Python e Django, para a disciplina **Software by Data Specification**, do curso de Análise e Desenvolvimento de Sistemas.

O sistema permite gerenciar produtos, registrar entradas e saídas de estoque, consultar saldos e exportar relatórios em CSV.

As funcionalidades integram interface web, processamento no backend e persistência no banco de dados.

## Acessar o projeto

- **Aplicação:** [Controle de Estoque](https://controle-estoque-kappa-liart.vercel.app/)
- **Relatório:** [Relatório de estoque](https://controle-estoque-kappa-liart.vercel.app/relatorio/)
- **Repositório:** [Código-fonte no GitHub](https://github.com/Dev-Borba/controle-estoque)
- **Board:** [Controle de Estoque — Faculdade](https://github.com/users/Dev-Borba/projects/1)

A aplicação está publicada no **Vercel** e utiliza **PostgreSQL hospedado no Neon**.

## Funcionalidades e entregas

| Entrega | Funcionalidade | Desenvolvimento |
|---|---|---|
| AC1 | Cadastro, consulta, busca, edição e exclusão de produtos. | Concluído |
| AC2 | Entradas de estoque com atualização automática do saldo e histórico. | Concluído |
| AC3 | Saídas de estoque com validação do saldo disponível e histórico. | Concluído |
| Prova | Relatório com filtros, identificação de estoque baixo e exportação CSV. | Concluído |

As quatro funcionalidades foram implementadas e publicadas. Os vídeos de demonstração serão disponibilizados pelo Google Drive e vinculados às respectivas fichas de entrega.

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

## Interface e temas

A interface utiliza uma identidade visual minimalista, com dois temas:

| Tema | Paleta |
|---|---|
| Claro | Branco, prata, bege e detalhes em marrom. |
| Escuro | Grafite, preto, marrom e detalhes em dourado. |

- Alternância entre os temas pelo botão no cabeçalho.
- Preferência salva no navegador para as próximas visitas.
- Na ausência de uma preferência salva, o tema inicial acompanha a configuração do sistema.
- Favicon em SVG.
- Mensagens de confirmação e validação durante as operações.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3.14 | Linguagem utilizada no ambiente de desenvolvimento. |
| Django 5.2.17 | Formulários, validações, rotas, templates e acesso ao banco. |
| PostgreSQL / Neon | Banco de dados utilizado em produção. |
| SQLite | Alternativa local quando `DATABASE_URL` não está configurada. |
| HTML e templates Django | Estrutura da interface web. |
| CSS | Estilização e definição das paletas dos temas. |
| JavaScript | Alternância dos temas e armazenamento da preferência no navegador. |
| psycopg | Conexão com PostgreSQL. |
| dj-database-url | Configuração do banco pela URL de conexão. |
| python-dotenv | Leitura das variáveis do arquivo `.env`. |
| Git e GitHub | Versionamento do código e acompanhamento das funcionalidades. |
| GitHub Projects | Organização do board do projeto. |
| Vercel | Hospedagem da aplicação. |
| DBeaver | Consulta e conferência dos registros no banco. |
| VS Code | Editor utilizado no desenvolvimento. |

## Executar no Windows com VS Code

### 1. Obter o projeto

Com Git instalado, execute:

```powershell
git clone https://github.com/Dev-Borba/controle-estoque.git
cd controle-estoque
```

Também é possível baixar o projeto pelo GitHub em **Code → Download ZIP**, extrair o arquivo e abrir a pasta no VS Code.

A raiz da pasta aberta deve conter o arquivo `manage.py`.

Abra **Terminal → Novo Terminal** e utilize o PowerShell.

### 2. Criar o ambiente virtual e instalar as dependências

Com Python 3.14 instalado, execute um comando por vez:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Os comandos deste README utilizam diretamente o Python do ambiente virtual, sem necessidade de ativá-lo manualmente.

### 3. Escolher o banco de dados

O projeto seleciona o banco de acordo com a variável `DATABASE_URL`.

#### Executar com SQLite

Quando `DATABASE_URL` não está definida ou está vazia, o Django utiliza o arquivo local `db.sqlite3`.

Essa opção permite iniciar uma instalação independente, sem configurar PostgreSQL.

Os dados do SQLite local são separados dos dados do site publicado.

#### Executar com PostgreSQL

Para utilizar PostgreSQL, crie um arquivo `.env` na mesma pasta do `manage.py` e configure:

```dotenv
DATABASE_URL="postgresql://USUARIO:SENHA@HOST/NOME_DO_BANCO?sslmode=require"
DJANGO_SECRET_KEY="SUBSTITUA_POR_UMA_CHAVE_SECRETA"
```

Substitua os valores de exemplo pelas configurações do seu banco.

Para Neon, utilize a URL de conexão fornecida pelo serviço.

O projeto carrega o arquivo `.env` automaticamente. Quando o banco está hospedado no Neon, não é necessário instalar um servidor PostgreSQL no computador.

Se o arquivo `.env` já estiver configurado para o ambiente desejado, mantenha os valores existentes.

**Não publique senhas, chaves ou URLs com credenciais.** O arquivo `.env` está incluído no `.gitignore`.

As migrações e operações serão executadas no banco configurado. Se utilizar a mesma conexão do site publicado, as alterações também aparecerão nele.

### 4. Criar as tabelas e iniciar o servidor

Execute um comando por vez:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

Mantenha o terminal aberto enquanto utiliza o sistema.

Para encerrar o servidor, pressione **Ctrl + C** no terminal.

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
- Códigos são normalizados para letras maiúsculas.
- Preços não podem ser negativos.
- Entradas e saídas exigem quantidades inteiras maiores que zero.
- Uma saída não pode superar o saldo disponível.
- A atualização do saldo e o registro da movimentação ocorrem na mesma transação.
- No PostgreSQL, o produto é bloqueado durante a movimentação para coordenar atualizações simultâneas.
- Produtos com saldo ou movimentações vinculadas não podem ser excluídos.
- Um produto é classificado com **estoque baixo** quando `saldo <= estoque_minimo`.
- O CSV utiliza os mesmos filtros aplicados ao relatório e exporta todos os resultados, sem paginação.

## Como verificar as funcionalidades

Os exemplos abaixo acompanham a sequência dos roteiros de demonstração.

Utilize um produto novo com código `VIDEO-001`. Caso esse código já exista, escolha outro e mantenha o mesmo durante todas as etapas.

Execute as verificações na ordem **AC1 → AC2 → AC3 → Prova**, preservando os dados entre elas.

### Produtos — AC1

1. Cadastre um produto com os seguintes dados:

   | Campo | Valor |
   |---|---|
   | Código | `VIDEO-001` |
   | Nome | Teclado USB |
   | Categoria | Periféricos |
   | Unidade | Unidade |
   | Preço de referência | `125,90` |
   | Estoque mínimo | `5` |

2. Confira o saldo inicial igual a `0`.
3. Recarregue a página e verifique se o produto permanece cadastrado.
4. Busque pelo código, nome ou categoria.
5. Edite o nome para `Teclado USB ABNT2` e o preço para `129,90`.
6. Salve e confira a atualização do mesmo produto.
7. Tente cadastrar outro produto com código `video-001`. A duplicação deve ser bloqueada.
8. Para verificar a exclusão, cadastre um produto temporário com código `EXC-VIDEO-001` e nome `Produto de teste`.
9. Abra a confirmação de exclusão do produto temporário e clique em **Cancelar**. Ele deve permanecer cadastrado.
10. Abra novamente a confirmação e confirme a exclusão. O produto temporário deve ser removido.

Mantenha o produto `VIDEO-001` cadastrado para as próximas verificações.

### Entradas — AC2

1. Selecione o produto `VIDEO-001`, inicialmente com saldo `0`.
2. Registre uma entrada de `10` unidades.
3. Confira o saldo atualizado para `10` e o registro no histórico.
4. Registre outra entrada de `5` unidades.
5. Confira o saldo atualizado para `15`.
6. Busque pelo código do produto no histórico e confira os dois recebimentos.
7. Recarregue a página e verifique a persistência dos dados.
8. Tente registrar uma entrada com quantidade `0`. O sistema deve rejeitar a operação.
9. Confira que o saldo permanece em `15`.

### Saídas — AC3

1. Selecione o produto `VIDEO-001`, com saldo `15`.
2. Registre uma saída de `12` unidades.
3. Confira o saldo atualizado para `3` e o registro no histórico.
4. Tente retirar `4` unidades. O sistema deve informar estoque insuficiente.
5. Tente registrar uma saída com quantidade `0`. A operação deve ser rejeitada.
6. Confira que as tentativas inválidas não alteraram o saldo nem criaram movimentações.
7. Recarregue a página e confirme que o saldo continua em `3`.

### Relatório e CSV — Prova

1. Abra o relatório e localize o produto `VIDEO-001`.
2. Confira o saldo `3` e o estoque mínimo `5`.
3. O produto deve aparecer como **Estoque baixo**, pois o saldo está abaixo do mínimo.
4. Teste a busca pelo código e pelo nome.
5. Teste o filtro de categoria utilizando `Periféricos`.
6. Selecione **Somente estoque baixo** e aplique os filtros.
7. Combine a busca por `VIDEO-001` com o filtro de estoque baixo.
8. Clique em **Exportar CSV**.
9. Abra o arquivo em um programa de planilhas ou no VS Code.
10. Compare os produtos, saldos e estoques mínimos exportados com os resultados do relatório.

O sistema também considera estoque baixo quando o saldo é exatamente igual ao estoque mínimo.

Os resultados refletem os dados existentes no momento da consulta ou da exportação.

### Temas claro e escuro

1. Abra uma página do sistema.
2. Utilize o botão de tema no cabeçalho para alternar entre claro e escuro.
3. Recarregue a página.
4. Confira que a preferência escolhida foi mantida no navegador.
5. Navegue pelas páginas de produtos, entradas, saídas e relatório e confira a aplicação do tema.

## Conferir os dados no DBeaver

Conecte o DBeaver ao mesmo banco PostgreSQL utilizado pela aplicação.

No esquema `public`, consulte:

| Tabela | Conteúdo |
|---|---|
| `estoque_produto` | Dados dos produtos, saldos e estoques mínimos. |
| `estoque_entradaestoque` | Histórico de entradas. |
| `estoque_saidaestoque` | Histórico de saídas. |

Após cadastrar um produto ou registrar uma movimentação pelo site, atualize a grade de dados no DBeaver.

Durante a sequência de demonstração, o produto `VIDEO-001` deve apresentar:

| Etapa | Operação | Saldo esperado |
|---|---|---:|
| AC1 | Cadastro do produto | 0 |
| AC2 | Entrada de 10 unidades | 10 |
| AC2 | Entrada de mais 5 unidades | 15 |
| AC3 | Saída de 12 unidades | 3 |
| AC3 | Tentativa rejeitada de saída de 4 unidades | 3 |
| Prova | Consulta ao relatório | 3 |

O relatório é gerado a partir dos dados dos produtos e seus saldos, sem uma tabela própria de relatório.

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
| Estilos e paletas dos temas | `estoque/static/estoque/styles.css` |
| Alternância e persistência do tema | `estoque/static/estoque/theme.js` |
| Favicon | `estoque/static/estoque/favicon.svg` |
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
| `DJANGO_SETTINGS_MODULE` | Define o módulo de configurações como `config.settings_producao`. |
| `DJANGO_SECRET_KEY` | Chave secreta da aplicação. |
| `DATABASE_URL` | URL de conexão PostgreSQL do Neon. |
| `DJANGO_ALLOWED_HOSTS` | Lista opcional de domínios adicionais, separados por vírgula e sem `https://`. |

O módulo de produção exige uma chave secreta e um banco PostgreSQL configurados.

Nesse ambiente:

- O modo de depuração fica desativado.
- Os cookies de sessão e CSRF utilizam a opção de transmissão segura.
- Os domínios fornecidos pelas variáveis de sistema do Vercel são adicionados aos hosts permitidos.
- As origens HTTPS desses domínios são utilizadas na configuração de CSRF.

As credenciais são configuradas nas variáveis de ambiente da hospedagem.

## Versões das entregas

| Entrega | Funcionalidade | Commit da implementação |
|---|---|---|
| AC1 | Cadastro e gerenciamento de produtos | [3ad11ed](https://github.com/Dev-Borba/controle-estoque/commit/3ad11edc03bd1f846e94334e061bf6cba7d51099) |
| AC2 | Entradas de estoque e histórico | [d9f2cd0](https://github.com/Dev-Borba/controle-estoque/commit/d9f2cd0f8e14c6cb6c02899ff059690a27a5d89f) |
| AC3 | Saídas e validação de saldo | [e8e5f28](https://github.com/Dev-Borba/controle-estoque/commit/e8e5f28e9bcd359f91c2c79ef9ae86d6e8fbba98) |
| Prova | Relatório com filtros e exportação CSV | [e9c3643](https://github.com/Dev-Borba/controle-estoque/commit/e9c3643e83c2ecd62495c86d011b538fdaa94971) |

O site publicado apresenta a versão atual do sistema.

Os commits acima identificam a implementação de cada entrega. Melhorias posteriores de interface, temas e documentação estão disponíveis no histórico do repositório.

## Organização acadêmica

As funcionalidades são acompanhadas no GitHub Projects, no quadro:

[Controle de Estoque — Faculdade](https://github.com/users/Dev-Borba/projects/1)

| Entrega | Cartão da funcionalidade |
|---|---|
| AC1 | [Cadastro e gerenciamento de produtos](https://github.com/Dev-Borba/controle-estoque/issues/1) |
| AC2 | [Entradas de estoque](https://github.com/Dev-Borba/controle-estoque/issues/3) |
| AC3 | [Saídas de estoque](https://github.com/Dev-Borba/controle-estoque/issues/4) |
| Prova | [Relatório e exportação CSV](https://github.com/Dev-Borba/controle-estoque/issues/5) |

Cada entrega acadêmica deve incluir:

- Nome completo do participante.
- Vídeo demonstrando a funcionalidade correspondente.
- Link do código-fonte no GitHub.
- Link do board de funcionalidades.
- Envio e confirmação da entrega pelo Classroom.

Os vídeos serão compartilhados pelo Google Drive, com acesso de visualização ao professor.

A Prova apresenta a funcionalidade nova de relatório com filtros e exportação CSV.

## Autor

**Gabriel Rodrigues de Borba**

Curso de **Análise e Desenvolvimento de Sistemas**.

Disciplina **Software by Data Specification**.

Projeto acadêmico individual.