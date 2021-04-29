import json
from datetime import date
from decimal import Decimal

import MySQLdb
import pandas as pd
from flask import Flask, request

import db

app = Flask(__name__)


@app.route("/consultar_cpf/")
@app.route("/consultar_cpf/<cpf>")
def consultar_divida(cpf=None):
    # Verifica se o cpf foi informado e é válido:
    if not cpf:
        return "Error: CPF não informado!", 400
    elif not len(str(cpf)) == 11:
        return "Error: CPF inválido!", 400

    # Data de nascimento mínima para que a pessoa tenha 18 anos:
    data_minima = date((date.today().year - 18), date.today().month, date.today().day)

    # Monta o sql da consulta:
    sql = f"SELECT cpf, nome, score, divida FROM pessoa WHERE cpf = '{str(cpf)}' AND data_nascimento <= '{data_minima}'"
    # sql = "SELECT  FROM pessoa WHERE cpf = '98465715652' and data_nascimento <= '2003-04-28'"

    try:
        result_rows = db.cursor.execute(sql)
        if result_rows > 0:
            columns = [i[0] for i in db.cursor.description]  # Separa o nome das colunas.
            df = pd.DataFrame(db.cursor.fetchall(), columns=columns)  # Prepara o DataFrame.
            return df.to_json(orient="records")  # Transforma o DataFrame em json e retorna.
    except MySQLdb.OperationalError as op_error:
        print("Error: " + op_error.args[1])
        return "Error: Server error! Please contact support.", 500
    except MySQLdb.ProgrammingError as prog_error:
        print("Error: " + prog_error.args[1])
        return "Error: Server error! Please contact support.", 500

    return "Message: É necessário ter mais que 18 para utilizar esse recurso!", 200


@app.route("/pagar_divida", methods=['PUT'])
def pagar_divida():
    # Pega o body request e armazena num dicionário:
    raw_request = request.data.decode('utf-8')
    body_request = json.loads(raw_request)

    # Verifica o body request:
    if list(body_request.keys()).sort() != ['cpf', 'valor'].sort():
        return "Error: invalid body request!", 400

    # Pega a data de nascimento mínima para que a pessoa tenha 18 anos:
    data_minima = date((date.today().year - 18), date.today().month, date.today().day)

    cpf = str(body_request['cpf'])
    valor = body_request['valor']

    # Monta o SQL para fazer o update:
    sql = f"UPDATE pessoa SET divida = 0.00, score = 1000 WHERE cpf = '{cpf}' AND " \
          f"divida = CAST({valor} AS DECIMAL(65,2)) AND data_nascimento <= '{data_minima}'"

    try:
        result_rows = db.cursor.execute(sql)
        if result_rows > 0: 
            return "Message: Dívida paga com sucesso!", 200
    except MySQLdb.OperationalError as op_error:
        print("Error: " + op_error.args[1])
        return "Error: Server error! Please contact support.", 500
    except MySQLdb.ProgrammingError as prog_error:
        print("Error: " + prog_error.args[1])
        return "Error: Server error! Please contact support.", 500

    return "Message: Erro ao pagar dívida!\nVerifique os dados informados.   ", 200


if __name__ == "__main__":
    app.run(debug=True)
