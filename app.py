from flask import Flask, request, jsonify

app = Flask(__name__)

# Función para el Cifrado César
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        effective_shift = -shift
    else:
        effective_shift = shift

    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + effective_shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'a' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start + effective_shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            result += char
    return result

# Endpoint para encriptar un mensaje
@app.route('/api/encrypt', methods=['POST'])
def encrypt_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos JSON"}), 400
    if 'message' not in data or 'shift' not in data:
        return jsonify({"error": "Faltan 'message' o 'shift' en los datos"}), 400
    
    message = data['message']
    shift = data['shift']

    if not isinstance(shift, int):
        return jsonify({"error": "'shift' debe ser un número entero"}), 400

    encrypted_text = caesar_cipher(message, shift, mode='encrypt')
    return jsonify({"encrypted_message": encrypted_text})

# Endpoint para desencriptar un mensaje
@app.route('/api/decrypt', methods=['POST'])
def decrypt_message():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos JSON"}), 400
    if 'message' not in data or 'shift' not in data:
        return jsonify({"error": "Faltan 'message' o 'shift' en los datos"}), 400
    
    message = data['message']
    shift = data['shift']

    if not isinstance(shift, int):
        return jsonify({"error": "'shift' debe ser un número entero"}), 400

    decrypted_text = caesar_cipher(message, shift, mode='decrypt')
    return jsonify({"decrypted_message": decrypted_text})

# Código para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5001)