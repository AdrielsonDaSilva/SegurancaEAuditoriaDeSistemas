# -*- coding: utf-8 -*-

# ==========================================================
# Exercício 1: Cifrando e Decifrando Arquivos com Cabeçalho
# ==========================================================

# 1. Cria o arquivo de entrada (arquivo original)
texto = b'Ola, este eh um arquivo secreto para teste de criptografia!'
with open("arquivoSecreto.txt", "wb") as f:
    f.write(texto)
print("Arquivo de entrada criado!")

# 2. Importa as bibliotecas necessárias
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# 3. Função para criptografar usando AES-CBC com padding PKCS7
def encrypt_aes(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    return encryptor.update(padded) + encryptor.finalize()

# 4. Função para descriptografar usando AES-CBC com padding PKCS7
def decrypt_aes(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()

# 5. Função para cifrar arquivo com cabeçalho personalizado
def cifrarArquivo(arquivo, chave):
    with open(arquivo, "rb") as f:
        arqBin = f.read()
    iv = secrets.token_bytes(16)
    enc = encrypt_aes(chave, iv, arqBin)
    header = bytearray()
    header += b'ED'             # Identificador
    header += bytes([0x01])     # Versão
    header += bytes([0x01])     # Algoritmo (AES)
    header += bytes([0x01])     # Modo (CBC)
    header += iv                # IV (16 bytes)
    header += bytes(11)         # Reservado
    completo = header + enc
    with open(arquivo+'.enc', "wb") as f:
        f.write(completo)
    print("Arquivo cifrado salvo como:", arquivo+'.enc')
    return iv  # retorna o IV para uso na decifragem

# 6. Função para decifrar arquivo com cabeçalho personalizado
def decifrarArquivo(arquivo_cifrado, chave, arquivo_saida):
    with open(arquivo_cifrado, "rb") as f:
        header = f.read(32)
        ciphertext = f.read()
    if header[0:2] != b'ED':
        raise Exception("Arquivo não possui cabeçalho válido!")
    iv = header[5:21]
    dados = decrypt_aes(chave, iv, ciphertext)
    with open(arquivo_saida, "wb") as f:
        f.write(dados)
    print("Arquivo decifrado salvo como:", arquivo_saida)

# 7. Executa o fluxo de cifragem e decifragem
chave = bytes([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
arquivo_original = "arquivoSecreto.txt"
arquivo_cifrado = arquivo_original + ".enc"
arquivo_recuperado = "arquivoSecreto_recuperado.txt"

# Cifrar
cifrarArquivo(arquivo_original, chave)

# Decifrar
decifrarArquivo(arquivo_cifrado, chave, arquivo_recuperado)

# 8. Verifica se o arquivo recuperado é igual ao original
with open(arquivo_original, "rb") as f1, open(arquivo_recuperado, "rb") as f2:
    print("Recuperação OK?", f1.read() == f2.read())

# ==========================================================
# Exercício 2: Gerando Arquivo de Metadados para Integridade
# ==========================================================

# 9. Função para gerar arquivo de metadados (48 bytes)
def gerar_metadado(arquivo_entrada, chave, arquivo_meta):
    with open(arquivo_entrada, "rb") as f:
        dados = f.read()
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    dados_padded = padder.update(dados) + padder.finalize()
    ciphertext = encryptor.update(dados_padded) + encryptor.finalize()
    fingerprint = ciphertext[-16:]  # Último bloco
    header = bytearray()
    header += b'CF'             # Identificador
    header += bytes([1])        # Versão
    header += bytes([1])        # Algoritmo
    header += bytes([1])        # Modo
    header += iv                # IV
    header += fingerprint       # Fingerprint
    header += bytes(11)         # Reservado
    with open(arquivo_meta, "wb") as f:
        f.write(header)
    print("Arquivo de metadados salvo como:", arquivo_meta)
    return iv  # retorna o IV para uso na verificação

# 10. Função para verificar integridade do arquivo usando o metadado
def verificar_integridade(arquivo_entrada, chave, arquivo_meta):
    with open(arquivo_meta, "rb") as f:
        meta = f.read(48)
    if meta[0:2] != b'CF':
        print("Arquivo de metadados inválido!")
        return False
    iv = meta[5:21]
    fingerprint_armazenado = meta[21:37]
    with open(arquivo_entrada, "rb") as f:
        dados = f.read()
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    dados_padded = padder.update(dados) + padder.finalize()
    ciphertext = encryptor.update(dados_padded) + encryptor.finalize()
    fingerprint_atual = ciphertext[-16:]
    if fingerprint_atual == fingerprint_armazenado:
        print("Integridade OK: arquivo não foi alterado.")
        return True
    else:
        print("Integridade FALHOU: arquivo foi alterado!")
        return False

# 11. Executa o fluxo de geração e verificação de metadados
arquivo_meta = "arquivoSecreto.txt.meta"
gerar_metadado(arquivo_original, chave, arquivo_meta)
verificar_integridade(arquivo_original, chave, arquivo_meta)