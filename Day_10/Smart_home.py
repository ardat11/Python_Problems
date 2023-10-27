#You’re making a voice recognition system.
#The given code declares the list of supported commands.

#Task
#Complete the program to take a command as input, check if it's supported, and output "OK", if it is and "Unknown" if it's not.
supported = ["Lights off", "Lock the door",
    "Open the door", "Make coffee", "Shut down"]

x = input()
y = x.capitalize()

if y in supported:
    print("OK")

else:
    print("Unknown")


