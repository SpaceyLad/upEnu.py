# Username and Password Enumeration example

python3 upEnu.py -u http://10.0.0.x:xx/login/ -U -P
                                                                                                                                                           
Scanning http://10.0.0.x:xx/login/                                                                                                                         
All Username mentions:
15. <inputtype="text"id="user"value="Spacey"class="login-forms"><br>
37. varu="Username";
All Password  mentions:
16. <pid="p-text"for="password">Password</label><br></p>
17. <inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
38. varp="Password";

# Explore mode example
python3 upEnu.py -u http://10.0.0.x:xx/ -e 

Javascripts found for http://10.0.0.x:xx/:                                                                                                                 
18. secret/variables.js
19. js/animation.js
20. secret/smiley.js

Full list:                                                                                                                                                    
http://10.0.0.x:xx/secret/variables.js
http://10.0.0.x:xx/js/animation.js
http://10.0.0.x:xx/secret/smiley.js

# Full scan
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -A

Javascripts found for http://10.0.0.x:xx/login/:                                                                                                           
31. ../secret/variables.js
32. ../js/credentials.js
33. ../js/animation.js
34. ../js/riWrAni.js

Full list:                                                                                                                                                    
http://10.0.0.x:xx/login/../secret/variables.js
http://10.0.0.x:xx/login/../js/credentials.js
http://10.0.0.x:xx/login/../js/animation.js
http://10.0.0.x:xx/login/../js/riWrAni.js

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/                                                                                                                         
All Username mentions:
15. <inputtype="text"id="user"value="Spacey"class="login-forms"><br>
37. varu="Username";
All Password  mentions:
16. <pid="p-text"for="password">Password</label><br></p>
17. <inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
38. varp="Password";
All Values:
15. <inputtype="text"id="user"value="Spacey"class="login-forms"><br>
17. <inputtype="password"id="pass"value="passord123"class="login-forms"><br><br>
18. <inputtype="submit"value="Login"id="submit-button">
All comments:
35.     <!-- Exploring variables is fun!-->

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../secret/variables.js                                                                                                   
All Username mentions:
2. varuserName=document.getElementById("user");
All Password mentions:
3. varpassWord=document.getElementById("pass");
All Values:
Nothing found..
All comments:
1. //Note! These variables should not be found..

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../js/credentials.js                                                                                                     
All Username mentions:
2. if(userName.value=="Luring"){
All Password  mentions:
3. if(passWord.value==sText[2]){
All Values:
2. if(userName.value=="Luring"){
3. if(passWord.value==sText[2]){
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
29. // Should I keep all this is one file? Probably not..

                                                                                                                                                              
Scanning http://10.0.0.x:xx/login/../js/riWrAni.js                                                                                                         
All Username mentions:
Nothing found..
All Password  mentions:
Nothing found..
All Values:
Nothing found..
All comments:
18. /*
19.       This has been quite fun to work with.
20.       Hope it is usefull for someone else! :]
21. */

# Search Mode
python3 upEnu.py -u http://10.0.0.x:xx/login/ -e -S sText

Javascripts found for http://10.0.0.x:xx/login/:
31. ../secret/variables.js
32. ../js/credentials.js
33. ../js/animation.js
34. ../js/riWrAni.js

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
13. varsText=["test","uffda","hehe","æsj"]


Scanning http://10.0.0.x:xx/login/../js/credentials.js
All sText  mentions:
3. if(passWord.value==sText[2]){


Scanning http://10.0.0.x:xx/login/../js/animation.js
All sText  mentions:
Nothing found..

Scanning http://10.0.0.x:xx/login/../js/riWrAni.js
All sText  mentions:
Nothing found..
