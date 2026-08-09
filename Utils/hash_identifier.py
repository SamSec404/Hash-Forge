HASH_LENGTHS = {
    32: "MD5",
    40: "SHA1",
    56: "SHA224",
    64: "SHA256",
    96: "SHA384",
    128: "SHA512",
}


def identify_hash(hash_value):

    hash_value = hash_value.strip()

    length = len(hash_value)

    return HASH_LENGTHS.get(
        length,
        "Unknown"
    )
