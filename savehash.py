import hashlib

def generate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


file = input("Enter file path: ")

hash_value = generate_hash(file)

print("\nSHA-256 Hash:")
print(hash_value)

with open("hashes.txt", "w") as f:
    f.write(file + "\n")
    f.write(hash_value)

print("\nHash saved successfully!")