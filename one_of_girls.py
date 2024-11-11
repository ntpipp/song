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
        ("Give me tough love", 0.09),
        ("Leave me with nothin when I come down", 0.08),
        ("My kind of love", 0.08),
        ("Push me and choke me till I pass out", 0.08),

        ("We don’t gotta be in love, no", 0.006),
        ("I don’t gotta bе the one, no", 0.08),
        ("I just wanna be onе of your girls tonight", 0.09),
        ("We don’t gotta be in love, no", 0.006),
        ("I don’t gotta be the one, no", 0.09),
        ("I just wanna be one of your girls tonight", 0.09),
        ("oh-oh...........", 0.09)
    ]

    delays = [4, 2, 4, 3, 
              0.4, 0.4, 2, 0.5, 0.5, 2, 20]

    for i, (line, char_delay) in enumerate(lines):
        if "We don’t gotta be in love, no" in line:
            line = line.replace("We don’t gotta be in love, no", gradasi("We don’t gotta be in love, no"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

lyrics()