# Automação-Hubspot

### Descrição

O projeto Automação-Hubspot é uma ferramenta que realiza extrações de dados do banco de dados da BIUD relacionados a ativações e upload de clientes em rede, ativações e upload de vendas em unidade e informações de criação de usuários. As extrações são salvas em arquivos CSV no Google Drive conectado à máquina local.

### Requisitos

- Python (versão 3.8 ou superior)
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/jeffexavier/automação-hubspot.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd automação-hubspot
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Configuração

#### Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```
db_database="nome_do_banco"
db_host="ip_conexao_banco"
db_port=1234  # Substitua pelo número da porta do banco de dados
db_user="usuario-banco"
db_password="senha-banco"
```

#### Arquivo `create_csv_file.py`

No arquivo `create_csv_file.py`, dentro da função `create_csv`, altere o valor da variável `base_path` para o caminho local do seu Google Drive conectado à máquina. Lembre-se de manter as duplas barras invertidas (`\\`) para evitar erros de compilação da string.

Exemplo:

```python
base_path = r'H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\'
```

### Execução

Após configurar o `.env` e o caminho do Google Drive, execute o comando:

```bash
python hubspot_queries.py
```

Se tudo estiver configurado corretamente, você verá mensagens como estas no terminal:

```
Pasta criada: H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024
Arquivo CSV criado/atualizado com sucesso em H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024\ativações_rede.csv
A pasta já existe: H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024
Arquivo CSV criado/atualizado com sucesso em H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024\ativações_unidade.csv
A pasta já existe: H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024
Arquivo CSV criado/atualizado com sucesso em H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\01-11-2024\users.csv
```

### Licença

Este projeto está licenciado sob os termos da [Licença MIT](https://opensource.org/licenses/MIT). 