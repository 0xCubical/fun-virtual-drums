# Augumented-drums-using-cv2-and-python
The software detects blue and red colors on screen and drum sounds are played once scrolled over to mimic playing of drums.

# Packages to install first
Install python and then install cv2, numpy, pyautogui and imutils using pip command on the terminal.

# How to run the code
Firstly open this website https://www.onemotion.com/drum-machine/ on one half of your device screen.Set it to drum pads where it plays different
drum sounds by pressing the respected keys. 
On the other half, run the program and take a red and a blue object and point it at the screen that apprears. You will notice the software track it 
in the video.
Click on the drums window to make it active and then use your red and blue pointers to go to the boxes with the respective instruments. Once you touch 
the respected regions, the respective sound will ring and you can play your virtual drums!

# Basic Logic
By using contours and coordinates, I made the program detect the biggest blue and red objects in the video. Next, by assigning some rectangles to the borders
of the screen and giving them a key value, we can virtually press the keys on the website to mimic playing the drums.

# A more effective solution for the contributors
By downloading the sounds manually and then assigning it to the rectangles, we can make this project work more effeciently. It will also make it easy for the
users to use this software.

Hope you guys liked it!
