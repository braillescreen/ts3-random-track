"""
Random TopSpeed3 track.
This bit of code will allow you to make a Top Speed track.
See readme.md for more details.
"""
import random, sys
import pyperclip

trackData = ""


print("Welcome to the Top Speed Track creator.\n")
minimumLines = input(
    "Enter the minimum amount of lines you would like this track to have."
)
maximumLines = input(
    "Enter the maximum amount of lines you would like this track to have."
)
if minimumLines == "" or maximumLines == "":
    # Blank fields, exit.
    print("Error: One of the fields are blank. Press enter to exit.")
    input()
    sys.exit()
lines = random.randint(int(minimumLines), int(maximumLines))
# Create our track's data.
for i in range(lines):
    trackData += (
        str(random.randint(0, 8))
        + " "
        + str(random.randint(0, 4))
        + " "
        + str(random.randint(0, 11))
        + " "
        + str(random.randint(5000, 50000))
        + "\n"
    )
print("Successfully wrote " + str(lines) + " lines for your track.")
pyperclip.copy(trackData)
print("Successfully copied the track data to the clipboard. Press enter to exit.")
input()
