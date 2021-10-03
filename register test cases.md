##########################################################
Checking functionality of 'REGISTER' button when credentials are not entered:

a. textbox for firstname is empty
b. textbox for lastname is empty
c. textbox for username is empty
d. textbox for email is empty
e. textbox for password is empty
f. textbox for confirm password is empty


navigate to registration page
click register
type in firstname: T'im-mie
click register
type in lastname: T'eu-cer
click register
type in username: timitense
click register
type in email: saysorry@gmail.com
click register
type in password: osmanthus!wine
click register

Prompted to enter firstname

Prompted to enter lastname

Prompted to enter username

Prompted to enter email

Prompted to enter password

Prompted to enter confirm password	




##########################################################
Checking functionality of 'REGISTER' button for invalid inputs:

a. input for firstname is not 2-15 characters long
b. input for firstname includes special characters except for "-" and "'"
c. input for lastname is not 2-15 characters long
d. input for lastname includes special characters except for "-" and "'"
e. input for username is not 6-20 characters long
f. input for username includes special characters
g. input for email does not follow the general format for email adrresses
h. input for password and confirm password does not match


AAAAAAAA BBBBBBBB
navigate to registration page
type in firstname: a
type in lastname: T'eu-cer
type in username: timitense
type in email: saysorry@gmail.com
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in firstname: wh@td4
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in firstname: abcdefghijklmnopqrst
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


CCCCCCCCC DDDDDDD
type in firstname: T'im-mie
type in lastname: a
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in lastname: 15794709~
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in lastname: abcdefghijklmnopqrst
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


EEEEEEEEEE FFFFFFFF
type in lastname: T'eu-cer
type in username: snow
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in username: @...aDoMin
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register
type in username: longestusernameintheworld
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


GGGGGGGGG
type in username: timitense
type in email: gmail .com
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


HHHHHHHHH
type in email: saysorry@gmail.com
type in password: osmanthus!wine
type in confirm password: osmanthus!not
click register




##########################################################
Checking functionality of 'REGISTER' button for valid inputs:

a. input for firstname and lastname is 2-15 characters long
b. input for username is 6-20 characters long
c. input for email is follows the general format
d. input for password and confirm password matches


navigate to registration page
type in firstname: T'im-mie
type in lastname: T'eu-cer
type in username: timitense
type in email: saysorry@gmail.com
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


##########################################################
Checking functionality of 'REGISTER' button when unique credentials/ identifiers are already registered:

a. input for username is already registered
b. input for email is already registered

navigate to registration page
type in firstname: Jon
type in lastname: Timmie
type in username: timitense
type in email: new@gmail.com
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register

type in username: jontimy
type in email: saysorry@gmail.com
type in password: osmanthus!wine
type in confirm password: osmanthus!wine
click register


