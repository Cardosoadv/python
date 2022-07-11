import conect
import datetime

class Clientes:

  hoje = datetime.date.today()

  def pegar_clientes():
    sql = "SELECT 'u'.'id', 'u'.'username', 'u'.'email', 'd'.'nome', 'd'.'cpf_cnpj', 'd'.'data_nascimento', 'd'.'telefone', 'd'.'img' FROM 'users' 'u' LEFT JOIN 'auth_groups_users' 'g' ON 'g'.'user_id'='u'.'id' LEFT JOIN 'dbc_users_data' 'd' ON 'd'.'user_id'='u'.'id' WHERE 'g'.'group_id' = 2"
    cursor = conect.banco.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

## Inserir clientes

  def novo_data_cliente(nome, cpf_cnpj,data_nascimento,telefone,img, user_id):
    param = [(nome, cpf_cnpj,data_nascimento,telefone,img, user_id)]
    sql = "INSERT INTO 'dbc_users_data'('nome', 'cpf_cnpj', 'data_nascimento', 'telefone', 'img', 'user_id') VALUES (%s, %s, %s, %s, %s)"
    cursor = conect.banco.cursor(sql,param)
    cursor.execute(sql, param)
    cursor.commit()
    
  def novo_group_cliente(user_id):
    param = [(user_id,2)]
    sql= "INSERT INTO 'auth_groups_users'('group_id', 'user_id') VALUES (%s, %s)"
    cursor = conect.banco.cursor()
    cursor.execute(sql, param)
    cursor.commit()
    
  def novo_cliente(username, email, nome, cpf_cnpj, data_nascimento, telefone, img):
    param = [(username,	email, Clientes.hoje)]
    sql = "INSERT INTO 'USERS' VALUES (%s, %s, %s)"
    cursor = conect.banco.cursor()
    cursor.execute(sql, param)
    user_id = cursor.lastrowid
    Clientes.novo_data_cliente(nome, cpf_cnpj,data_nascimento,telefone,img, user_id)
    Clientes.novo_group_cliente(user_id)
    cursor.commit()
  
## Editar clientes
  
  def data_cliente(nome, cpf_cnpj,data_nascimento,telefone,img, user_id):
    param = [(nome, cpf_cnpj,data_nascimento,telefone,img, user_id)]
    sql = "UPDATE 'dbc_users_data' SET (nome, cpf_cnpj,data_nascimento,telefone,img) VALUES (%s, %s, %s, %s, %s) WHERE id = %s"
    cursor = conect.banco.cursor(sql,param)
    cursor.execute(sql, param)
    cursor.commit()
    
  def editar_cliente(username, email, nome, cpf_cnpj, data_nascimento, telefone, img, user_id):
    param = [(username,	email, Clientes.hoje, user_id)]
    sql = "UPDATE 'users' SET (username,	email, updated_at) VALUES (%s, %s, %s) WHERE id = %s"
    cursor = conect.banco.cursor()
    cursor.execute(sql, param)
    Clientes.data_cliente(nome, cpf_cnpj,data_nascimento,telefone,img, user_id)
    cursor.commit()