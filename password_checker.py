import hashlib
import getpass
import sys

def encrypt_content(content):
    hashed_content = hashlib.sha256(content.encode()).hexdigest()
    return hashed_content

def read_content_from_file(file_path):
    # Lê o conteúdo do arquivo
    with open(file_path, 'r') as file:
        return file.read().strip()

def save_content_to_file(content, file_path):
    # Salva o conteúdo em um arquivo
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    # Verifica se foram fornecidos argumentos de linha de comando
    if len(sys.argv) < 3:
        print("Uso: python script.py <caminho_do_arquivo_criptografado> <caminho_do_arquivo_de_texto>")
        sys.exit(1)

    encrypted_file_path = sys.argv[1]
    user_file_path = sys.argv[2]

    # Solicita ao usuário para fornecer uma senha e criptografa o conteúdo
    with open(user_file_path, 'r') as user_file:
        content_to_encrypt = user_file.read()

    encrypted_content = encrypt_content(content_to_encrypt)

    save_content_to_file(encrypted_content, encrypted_file_path)
    print("Conteúdo criptografado e armazenado com sucesso.")

    # Realiza o teste de comparação internamente
    stored_content = read_content_from_file(encrypted_file_path)

    # Solicita ao usuário para fornecer uma senha para teste
    user_password = getpass.getpass("Digite a senha para teste: ")
    encrypted_user_password = encrypt_content(user_password)

    if encrypted_user_password == stored_content:
        print("Senha correta.")
    else:
        print("Senha incorreta.")

if __name__ == "__main__":
    main()
