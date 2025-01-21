from string import ascii_letters, digits
from itertools import product
from tqdm import tqdm
import pikepdf
import msoffcrypto
import io


class BruteForce:
    all_chars = digits

    def __init__(self):
        self.min_len = 1
        self.max_len = 10

    def brute_force(self) -> str:
        for i in range(self.min_len, self.max_len + 1):
            for j in product(self.all_chars, repeat=i):
                yield "".join(j)


class CrackFile(BruteForce):
    def __init__(self, file: str):
        super().__init__()
        self.file = file

    def crack_pdf(self) -> str:
        for i in self.brute_force():
            try:
                with pikepdf.open(self.file, password=i) as p:
                    return i
            except Exception as e:
                continue

    def crack_excel(self) -> str:
        decrypted = io.BytesIO()
        with open(self.file, "rb") as f:
            excel_file = msoffcrypto.OfficeFile(f)
            for i in self.brute_force():
                try:
                    excel_file.load_key(password=i)
                    excel_file.decrypt(decrypted)
                    return i
                except Exception as e:
                    continue

    def hack(self):
        extension = self.file.split('.')[-1]
        if extension == 'pdf':
            return self.crack_pdf()
        elif extension in ['xls', 'xlsx']:
            return self.crack_excel()
