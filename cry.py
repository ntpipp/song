import sys
from time import sleep
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen

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
        ("It's making you cry every time", 0.2),
        ("You give your love to me this way", 0.1),
        ("Saying you'd wait for me to stay", 0.1),
        ("I know it hurts you", 0.1),
        ("But I need to tell you something", 0.1),
        ("My heart just can't be faithful for long", 0.1),
        ("I swear I'll only make you cry", 0.01),
        ("Maybe I'd change for you someday", 0.1),
        ("But I can't help the way I feel", 0.1),
        ("Wish I was good, wish that I could", 0.1),
        ("Give you my love now", 0.1),

        ("But I need to tell you something", 0.1),
        ("My heart just can't be faithful for long", 0.1),
        ("I swear I'll only make you cry..........", 0.01),
    ]

    delays = [2, 3, 3, 3, 
              4, 6, 6, 4, 4, 4, 
              3, 7, 6, 20]

    for i, (line, char_delay) in enumerate(lines):
        if "I swear I'll only make you cry" in line:
            line = line.replace("I swear I'll only make you cry", gradasi("I swear I'll only make you cry"))
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

lyrics()