## Username and Password Enumeration example

python3 upEnu.py -u http://10.0.0.x:xx/login/ -U -P
                                                                                                                                                           
Scanning http://10.0.0.x:xx/login/                                                                                                                         
All Username mentions:
<inputtype="text"id="user"value="Spacey"class="login-forms"><br>
varu="Username";
Password  mentions:
<pid="p-text"for="password">Password</label><br></p>
<inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
varp="Password";

## Explore mode example
python3 upEnu.py -u http://10.0.0.x:xx/ -e 

Javascripts found for http://10.0.0.x:xx/:                                                                                                                 
secret/variables.js
js/animation.js
secret/smiley.js

Full list:                                                                                                                                                    
http://10.0.0.x:xx/secret/variables.js
http://10.0.0.x:xx/js/animation.js
http://10.0.0.x:xx/secret/smiley.js

## Full scan
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -A

Javascripts found for http://10.0.0.x:xx/login/:                                                                                                           
../secret/variables.js
../js/credentials.js
../js/animation.js
../js/riWrAni.js

Full list:                                                                                                                                                    
http://10.0.0.x:xx/login/../secret/variables.js
http://10.0.0.x:xx/login/../js/credentials.js
http://10.0.0.x:xx/login/../js/animation.js
http://10.0.0.x:xx/login/../js/riWrAni.js

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/                                                                                                                         
All Username mentions:
<inputtype="text"id="user"value="Spacey"class="login-forms"><br>
varu="Username";
All Password  mentions:
<pid="p-text"for="password">Password</label><br></p>
<inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
varp="Password";
All Values:
<inputtype="text"id="user"value="Spacey"class="login-forms"><br>
<inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
<inputtype="submit"value="Login"id="submit-button">
All comments:
     <!-- Exploring variables is fun!-->

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../secret/variables.js                                                                                                   
All Username mentions:
varuserName=document.getElementById("user");
All Password mentions:
varpassWord=document.getElementById("pass");
All Values:
Nothing found..
All comments:
//Note! These variables should not be found..

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../js/credentials.js                                                                                                     
All Username mentions:
if(userName.value=="Luring"){
All Password  mentions:
if(passWord.value==sText[2]){
All Values:
if(userName.value=="Luring"){
if(passWord.value==sText[2]){
All comments:
Nothing found..

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../js/animation.js                                                                                                       
All Username mentions:
Nothing found..
All Password  mentions:
Nothing found..
All Values:
Nothing found..
All comments:
// Should I keep all this is one file? Probably not..

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../js/riWrAni.js                                                                                                         
All Username mentions:
Nothing found..
All Password  mentions:
Nothing found..
All Values:
Nothing found..
All comments:
/*
      This has been quite fun to work with.
      Hope it is usefull for someone else! :]
*/

## Search Mode
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -S sText

Javascripts found for http://10.0.0.x:xx/login/:
../secret/variables.js
../js/credentials.js
../js/animation.js
../js/riWrAni.js

Full list:
http://10.0.0.x:xx/login/../secret/variables.js
http://10.0.0.x:xx/login/../js/credentials.js
http://10.0.0.x:xx/login/../js/animation.js
http://10.0.0.x:xx/login/../js/riWrAni.js


Scanning http://10.0.0.x:xx/login/
All sText  mentions:
Nothing found..


Scanning http://10.0.0.x:xx/login/../secret/variables.js 
All sText  mentions:
varsText=["test","uffda","hehe","æsj"]


Scanning http://10.0.0.x:xx/login/../js/credentials.js
All sText  mentions:
if(passWord.value==sText[2]){


Scanning http://10.0.0.x:xx/login/../js/animation.js
All sText  mentions:
Nothing found..

Scanning http://10.0.0.x:xx/login/../js/riWrAni.js
All sText  mentions:
Nothing found..
