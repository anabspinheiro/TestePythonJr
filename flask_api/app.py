from flask import Flask, request, jsonify

app = Flask(__name__)

# endpoint 1: GET saudação+nome
@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome')
    
    # retornar erro caso o nome não for fornecido
    if not nome:
        return jsonify({"erro": "O parâmetro 'nome' é obrigatorio"}), 400
    
    return jsonify({"mensagem": f"Olá, {nome}!"})

# endpoint 2: POST soma de dois valores
@app.route('/soma', methods=['POST'])
def soma():

    dados = request.get_json()
    
    # verifica os dados fornecidos e se os campos estão devidamente preenchidos
    if not dados or 'primeiro_valor' not in dados or 'segundo_valor' not in dados:
        return jsonify({"erro": "Os campos 'primeiro valor' e ' segundo valor' são obrigatorios"}), 400
    
    resultado = dados['primeiro_valor'] + dados['segundo_valor']

    return jsonify({"soma": resultado})

if __name__ == '__main__':
    app.run(debug=True)
