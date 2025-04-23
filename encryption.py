import pyAesCrypt
import os

# ┌───────────────────────────────────────────────────────────┐
# │                    encrypt_file()                        │
# ├───────────────────────────────────────────────────────────┤
# │ Encrypts a single file using AES encryption, writes the   │
# │ output to `<filename>.crp`, prints confirmation, and      │
# │ deletes the original unencrypted file.                   │
# └───────────────────────────────────────────────────────────┘
def encryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    base = os.path.splitext(file)[0]
    print(f"[File '{base}' has been encrypted]")

    os.remove(file)

# ┌───────────────────────────────────────────────────────────┐
# │                    walking_by_dirs()                     │
# ├───────────────────────────────────────────────────────────┤
# │ Recursively walks through all files in `directory_path`, │
# │ calling the provided `action` (encrypt_file) │
# │ on each file encountered.                                 │
# └───────────────────────────────────────────────────────────┘
def walikngByDirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if (os.path.isfile(path)):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        
        else:
            walikngByDirs(path, password)

password = input("Enter password for encryption: ")
dirName = input("Enter dircetory name you want to decrypt: ")
print(f"🔒 Encrypting all files under '{dirName}' …")
walikngByDirs(dirName, password)