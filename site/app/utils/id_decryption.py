import hashlib
import base64
import os
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

load_dotenv()
uuid_key = os.getenv("ID_KEY")

def decrypt_id(encrypted_str: str) -> str:
    key = hashlib.sha256(uuid_key.encode()).digest()
    
    # Удаляем добавленные рандомные данные
    clean = encrypted_str[:len(encrypted_str)-128]
    
    # Первый этап декодирования
    combined2 = base64.b64decode(clean)
    iv2 = combined2[:AES.block_size]
    cipher2 = AES.new(key, AES.MODE_CBC, iv=iv2)
    pt = unpad(cipher2.decrypt(combined2[AES.block_size:]), AES.block_size).decode()
    
    # Второй этап декодирования
    combined = base64.b64decode(pt)
    iv = combined[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(combined[AES.block_size:]), AES.block_size).decode()