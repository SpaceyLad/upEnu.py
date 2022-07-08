# upEnu.py - Username & Password enumeration
This script is for CTF players. Do not use on websites and domains you do not own or have permission to scan.
## What is this?
A tool created to speed up the enumeration process when scanning websites.
The script will look through the given url/urls and print out the line and line number where it find mentions of what the user is looking for. Then it will print out the result so the user easily can get an idea of how the website works and maybe even get a clue where to look for exploits or lazy code.
This is useful on very large websites with a lot of information. But as usual, it is worth taking a look on the website and adjusting the filters to get better results.
## How does it work?
###### Paths:
The script demands a path to work with. You can give this to the script with a --url [-u] or --wordlist [-w] containing the urls separated with \n.
###### Arguments:
The script also demands an argument (Except if explore mode is active.). Make sure to read the help [-h] to see all options or run all [-A] to try them all.
If you find an interesting variable you would like to explore, but are not sure where to find it, you can use --search [-S] mode to look for it. Example bellow.
###### Explore mode:
You can also run --explore [-e]. Then the script will look for Javascript paths [.js] and print them out for you.
If you provide the script an argument while explore mode is active, it will scan the Javascript files and print out the result in a separate list.
Beware that it will scan all files, even files outside the domain. So be careful not to run this if it leads you out of scope, but rather craft a wordlist with the results given.
###### Output and quiet mode
You print the results directly into a file running --output [-o]. Note that this will add data to the file. So if it already exists, the data will be added in the end of the file. Combining this with --quiet [-q] mode will make the script not print out anything after it is done. This is neat if you want to data from different paths into different files and grep them or keep them for later.
## Examples
###### User & Pass Enumeration example
python3 upEnu.py -u http://10.0.0.x:xx/login/ -U -P
###### Full scan
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -A
###### Search Mode
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -S sText
###### Check result examples here.
https://github.com/SpaceyLad/upEnu.py/blob/main/Examples
![image](https://user-images.githubusercontent.com/87969837/177986066-191b30c0-c505-46c3-af29-3ec7f4eb9cb3.png)
## Todo:
* Implement verbose mode
* Implement "one line" mode
* Implement prompt mode [Easy mode] (Maybe with Ascii art?)
* Implement a wordlist creation mode [Make a file from explore mode]

# Why did I make this?
Because Python is fun, and this is a great exercise to improve <3
