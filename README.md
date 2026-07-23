#  FileGuard

## Objective

FileGuard is a simple cybersecurity tool developed in Python to verify the integrity of files using the SHA-256 hashing algorithm. It generates a unique hash for a file, stores it, and later verifies whether the file has been modified by comparing hash values.

---

##  Features

- Generate SHA-256 hash for any file
- Save the generated hash
- Verify file integrity
- Detect unauthorized file modifications
- Simple command-line interface
- Lightweight and easy to use

---

##  Technologies Used

- Python 3
- hashlib (Built-in Python Library)
- File Handling

---

##  Project Files

- `savehash.py` – Generates and saves the SHA-256 hash of a file.
- `verifyhash.py` – Verifies the integrity of a file by comparing hash values.
- `hashes.txt` – Stores the original SHA-256 hash.
- `test.txt` – Sample file used for testing.
- `README.md` – Project documentation.

---

## How to Run

### Step 1: Generate and Save the Hash

Run the following command:

```bash
python savehash.py
```

When prompted, enter the file name:

```text
test.txt
```

The program will generate a SHA-256 hash and save it in `hashes.txt`.



### Step 2: Verify File Integrity

Run the following command:

```bash
python verifyhash.py
```

If the file has not been modified, the output will be:

```text
Checking file integrity...

✔ File is Safe
```

If the file has been modified, the output will be:

```text
Checking file integrity...

⚠ File Has Been Modified
```



##  Workflow

1. Select a file.
2. Generate a SHA-256 hash.
3. Save the hash in `hashes.txt`.
4. Read the saved hash.
5. Generate a new SHA-256 hash for the same file.
6. Compare both hash values.
7. Display whether the file is safe or modified.

---

##  Example Output

### Generate Hash

```text
Enter file path: test.txt

SHA-256 Hash:
a591a6d40bf420404a011733cfb7b190...

Hash saved successfully!
```

### Verify File

```text
Checking file integrity...

✔ File is Safe
```

### After Modifying the File

```text
Checking file integrity...

⚠ File Has Been Modified
```

##  Purpose

This project demonstrates the use of cryptographic hashing in cybersecurity to detect unauthorized file modifications and verify data integrity.


##  Developer

Developed as a Cybersecurity Tool Project using Python.
