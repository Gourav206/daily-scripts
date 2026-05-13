import os, datetime
clip = os.popen('termux-clipboard-get').read()
if clip.strip():
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open('clipboard_history.txt', 'a') as f:
        f.write(f"[{time}]\n{clip}\n{'-'*30}\n")
    if "bruh" in clip.lower():
        os.system('termux-tts-speak "BRUH"')
    os.system ('termux-notification --title "CLIPBOARD SAVED" --content "' + clip[:30] + '..."')
    print ("SAVED! :3")
else:
    print ("clipboard empty :(")
