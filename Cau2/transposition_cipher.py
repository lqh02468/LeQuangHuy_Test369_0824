class TranspositionCipher:

    @staticmethod
    def encrypt(text, key):
        key = int(key)

        cipher = [''] * key

        for col in range(key):
            pointer = col

            while pointer < len(text):
                cipher[col] += text[pointer]
                pointer += key

        return ''.join(cipher)

    @staticmethod
    def decrypt(ciphertext, key):
        key = int(key)

        num_cols = -(-len(ciphertext) // key)
        num_rows = key
        num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)

        plaintext = [''] * num_cols

        col = 0
        row = 0

        for symbol in ciphertext:
            plaintext[col] += symbol
            col += 1

            if (col == num_cols) or (
                    col == num_cols - 1 and
                    row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1

        return ''.join(plaintext)