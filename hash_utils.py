import hashlib

SUPPORTED_ALGORITHMS = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA224": hashlib.sha224,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512,
    "SHA3-224": hashlib.sha3_224,
    "SHA3-256": hashlib.sha3_256,
    "SHA3-384": hashlib.sha3_384,
    "SHA3-512": hashlib.sha3_512,
    "BLAKE2b": hashlib.blake2b,
    "BLAKE2s": hashlib.blake2s
}


def generate_hash(text, algorithm):
    hash_object = SUPPORTED_ALGORITHMS[algorithm]()
    hash_object.update(text.encode("utf-8"))
    return hash_object.hexdigest()


def generate_file_hash(file_path, algorithm):

    hash_object = SUPPORTED_ALGORITHMS[algorithm]()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            hash_object.update(chunk)

    return hash_object.hexdigest()