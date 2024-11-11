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
 
def lyrics():
    lines = [
        ("Wherever you go, that’s where I’ll follow", 0.09),
        ("Nobody’s promised tomorrow", 0.08),
        ("So I’ma love you every night like it’s the last night", 0.05),
        ("Like it’s the last night", 0.08),
        ("If the world was ending", 0.009),
        ("I’d wanna be next to you", 0.08),
        ("If the party was over", 0.08),
        ("And our time on Earth was through", 0.08),
        ("I’d wanna hold you just for a while", 0.09),
        ("And die with a smile", 0.09),
        ("If the world was ending", 0.009),
        ("I’d wanna be next to you", 0.08)
    ]

    delays = [1, 1, 1, 1, 
              1, 4, 1, 4, 
              2, 1, 1, 20]

    for i, (line, char_delay) in enumerate(lines):
        if "If the world was ending" in line:
            line = line.replace("If the world was ending", gradasi("If the world was ending"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

lyrics()