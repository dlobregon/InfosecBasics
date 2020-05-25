# use the "hashlib" module to compute md5, sha1 and sha256 of the string "Hellow, world!"
import hashlib
inputText="Hello, world!"

# processing the MD5 hash
m= hashlib.md5()
m.update(inputText.encode("utf-8"))
md5Value= m.hexdigest()
print("MD5:")
print(md5Value)

#processing the SHA1 hash
m= hashlib.sha1()
m.update(inputText.encode("utf-8"))
sha1Value = m.hexdigest()
print("SHA1:")
print(sha1Value)

# processing the sha256 hash
m= hashlib.sha256()
m.update(inputText.encode("utf-8"))
sha256Value = m.hexdigest()
print("SHA256:")
print(sha256Value)