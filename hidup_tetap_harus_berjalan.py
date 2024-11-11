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
 
def untungnya_lyrics():
    lines = [
        ("… Ada waktu-waktu", 0.08),
        ("Hal buruk datang berturut-turut", 0.08),
        ("Semua yang tinggal, juga yang hilang", 0.05),
        ("Seberapa pun absurdnya pasti ada makna", 0.08),
        ("… Untungnya, bumi masih berputar", 0.009),
        ("Untungnya, ku tak pilih menyerah", 0.08),
        ("Itu memang paling mudah", 0.08),
        ("Untungnya, kupilih yang lebih susah", 0.08),
        ("… Untungnya, kupakai akal sehat", 0.08),
        ("Untungnya, hidup terus berjalan", 0.08),
        ("Untungnya, ku bisa rasa", 0.08),
        ("Hal-hal baik yang datangnya belakangan", 0.08),
        ("… Untungnya, untungnya", 0.09),
        ("Hidup harus tetap berjalan", 0.09)
    ]

    delays = [5, 3, 1, 5, 2, 4, 1, 6, 3, 3, 2, 8, 1,1]

    for i, (line, char_delay) in enumerate(lines):
        if "… Untungnya, bumi masih berputar" in line:
            line = line.replace("… Untungnya, bumi masih berputar", gradasi("… Untungnya, bumi masih berputar"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

untungnya_lyrics()