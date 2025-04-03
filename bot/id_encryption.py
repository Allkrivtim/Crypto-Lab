import hashlib
import base64
import os
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

load_dotenv()
uuid_key = os.getenv("ID_KEY")

def encrypt_id(id_str: str) -> str:
    # Генерируем ключ из UUID
    key = hashlib.sha256(uuid_key.encode()).digest()
    
    # Шифруем данные
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(id_str.encode(), AES.block_size))
    
    # Первое кодирование (IV + ciphertext)
    combined = cipher.iv + ct_bytes
    encoded = base64.b64encode(combined).decode()
    
    # Второй раунд шифрования и кодирования
    cipher2 = AES.new(key, AES.MODE_CBC)
    ct_bytes2 = cipher2.encrypt(pad(encoded.encode(), AES.block_size))
    combined2 = cipher2.iv + ct_bytes2
    
    # Финал: кодирование + добавление рандомных данных
    final = base64.b64encode(combined2).decode() + os.urandom(64).hex()
    return final