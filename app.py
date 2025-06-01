from flask import Flask, request, jsonify

app = Flask(__name__)

# Función para el Cifrado César
def caesar_cipher(text_to_process, shift_amount, mode='encrypt'): # Renombrado de parámetros para mayor claridad
    processed_result = '' # Renombrado de variable
    
    # Ajuste del desplazamiento según el modo (encriptar/desencriptar)
    if mode == 'decrypt':
        effective_shift = -shift_amount
    else:
        effective_shift = shift_amount

    for char in text_to_process:
        if 'A' <= char <= 'Z':
            start_ord = ord('A') # Renombrado de variable
            shifted_char_code = (ord(char) - start_ord + effective_shift) % 26 + start_ord
            processed_result += chr(shifted_char_code)
        elif 'a' <= char <= 'z':
            start_ord = ord('a') # Renombrado de variable
            shifted_char_code = (ord(char) - start_ord + effective_shift) % 26 + start_ord
            processed_result += chr(shifted_char_code)
        else:
            processed_result += char # Los caracteres no alfabéticos se mantienen sin cambios
    return processed_result

# Endpoint para encriptar un mensaje
@app.route('/api/encrypt', methods=['POST'])
def encrypt_message():
    request_data = request.get_json() # Renombrado de variable
    
    if not request_data:
        return jsonify({"error": "No se enviaron datos JSON en la solicitud."}), 400 # Mensaje de error ligeramente modificado
    
    # Validar la presencia de las claves requeridas
    if 'message' not in request_data or 'shift' not in request_data:
        return jsonify({"error": "Faltan 'message' o 'shift' en los datos de la solicitud."}), 400 # Mensaje de error ligeramente modificado
    
    message_to_encrypt = request_data['message'] # Renombrado de variable
    encryption_shift = request_data['shift'] # Renombrado de variable

    # Validar que el desplazamiento sea un entero
    if not isinstance(encryption_shift, int):
        return jsonify({"error": "'shift' debe ser un número entero válido."}), 400 # Mensaje de error ligeramente modificado

    encrypted_text = caesar_cipher(message_to_encrypt, encryption_shift, mode='encrypt')
    return jsonify({"encrypted_message": encrypted_text})

# Endpoint para desencriptar un mensaje
@app.route('/api/decrypt', methods=['POST'])
def decrypt_message():
    request_data = request.get_json() # Renombrado de variable
    
    if not request_data:
        return jsonify({"error": "No se enviaron datos JSON en la solicitud."}), 400 # Mensaje de error ligeramente modificado
    
    # Validar la presencia de las claves requeridas
    if 'message' not in request_data or 'shift' not in request_data:
        return jsonify({"error": "Faltan 'message' o 'shift' en los datos de la solicitud."}), 400 # Mensaje de error ligeramente modificado
    
    message_to_decrypt = request_data['message'] # Renombrado de variable
    decryption_shift = request_data['shift'] # Renombrado de variable

    # Validar que el desplazamiento sea un entero
    if not isinstance(decryption_shift, int):
        return jsonify({"error": "'shift' debe ser un número entero válido."}), 400 # Mensaje de error ligeramente modificado

    decrypted_text = caesar_cipher(message_to_decrypt, decryption_shift, mode='decrypt')
    return jsonify({"decrypted_message": decrypted_text})

# Código para ejecutar la aplicación
if __name__ == '__main__':
    # La aplicación se ejecuta en modo depuración (útil para desarrollo)
    # y en el puerto 5001.
    app.run(debug=True, port=5001)