import pyAesCrypt
import os

# ┌───────────────────────────────────────────────────────────┐
# │                    decrypt_file()                        │
# ├───────────────────────────────────────────────────────────┤
# │ Decrypts a single `.crp` file using AES decryption,       │
# │ writes the original file back, prints confirmation, and   │
# │ deletes the encrypted `.crp` file.                        │
# └───────────────────────────────────────────────────────────┘
def decryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    base = os.path.splitext(file)[0]
    print(f"[File '{base}' has been decrypted]")

    os.remove(file)

# ┌───────────────────────────────────────────────────────────┐
# │                    walking_by_dirs()                     │
# ├───────────────────────────────────────────────────────────┤
# │ Recursively walks through all files in `directory_path`, │
# │ calling the provided `action` (decrypt_file) │
# │ on each file encountered.                                 │
# └───────────────────────────────────────────────────────────┘
def walikngByDirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if (os.path.isfile(path)):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        
        else:
            walikngByDirs(path, password)

password = input("Enter password for decryption: ")
dirName = input("Enter dircetory name you want to decrypt: ")
print(f"🔓 Decrypting all files under '{dirName}' …")
walikngByDirs(dirName, password)