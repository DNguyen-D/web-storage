import os
import hashlib
import hmac
import base64

HASH_NAME = "sha256"
ITERATIONS = 100_000
SALT_SIZE = 16


def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    salt = os.urandom(SALT_SIZE)

    pwd_hash = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    combined = salt + pwd_hash
    return base64.b64encode(combined).decode("utf-8")


def verify_password(password: str, stored_hash: str) -> bool:
    decoded = base64.b64decode(stored_hash.encode("utf-8"))

    salt = decoded[:SALT_SIZE]
    stored_pwd_hash = decoded[SALT_SIZE:]

    new_hash = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    return hmac.compare_digest(new_hash, stored_pwd_hash)