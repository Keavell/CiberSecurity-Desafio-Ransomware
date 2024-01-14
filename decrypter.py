import pyaes
import os


## Leitura do conteudo do arquivo
file_name = "teste.txt.ransomware"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## descriptografar os dados
key = b"diome-13.01.2024"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Fazer replace do arquivo por um arquivo descriptografado
os.remove(file_name)
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
