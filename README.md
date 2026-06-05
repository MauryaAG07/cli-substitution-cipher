# CLI Substitution Cipher

A terminal-based Python cryptography script utilizing a randomized substitution cipher to encrypt and decrypt localized strings.

## Architecture & Tech Stack
* **Language:** Python 3.x
* **Standard Libraries:** `random` (for cryptographic key shuffling) and `string` (for dynamic constant generation).
* **State Management:** Utilizes nested functional scopes (`encrypt` and `decrypt`) within a primary `if __name__ == "__main__":` execution block to prevent global variable leakage and maintain key integrity during the session lifecycle.

## Logic & Security Metrics
* **Dynamic Character Space:** Constructs a comprehensive 94-character mapping space using built-in `string.punctuation`, `string.digits`, and `string.ascii_letters`. Explicitly parses standard whitespace (" ") to avoid escape-sequence formatting errors caused by `string.whitespace`.
* **Symmetrical Indexing:** Implements efficient O(N) array indexing (`chars.index(char) -> key[index]`) to map and decipher text sequences iteratively.

## Known Limitations
* **Ephemeral Keys:** Cryptographic keys are randomized per execution instance via `random.shuffle()`. Keys are not persistently cached to an external database or JSON file, meaning encryption and decryption must occur sequentially within the exact same active terminal session.
* **Character Constraints:** The cipher strictly supports standard ASCII characters, numbers, and basic punctuation. Unsupported characters (e.g., tabs or complex Unicode symbols) will trigger an unhandled `ValueError` during the index mapping phase.

## Execution
```bash
git clone [https://github.com/MauryaAG07/cli-substitution-cipher.git](https://github.com/MauryaAG07/cli-substitution-cipher.git)
cd cli-substitution-cipher
python src/Encryption.py
