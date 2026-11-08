from pathlib import Path

path = Path("programming_poll.txt")

print("Mengapa Anda menyukai pemrograman?")
print("Ketik 'q' untuk berhenti.")

while True:
    answer = input("Alasan Anda: ")

    if answer.lower() == "q":
        break

    with path.open("a") as file:
        file.write(answer + "\n")

print("Jawaban berhasil disimpan.")