
class SelectQuery:
  def __init__(self, file_name: str, query: str):
    self.file_name = file_name
    self.query = query


ativacoes_rede = SelectQuery("ativações_rede.csv",'''
  SELECT 
      bg.id AS "ID Rede",
      bg."name" AS "Nome da rede",
      bg.created_at AS "Data e hora de criação Rede",
      MIN(a.start_at) AS "data_e_hora_da_primeira_ativacao_rede",
      MAX(a.start_at) AS "data_e_hora_da_ultima_ativacao_rede",
      MIN(c.created_at) AS "data_e_hora_da_primeira_criacao_de_cliente_rede",
      MAX(c.created_at) AS "data_e_hora_da_ultima_criacao_de_cliente_rede"
  FROM business_group bg
  LEFT JOIN activation a ON a.business_group_id = bg.id
  LEFT JOIN customer c  ON c.business_group_id = bg.id
  GROUP BY 
      bg.id,
      bg."name",
      bg.created_at
''')

ativacoes_unidade = SelectQuery("ativações_unidade.csv", '''
  SELECT  
    b.group_id  as "ID Rede",
    b.id AS "ID unidade",
    b."name" AS "Nome da unidade",
    b.created_at AS "Data e hora de criação Unidade",
    MIN(a.start_at) AS "data_e_hora_da_primeira_ativacao_unidade",
    MAX(a.start_at) AS "data_e_hora_da_ultima_ativacao_unidade",
    MIN(p."date") as "data_e_hora_da_primeria_venda_unidade",
    MAX(p."date") as "data_e_hora_da_ultima_venda_unidade"
  FROM business b
  LEFT JOIN activation a ON a.business_id = b.id
  left join purcharse p on p.business_id = b.id 
  GROUP BY 
    b.id,
    b."name",
    b.created_at;
''')

users = SelectQuery("users.csv",'''
  SELECT
    id as "ID usuário",
    email,
    created_at as "Data da criação",
    "name" as "Nome",
    last_login_at as "data_e_hora_do_ultimo_login"
  from public."user";
''')

def select_queries():
  return ativacoes_rede, ativacoes_unidade, users
