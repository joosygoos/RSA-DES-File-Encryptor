# Python Hybrid Encryption: RSA + DES File Encryptor

This project is a demonstration of a hybrid encryption system implemented in Python. It uses the strengths of both asymmetric (RSA) and symmetric (DES) cryptography to securely encrypt and decrypt a file.

The core idea is to use the fast and efficient DES algorithm to encrypt the bulk of the data (an image file) and to use the secure but slower RSA algorithm to encrypt only the DES key. This approach provides both high security and good performance.

---

## Key Concepts Demonstrated

* **Asymmetric Cryptography (RSA)**: The use of a public/private key pair. Ideal for securing small amounts of data, like encryption keys.
* **Symmetric Cryptography (DES)**: The use of a single shared secret key. Very fast and efficient for encrypting large amounts of data.
* **Hybrid Encryption**: A system that combines the convenience and security of asymmetric cryptography with the speed of symmetric cryptography to create a robust and practical security solution.

---

## How It Works

The process simulates sending a file securely from a sender to a receiver:

1.  **RSA Key Generation**: The `main.py` script starts by generating a public and private RSA key pair.
    * The **public key** can be shared freely and is used for encryption.
    * The **private key** must be kept secret and is used for decryption.

2.  **Symmetric Key Input**: The user is prompted to enter an 8-character key. This key will be used for the DES encryption.

3.  **DES Key Encryption**: The 8-character DES key is encrypted using the **RSA public key**. This ensures that only someone with the corresponding RSA private key can decrypt and view the DES key.

4.  **File Encryption**: The target file (`penguin.jpg`) is encrypted using the **DES algorithm** and the user-provided 8-character key. This process is much faster than encrypting the entire file with RSA.

5.  **Simulated Transfer**: At this point, the **encrypted file** (`penguin_encrypted.bin`) and the **RSA-encrypted DES key** would be sent over an insecure channel (like the internet).

6.  **Decryption Process**:
    * The receiver uses their **RSA private key** to decrypt the encrypted DES key.
    * With the original DES key now recovered, the receiver uses it to decrypt the file (`penguin_encrypted.bin`).
    * The final output is the decrypted file (`penguin_decrypted.jpg`), which is verified against the original to ensure the process was successful.

---

## Project Structure

The project is organized into three main files:

* `main.py`: The main driver script that orchestrates the entire encryption and decryption process. It handles file I/O, user input, and calls functions from the other two modules.
* `RSA (1).py`: A module containing the implementation of the RSA algorithm, including functions for key generation, encryption, and decryption.
* `des.py`: A module that implements the Data Encryption Standard (DES) algorithm for symmetric encryption and decryption of data blocks.

---

## How to Run

To run this project, you will need Python 3 installed.

1.  **Prepare the File**: Place an image file named `penguin.jpg` in the same directory as the Python scripts. You can substitute this with another `.jpg` file, but you will need to change the filename in `main.py`.

2.  **Execute the Script**: Run the main program from your terminal:
    ```bash
    python main.py
    ```

3.  **Enter the DES Key**: When prompted, enter a key that is exactly 8 characters long.
    ```text
    enter the DES key, 8 Characters
    > mysecret
    ```

4.  **Observe the Output**: The script will print the RSA keys, the encrypted DES key, and status messages to the console. It will also generate two new files in your directory:
    * `penguin_encrypted.bin`: The binary file containing the DES-encrypted image data.
    * `penguin_decrypted.jpg`: The final decrypted image.

The script will automatically verify if the decrypted image matches the original and print a success or failure message.

