from cryptography.hazmat.primitives.ciphers.aead import (
    AESGCM,
)


def encrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM
    cipher = AESGCM(key)

    return cipher.encrypt(nonce, msg, None)


def decrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM
    cipher = AESGCM(key)

    return cipher.decrypt(nonce, msg, None)
