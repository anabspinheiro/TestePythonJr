from flask import Flask, request, jsonify
# importar funções para gerar e verificar hashes de senha
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# melhorar a segurança da senha armazenando como um hash, não em texto plano
USER_CREDENTIALS = {
    # substuindo "senha_segura" por uma senha forte
    "admin": generate_password_hash("senha_segura")  
}

@app.route('/login', methods=['POST'])
def login():
    # adicionando validação de entrada
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({"erro": "Nome de usuário e senha são obrigatórios"}), 400

    # verificar se o usuário existe e se a senha está correta
    if username in USER_CREDENTIALS and check_password_hash(USER_CREDENTIALS[username], password):
        return jsonify({"mensagem": "Acesso concedido"}), 200
    else:
        return jsonify({"erro": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    # desativa o modo de debug em produção
    app.run(debug=False)