import os
name = ("Gourav:")
print (f"hey {name} i'm vivo y15s")
print ("total storage", os.popen('df -h $HOME | tail -1').read().split()[1])
print ("used storage", os.popen('df -h $HOME | tail -1').read().split()[2])
print ("free storage", os.popen('df -h $HOME | tail -1').read().split()[3])
print (f"hey {name} termux is working fine")
