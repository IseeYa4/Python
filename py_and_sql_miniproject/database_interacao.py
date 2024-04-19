import mysql.connector
import os

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="funcionario_data",
)

def resetar_ids(db):
    cursor = db.cursor()
    cursor.execute("SET @count = 0;")
    cursor.execute("UPDATE funcionarios SET funcionario_id = @count:= @count + 1;")
    db.commit()

def inserir_data(db):
    nome = input("Nome:")
    cargo = input("Cargo:")
    loja = input("Loja")
    val = (nome, cargo, loja)
    cursor = db.cursor()
    sql = "INSERT INTO funcionarios(nome, cargo, loja) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} dados inseridos".format(cursor.rowcount))
    resetar_ids(db)

def mostrar_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM funcionarios ORDER BY funcionario_id"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Nao existe data!")
    else:
        for data in resultado:
            print(data)

def atualizar_data(db):
    cursor = db.cursor()
    mostrar_data(db)
    funcionario_id = input("Escolha ID funcionario >")
    nome = input("Novo nome:")
    cargo = input("Novo cargo:")
    loja = input("Nova loja:")
    sql = "UPDATE funcionarios SET nome=%s, cargo=%s, loja=%s WHERE funcionario_id=%s"
    val = (nome, cargo, loja, funcionario_id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data foi atualizada!".format(cursor.rowcount))

def eliminar_data(db):
    cursor = db.cursor()
    mostrar_data(db)
    funcionarios_id = input("Escolha ID funcionario>")
    sql = "DELETE FROM funcionarios WHERE funcionario_id=%s"
    val = (funcionarios_id,)
    cursor.execute(sql, val, id)
    db.commit()
    print("{} data foi eliminada".format(cursor.rowcount))
    resetar_ids(db)

def pesquisar_data(db):
    cursor = db.cursor()
    procurar = input("Palavra-chave: ")
    sql = "SELECT * FROM funcionarios WHERE nome LIKE %s OR cargo LIKE %s OR loja LIKE %s"
    val = ("%" + procurar + "%", "%" + procurar + "%", "%" + procurar + "%")
    cursor.execute(sql, val)
    resultado = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Nao existe data.")
    else:
        for data in resultado:
            print(data)

def duplicar_registro(db):
    cursor = db.cursor()
    mostrar_data(db)
    funcionario_id = input("Escolha o ID do funcionário a ser duplicado: ")
    sql_select = "SELECT nome, cargo, loja FROM funcionarios WHERE funcionario_id = %s"
    cursor.execute(sql_select, (funcionario_id,))
    resultado = cursor.fetchone()

    if not resultado:
        print("O ID do funcionário não existe.")
        return

    nome, cargo, loja = resultado

    # Insere um novo registro com os mesmos valores, exceto pelo ID
    sql_insert = "INSERT INTO funcionarios (nome, cargo, loja) VALUES (%s, %s, %s)"
    val = (nome, cargo, loja)
    cursor.execute(sql_insert, val)
    db.commit()

    print("Registro duplicado com sucesso.")
    resetar_ids(db)

def mostrar_menu(db):
    print("=== DATABASE PYTHON ===")
    print("1 Inserir data")
    print("2 Mostrar data")
    print("3 Atualizar data")
    print("4 Eliminar data")
    print("5 Procurar data")
    print("6 Duplicar data")
    print("7 Resetar data")
    print("0 Sair")
    print("------------------------")
    menu = input("Escolha menu> ")

    # Limpar tela
    os.system("clear")

    if menu == "1":
        inserir_data(db)
    elif menu == "2":
        mostrar_data(db)
    elif menu == "3":
        atualizar_data(db)
    elif menu == "4":
        eliminar_data(db)
    elif menu == "5":
        pesquisar_data(db)
    elif menu == "6":
        duplicar_registro(db)
    elif menu == "7":
        resetar_ids(db)
    elif menu == "0":
        exit()
    else:
        print("opcao nao existe")

if __name__ == "__main__":
    while True:
        mostrar_menu(db)
