import time
# print("▄████ ▄   █    ▄████  ▄█ █      ▀▄    ▄ ████▄   ▄   █▄▄▄▄    ██▄   ▄███▄     ▄▄▄▄▄      ▄▄▄▄▀ ▄█    ▄  ▀▄    ▄ ")
# time.sleep(0.7)
# print("█▀   ▀ █  █    █▀   ▀ ██ █        █  █  █   █    █  █  ▄▀    █  █  █▀   ▀   █     ▀▄ ▀▀▀ █    ██     █   █  █  ")
# time.sleep(0.7)
# print("█▀▀ █   █ █    █▀▀    ██ █         ▀█   █   █ █   █ █▀▀▌     █   █ ██▄▄   ▄  ▀▀▀▀▄       █    ██ ██   █   ▀█   ")
# time.sleep(0.7)
# print("█   █   █ ███▄ █      ▐█ ███▄      █    ▀████ █   █ █  █     █  █  █▄   ▄▀ ▀▄▄▄▄▀       █     ▐█ █ █  █   █    ")
# time.sleep(0.7)
# print(" █  █▄ ▄█     ▀ █      ▐     ▀   ▄▀           █▄ ▄█   █      ███▀  ▀███▀               ▀       ▐ █  █ █ ▄▀     ")
# time.sleep(0.7)
# print("  ▀  ▀▀▀         ▀                             ▀▀▀   ▀                                           █   ██        ")
# time.sleep(2.5)

chicken_art = """
this is one line
this is another line
yet another line"""

for line in iter(chicken_art.splitlines()):
    print(line)
    time.sleep(0.7)

exit(0)
startGame = input("Do you dare fulfil your destiny? (Y/N): ")
if startGame == 'n' or startGame == 'N' :
    print("Bad luck")
elif startGame == 'y' or startGame == 'Y' :
    intro()