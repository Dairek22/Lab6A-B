import hashlib

hash_value = 'c89aa2ffb9edcc6604005196b5f0e0e4'
this_string = 'ecsc'


def hash_function(test_hashing_str):
    answer = hashlib.md5(test_hashing_str.encode())
    hashes = answer.hexdigest()
    return hashes


while this_string != 'c89aa2ffb9edcc6604005196b5f0e0e4':
    this_string = hash_function(this_string)
    print(this_string)
