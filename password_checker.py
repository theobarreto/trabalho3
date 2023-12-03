import hashlib
import getpass
import sys

def encrypt_content(content):
    hashed_content = hashlib.sha256(content.encode()).hexdigest()
    return hashed_content

def read_content_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def save_content_to_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    encrypted_file_path = 'path/to/your/encrypted_file.txt' #aqui deve ser mudado para adicionar o seu arquivo txt com a senha
    
    stored_content = read_content_from_file(encrypted_file_path)

    # solicitação ao usuário para fornecer uma senha para teste
    user_password = getpass.getpass("Digite a senha para teste: ")
    encrypted_user_password = encrypt_content(user_password)

    if encrypted_user_password == stored_content:
        print("Senha correta.")
    else:
        print("Senha incorreta.")
        sys.exit(1)

if __name__ == "__main__":
    main()
