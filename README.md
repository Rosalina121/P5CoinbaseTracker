# P5CoinbaseTracker
A tracker using Coinbase API that fits the Persona 5 aesthetic.

![Example](Example.png)
The tracker uses the Coinbase Python API and Rainmeter.  
Earwig Factory font available here: https://www.dafont.com/earwig-factory.font  
Original LuaTextFile skin by jsmorley from https://forum.rainmeter.net/viewtopic.php?t=6998  

# How it works?
The skin uses a Lua script to read a string from a textfile (there are some tabs to spaces shenanigans because Rainmeter). The Python script gets values from Coinbase API and writes them to said textfile. You can refresh by leftclick on the skin.
Could it be simpler? Yes. Do I know or have the time to make it simpler? Take a wild guess.  

# What goes where
LuaTextFile.ini and .lua files go to the Rainmeter skin directory.  
imgBG.ini is for the background image so put it in another skin directory.  
main.py goes wherever you want. Only thing to change there is Text.txt location, APi key and secret and account IDs (depends on your needs).
In the LuaTextFile.ini file you only have to specify the python.exe and main.py locations.  
In imgBG.ini just paste the p5bg.png file path.  

Anyway feel free to copy and change anything. The PNG file is in FullHD but you could make it work with other resolutions by cropping and resizing.
