# this is meant to brute force and try all the possible hashes till one matches.

# import the library module
import sys
import hashlib

if sys.version_info < (3, 6):
	import sha3

target = "67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2"

if __name__ == "__main__":
    for i in range(0, 10000):
        string = str(i)
        encoded_str = string.encode()
        obj_sha3_256 = hashlib.sha3_256(encoded_str)
        # print(obj_sha3_256)
        output = obj_sha3_256.hexdigest()
        if output == target:
            print("the hashed number is ", i)
            break
    
print("finished")