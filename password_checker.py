import hashlib
import getpass

def encrypt_content(content):
    hashed_content = hashlib.sha256(content.encode()).hexdigest()
    return hashed_content

def read_password_from_file(file_path):
    # Lê o conteúdo criptografado do arquivo
    with open(file_path, 'r') as file:
        return file.read().strip()

def save_content_to_file(content, file_path):
    # Salva o conteúdo criptografado em um arquivo
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    encrypted_file_path = 'encrypted_file.txt'

    # Branch 1: Solicita ao usuário para fornecer um arquivo de texto e criptografa o conteúdo
    user_file_path = input("Digite o caminho do arquivo de texto: ")

    with open(user_file_path, 'r') as user_file:
        content_to_encrypt = user_file.read()

    encrypted_content = encrypt_content(content_to_encrypt)

    save_content_to_file(encrypted_content, encrypted_file_path)
    print("Conteúdo criptografado e armazenado com sucesso.")

    # Branch 2: Realiza o teste de comparação internamente
    stored_content = read_password_from_file(encrypted_file_path)

    # Simule o mesmo processo de criptografia para a senha fornecida
    user_password = getpass.getpass("Digite a senha para teste: ")
    encrypted_user_password = encrypt_content(user_password)

    if encrypted_user_password == stored_content:
        print("Senha correta.")
    else:
        print("Senha incorreta.")

if __name__ == "__main__":
    main()