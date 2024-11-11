import sys
from time import sleep
import time
import os
os.system('cls')

def gradasi(text):
    # Tentukan warna gradasi 
    colors = [
        "\033[38;5;88m",  # Dark red
        "\033[38;5;130m", # Orange-red
        "\033[38;5;94m",  # Deep orange
        "\033[38;5;136m", # Orange
        "\033[38;5;166m", # Dark orange
        "\033[38;5;202m", # Red-orange
        "\033[38;5;208m", # Orange-red
        "\033[38;5;124m", # Red
        "\033[38;5;88m"   # Dark red
    ]
    
    gradiasi_text = ''
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        gradiasi_text += color + char
    gradiasi_text += "\033[0m"  # Reset color
    return gradiasi_text
 
def bernadya_lyrics():
    lines = [
        ("Belum ada satu bulan", 0.005),
        ("Ku yakin masih ada sisa wangiku di bajumu", 0.08),
        ("Namun, kau tampak baik saja", 0.08),
        ("Bahkan senyummu lebih lepas", 0.08),
        ("Sedang aku di sini hampir gila", 0.08),
        ("Kita tak temukan jalan", 0.08),
        ("Sepakat akhiri setelah beribu debat panjang", 0.08),
        ("Namun kau tampak baik saja", 0.08),
        ("Bahkan senyummu lebih lepas", 0.08),
        ("Sedang aku di sini belum terima", 0.08),
        ("Bohongkah tangismu sore itu di pelukku?", 0.09),
        ("Nyatanya pergiku pun tak lagi mengganggumu", 0.08),
        ("Apa sudah ada kabar lain yang kautunggu?", 0.08),
        ("Sudah adakah yang gantikanku", 0.08),
        ("Yang khawatirkanmu setiap waktu", 0.08),
        ("Yang cerita tentang apa pun sampai hal-hal tak perlu", 0.08),
        ("Kalau bisa, jangan buru-buru", 0.09),
        ("Kalau bisa, jangan ada dulu", 0.09)
    ]

    delays = [4, 3, 1, 1, 3, 4, 2, 2, 2, 3, 2, 2, 2, 2, 2, 4, 3, 20]

    for i, (line, char_delay) in enumerate(lines):
        if "Belum ada satu bulan" in line:
            line = line.replace("Belum ada satu bulan", gradasi("Belum ada satu bulan"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

bernadya_lyrics()