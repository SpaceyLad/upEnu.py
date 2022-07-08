# upEnu.py - Username & Password enumeration

This program is for CTF players. Do not use this script on websites and domains you do not own or have permission to scan.

# What is this?
A tool created to speed up the enumeration process when scanning a website.
The script will look through the website and print out the line and line number where it finds mentions of what we are looking for and print out the result so the user easly can get an idea of how the website works and maybe even get a clue where to look.
This is usefull on very large websited with a lot of information. But as usual, it is worth taking a look on the website and adjusting the filters get better results.

# How does it work?
paths:
The script demands a path to work with. You can give this to the script with a --url [-u] or --wordlist [-w] containing the urls seperated with \n.

Arguments:
The script also demands an argument (Except if explore mode is active.). Make sure to read the help [-h] to see all options, or run all [-A] to try them all.
If you find an interesting variable you would like to explore, but are not sure where to find, you can use --search [-S] mode to look for it. Example bellow.

Explore mode:
You can also run --explore [-e]. Then the script will look for javascript paths [.js] and print them out for you.
If you provide the script an argument while explore mode is active, it will scan the javascript files and print out the result in a seperate list.

Output and quiet mode
You print the results directly into a file running --output [-o]. Note that this will add data to the file. So if it allready exists, the data will be added in the end of the file. Combining this with --quiet [-q] mode will make the script not print out anything after it is done. This is neat if you want to data from different paths into different files and grep them or keep them for later.

# Examples
User & Pass Enumeration example
python3 upEnu.py -u http://10.0.0.x:xx/login/ -U -P

Full scan
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -A

Search Mode
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -S sText

Check result examples here.
https://github.com/SpaceyLad/upEnu.py/blob/main/Examples

# Todo:
Implement verbose mode
Implement oneline mode
Implement prompt mode [Easy mode]
