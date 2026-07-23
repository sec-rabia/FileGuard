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


with open("hashes.txt", "r") as f:
    saved_file = f.readline().strip()
    saved_hash = f.readline().strip()

new_hash = generate_hash(saved_file)

print("Checking file integrity...\n")

if new_hash == saved_hash:
    print("✔ File is Safe")
else:
    print("⚠ File Has Been Modified")