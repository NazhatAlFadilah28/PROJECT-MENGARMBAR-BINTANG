#https://www.youtube.com/watch?v=PMtkPWXdnEc
#Made by Nazhat Al Fadilah

import time
import random

# Daftar kalimat untuk mengetik
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and versatile.",
    "Artificial Intelligence is the future of technology.",
    "Typing speed tests are a great way to improve your skills.",
    "Keep practicing to achieve higher accuracy and speed."
]

def typing_speed_test():
    print("Selamat datang di Typing Speed Test!")
    print("Anda akan diberikan sebuah kalimat untuk diketik.")
    print("Tekan Enter untuk memulai...\n")
    input()  # Tunggu pengguna siap

    # Pilih kalimat acak
    sentence = random.choice(sentences)
    print("Ketik kalimat berikut secepat dan seakurat mungkin:")
    print(f"\n{sentence}\n")

    # Mulai timer
    start_time = time.time()
    user_input = input("Ketik di sini: ")
    end_time = time.time()

    # Hitung waktu yang dihabiskan
    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)

    # Hitung akurasi
    words_correct = sum(1 for a, b in zip(user_input.split(), sentence.split()) if a == b)
    accuracy = (words_correct / len(sentence.split())) * 100

    # Hitung kecepatan dalam WPM (Words Per Minute)
    words_per_minute = (len(user_input.split()) / time_taken) * 60

    # Tampilkan hasil
    print("\nHasil Anda:")
    print(f"Kalimat yang diketik: {user_input}")
    print(f"Waktu yang dihabiskan: {time_taken} detik")
    print(f"Akurasi: {accuracy:.2f}%")
    print(f"Kecepatan: {words_per_minute:.2f} kata per menit (WPM)")

# Jalankan program
if __name__ == "__main__":
    typing_speed_test()
