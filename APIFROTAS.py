from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        'id': 1,
        'placa': 'AZP3E72',
        'nome': 'Marcio Vitor Machado'
    },
    {
        'id': 2,
        'placa': 'XYZ9K45',
        'nome': 'Ana Clara Souza'
    },
    {
        'id': 3,
        'placa': 'QWE7L89',
        'nome': 'Carlos Eduardo Lima'
    },
    {
        'id': 4,
        'placa': 'RTY2M34',
        'nome': 'Fernanda Silva'
    }
]

#consultar
@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios)

#consultar
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuarios_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

 #editar
@app.route('/usuarios/<int:id>',methods=['PUT'])
def editar_usuario_id(id):
    usuario_editado = request.get_json()
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_editado)
            return jsonify(usuarios[indice])

#adicionar

@app.route('/usuarios', methods=['POST'])
def incluir_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)

    return jsonify(usuarios)

#excluir

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]

    return jsonify(usuarios)

app.run(port=5000, host='localhost', debug=True) 



#consultar id, todos e excluir

#1- CRIAR API QUE DISPONIBILIZA A CONSULTA, CRIAÇÃO, EDIÇÃO E EXCLUSAO DE CADASTROS DE COMBUSTIVEL 
#2- URL BASE - localhost
#3- Endpoints
#    -localhost/beneficiario (GET)
#   -localhost/beneficiario (POST)
#   -localhost/beneficiario/id (GET)
#  -localhost/beneficiario/id (PUT)
# -localhost/beneficiario/id (DELETE)
#4 - Recursos - Combustivel

