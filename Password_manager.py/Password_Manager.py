import os
import csv
import base64
# Cryptography imports
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Folder where all vault files will be stored
VAULT_DIR = "vaults"


def ensure_vault_folder():
    """
    Create the vaults folder if it does not exist.
    This allows storing multiple different password files.
    """
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)


def derive_key(master_password, salt):
    """
    Convert the user's master password into a secure encryption key.

    master_password → PBKDF2 (with salt & many iterations) → encryption key
    This ensures:
      - Even if 2 users choose same password, their keys differ (because of salt)
      - It is slow to brute-force because of iterations
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),   # Hash function used internally
        length=32,                   # Fernet requires 32-byte keys
        salt=salt,                   # Unique salt for this vault
        iterations=300000,           # Higher = more secure (but slower)
    )

    # Convert derived bytes into a format Fernet can use
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))


def load_vault(vault_name, master_password):
    """
    Attempt to load an existing vault.
    Returns Fernet object (for encrypt/decrypt), file path, and salt.
    If vault doesn't exist → return (None, None, None)
    """

    # Paths to salt file and CSV file
    salt_path = os.path.join(VAULT_DIR, vault_name + ".salt")
    file_path = os.path.join(VAULT_DIR, vault_name + ".csv")

    if not os.path.exists(salt_path):
        return None, None, None   # Vault does not exist

    # Read stored salt
    with open(salt_path, "rb") as f:
        salt = f.read()

    # Derive key from given password + stored salt
    key = derive_key(master_password, salt)

    # Create Fernet encryption/decryption object
    fernet = Fernet(key)

    return fernet, file_path, salt


def create_new_vault(vault_name, master_password):
    """
    Create a brand new vault:
    - Generate a random salt
    - Derive encryption key from master password
    - Create empty CSV file with header row
    """

    # Generate new random salt (salt is NOT secret, can be stored)
    salt = os.urandom(16)

    salt_path = os.path.join(VAULT_DIR, vault_name + ".salt")
    file_path = os.path.join(VAULT_DIR, vault_name + ".csv")

    # Store salt in file
    with open(salt_path, "wb") as f:
        f.write(salt)

    # Derive encryption key for this vault
    key = derive_key(master_password, salt)
    fernet = Fernet(key)

    # Create CSV with headers
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["S.No", "WebsiteName", "Username", "Password"])

    print(f"✅ Vault '{vault_name}' created successfully.")
    return fernet, file_path, salt


def add_password(fernet, file_path):
    """
    Ask user for website, username, password.
    Encrypt password and append to vault CSV.
    """

    website = input("Website Name: ")
    username = input("User Name: ")
    password = input("Password: ")

    # Encrypt password before saving (this is the core security!)
    encrypted_pass = fernet.encrypt(password.encode()).decode()

    # Get next S.No by counting rows
    with open(file_path, "r", newline="") as f:
        rows = list(csv.reader(f))
        s_no = len(rows)  # because header is row 0

    # Append new entry
    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([s_no, website, username, encrypted_pass])

    print("✅ Password saved successfully.")


def view_passwords(fernet, file_path):
    """
    Read encrypted passwords from CSV and decrypt them before showing.
    """

    with open(file_path, "r", newline="") as f:
        rows = list(csv.reader(f))

    print("\n--------- SAVED PASSWORDS ---------")
    for row in rows[1:]:  # Skip header row
        decrypted = fernet.decrypt(row[3].encode()).decode()
        print(f"{row[0]}. {row[1]} | {row[2]} | {decrypted}")
    print("-----------------------------------\n")


def main():
    ensure_vault_folder()

    print("=== PASSWORD MANAGER ===")
    print("Available Vaults:", [v.replace(".csv", "") for v in os.listdir(VAULT_DIR) if v.endswith(".csv")])

    vault_name = input("Enter vault name: ")
    master_password = input("Enter master password: ")

    # Try opening the vault
    fernet, file_path, salt = load_vault(vault_name, master_password)

    # If vault does not exist → ask user to create one
    if fernet is None:
        choice = input("Vault not found. Create new? (y/n): ")
        if choice.lower() == "y":
            fernet, file_path, salt = create_new_vault(vault_name, master_password)
        else:
            print("Exiting...")
            return

    # Main menu
    while True:
        print("""
1) View Passwords
2) Add Password
3) Quit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            view_passwords(fernet, file_path)
        elif choice == "2":
            add_password(fernet, file_path)
        elif choice == "3":
            print("Bye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

