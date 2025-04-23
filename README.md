```markdown
# AES Bulk File Encryptor/Decryptor

A simple Python utility to recursively encrypt or decrypt **all** files in a given directory (and its subdirectories) using AES-256. Leveraging [pyAesCrypt](https://pypi.org/project/pyAesCrypt/), this script:

- Encrypts each file to `<filename>.crp`, then removes the original.
- Decrypts each `.crp` file back to its original name, then removes the encrypted copy.
- Walks directory trees recursively.
- Provides a clean interactive CLI.

---

## 🚀 Features

- **AES-256 encryption/decryption** using a single password.
- **Recursive directory traversal**—process entire folder trees in one go.
- **Safe file replacement**: original (encrypted or decrypted) files are deleted after processing.
- **Single script** with “encrypt”/“decrypt” modes.
- Clear, boxed comment headers on each function for easy reference.

---

## 🛠️ Requirements

- Python **3.6+**
- [`pyAesCrypt`](https://pypi.org/project/pyAesCrypt/)  
  ```bash
  pip install pyAesCrypt
  ```

---

## 📁 Project Structure

```
.
├── encryption.py     # Encryptor
├── decryption.py     # Decryptor
└── README.md         # This file
```

---

## ⚙️ Usage

1. **Clone or download** this repo:

2. **Install dependencies**:
   ```bash
   pip install pyAesCrypt
   ```

3. **Run the script**:
   ```bash
   python aes_bulk.py
   ```

4. **Follow the prompts**:

   ```text
   Enter password: mySecretPassword
   Enter directory path: ./my_folder
   🔒 Encrypting all files under './my_folder' …
   [File 'document.txt' has been encrypted]
   …done!
   ```

---

## 🔒 Security Notes

- **Password strength**: Choose a strong password! The script does not enforce any complexity rules.
- **Backup**: Always keep backups. If you lose your password, encrypted files are irrecoverable.
- **File deletion**: Originals are removed after encryption/decryption—ensure you’re pointed at the correct directory.

---

## 📝 Contributing

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature/YourFeature`).
5. Open a Pull Request!

---

*Happy encrypting!* 🔐  
```
