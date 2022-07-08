#!/usr/bin/env python3

# Written and developed by Stian Kvålshagen.
# Reminder: Do not use this against websites not owned by you without permission.

import urllib.request
import argparse
import colorama
from colorama import Fore,Style

# Filters you can modify! If your target has a spesific way of coding, modify items bellow.
uWordlist = ["username","user"," u ","u=","u ="]
pWordlist = ["password","pass"," p ","p=","p ="]
filters = [" ","<scriptsrc=\"","<src=\"","src=\"","\"></script>"]
cList = ["//","<!--","-->","/*"]

parser = argparse.ArgumentParser()
parser.add_argument("-A","--all",help="Use all scan arguments.",action="store_true")
parser.add_argument("-C","--Comment",help="Print all comments",action="store_true")
parser.add_argument("-e","--explore",help="Explore mode. Will check every javascript file it can find. Run with other arguments to scan found files. \nNOTE:Be carefull! This will scan everything, make sure you stay inside your scope.",action="store_true")
parser.add_argument("-o","--output",help="File to store results",type=str)
parser.add_argument("-P","--Pass",help="Get mentions of passwords.",action="store_true")   
parser.add_argument("-q","--quiet",help="Do not print anything. Should be used with --output",action="store_true")
parser.add_argument("-S","--search",help="Search for a given variable. Example: -S testVar",type=str)
parser.add_argument("-u","--url",help="The url you wish to scan.",type=str)
parser.add_argument("-U","--User",help="Get mentions of usernames.",action="store_true")
parser.add_argument("-V","--Value",help="Look for values used in javascript.",action="store_true")
parser.add_argument("-w","--input",help="A wordlist with different urls to scan.",type=str)
args = parser.parse_args()

# Todo: Find a way to counter "1 line websites" and implement verbose mode. Switch newline with < ?
parser.add_argument("-v","--verbose",help="Print everything that happens.",action="store_true")


url = []
list = []
js = []
links = []
box = []

if args.output:
 outFile = []
if args.url:
 onlyUrl = args.url
 url.append(onlyUrl)
if args.search:
 search = args.search
if args.input:
 inputFile = args.input
if args.output:
 outName = args.output

# Activate all scan [-A]
if args.all:
 args.explore = True
 args.User = True
 args.Pass = True
 args.Comment = True
 args.Value = True

# Error messages
if not args.url and not args.input:
 print(Fore.RED + "You need to specify where to look! Use -h for help.")
 exit()
if args.User is not True and args.Pass is not True and args.explore is not True and not args.search and args.Comment is not True:
 print(Fore.RED + "Make sure to have an argument! Use -h for help.")
 exit()

# Open,read and split the lines from given url. [-u]
if args.url:
 list.append(onlyUrl)
 fp = urllib.request.urlopen(onlyUrl)
 mybytes = fp.read()
 mystr = mybytes.decode("utf8")
 fp.close()
 lines =  mystr.split("\n",)
 fl = []
 for x in lines:
  fl.append(x)
 box.append(fl)

# If using an input list [-w]
if args.input:
 fC = []
 file = open(inputFile)
 content = file.readlines()
 i = 0
 for c in content:
  fC.append(c.replace("\n",""))
 for c in fC:
  url.append(c)
  list.append(c)
  fp = urllib.request.urlopen(c)
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  lines =  mystr.split("\n",)
  fl = []
  for x in lines:
   fl.append(x)
  box.append(fl)
  i = i + 1

# Explore mode [-e]
if args.explore:
 i = 0
 found = False
 for u in url:
  counter = 0
  foundNr = []
  if args.quiet is not True:
   print(Fore.CYAN + "\nJavascripts found for " + u + ":" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "\nJavascripts found for " + u + ":" + Style.RESET_ALL)
  for text in box[i]:
   counter = counter + 1
   if ".js" in text:
    if counter not in foundNr:
     foundNr.append(counter)
     for x in filters:
      text = text.replace(x,"")
     js.append(text)
     if args.quiet is not True:
      print(str(counter) + ". " + text.replace(" ",""))
     if args.output:
      outFile.append(str(counter) + ". " + text.replace(" ",""))
     found = True
     links.append(u + text)
  i = i + 1
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
 if args.quiet is not True:
  print(Fore.CYAN + "\nFull list:" + Style.RESET_ALL)
 if args.output:
  outFile.append(Fore.CYAN + "\nFull list:" + Style.RESET_ALL)
 for x in links:
  if args.quiet is not True:
   print(x)
  if args.output:
   outFile.append(x)
  list.append(x)

# Start scanning items based on arguments
for item in list:
 if args.User or args.Pass or args.Value or args.search or args.Comment:
  if args.quiet is not True:
   print(Fore.GREEN + "\n\nScanning " + item + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.GREEN + "\n\nScanning " + item + Style.RESET_ALL)
  fp = urllib.request.urlopen(item)
  mybytes = fp.read()
  mystr = mybytes.decode("utf8")
  fp.close()
  lines =  mystr.split("\n",)
  fl = []
  for x in lines:
   fl.append(x)

# Find all Usernames [-U]
 counter = 0
 foundNr = []
 if args.User:
  found = False
  if args.quiet is not True:
   print(Fore.CYAN + "All Username mentions:" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "All Username mentions:" + Style.RESET_ALL)
  for text in fl:
   counter = counter + 1
   for wList in uWordlist:
    if wList in text:
     if counter not in foundNr:
      if args.quiet is not True:
       print(str(counter) + ". " + text.replace(" ",""))
      if args.output:
       outFile.append(str(counter) + ". " + text.replace(" ",""))
      foundNr.append(counter)
      found = True
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
   if args.output:
    outFile.append("Nothing found..")

# Find all Passwords [-P]
 if args.Pass:
  counter = 0
  foundNr = []
  found = False
  if args.quiet is not True:
   print(Fore.CYAN + "All Password  mentions:" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "All Password  mentions:" + Style.RESET_ALL)
  for text in fl:
   counter = counter + 1
   for pList in pWordlist:
    if pList in text:
     if counter not in foundNr:
      if args.quiet is not True:
       print(str(counter) + ". " + text.replace(" ",""))
      if args.output:
       outFile.append(str(counter) + ". " + text.replace(" ",""))
      foundNr.append(counter)
      found = True
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
   if args.output:
    outFile.append("Nothing found..")

# Find all values [-V]
 if args.Value:
  counter = 0
  foundNr = []
  found = False
  if args.quiet is not True:
   print(Fore.CYAN + "All Values:" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "All Values:" + Style.RESET_ALL)
  for text in fl:
   counter = counter + 1
   if "value" in text:
    if counter not in foundNr:
     if args.quiet is not True:
      print(str(counter) + ". " + text.replace(" ",""))
     if args.output:
      outFile.append(str(counter) + ". " + text.replace(" ",""))
     foundNr.append(counter)
     found = True
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
   if args.output:
    outFile.append("Nothing found..")

# Find specified variable [-S]
 if args.search:
  counter = 0
  foundNr = []
  found = False
  if args.quiet is not True:
   print(Fore.CYAN + "All " + search  + "  mentions:" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "All " + search  + "  mentions:" + Style.RESET_ALL)
  for text in fl:
   counter = counter + 1
   if search in text:
    if counter not in foundNr:
     if args.quiet is not True:
      print(str(counter) + ". " + text.replace(" ",""))
     if args.output:
      outFile.append(str(counter) + ". " + text.replace(" ",""))
     foundNr.append(counter)
     found = True
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
   if args.output:
    outFile.append("Nothing found..")

# Find all comments [-V]
 if args.Comment:
  counter = 0
  foundNr = []
  found = False
  longC = False
  if args.quiet is not True:
   print(Fore.CYAN + "All comments:" + Style.RESET_ALL)
  if args.output:
   outFile.append(Fore.CYAN + "All comments:" + Style.RESET_ALL)
  for text in fl:
   counter = counter + 1
   for c in cList:
    if "/*" in text:
     found = True
     longC = True
    if "*/" in text:
     if counter not in foundNr:
      foundNr.append(counter)
      if args.quiet is not True:
       print(str(counter) + ". " + text)
      if args.output:
       outFile.append(str(counter) + ". " + text)
      longC = False
    if longC:
     if counter not in foundNr:
      foundNr.append(counter)
      if args.quiet is not True:
       print(str(counter) + ". " + text)
      if args.output:
       outFile.append(str(counter) + ". " + text)
    if c in text and longC is not True:
     if counter not in foundNr:
      if args.quiet is not True:
       print(str(counter) + ". " + text)
      if args.output:
       outFile.append(str(counter) + ". " + text)
      foundNr.append(counter)
      found = True
  if not found:
   if args.quiet is not True:
    print("Nothing found..")
   if args.output:
    outFile.append("Nothing found..")

# Print results to file [-o]
if args.output:
 if args.quiet is not True:
  print(Fore.CYAN + "Creating file: " + outName + Style.RESET_ALL)
 with open(outName,"a") as f:
  for o in outFile:
   f.write("\n" + o)
 f.close
