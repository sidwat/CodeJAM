# CORONA SPECIAL

Mera naam Mukesh hai, Mai lockdown ke time sutta lene campus kebahar gaya tha...A patient Mukesh is infected by pneumonia and is not responding to conventional Treatments, doctorsfear that it is because of the novel corona-virus disease cause by the highly infectious new virus.  DrMohan from the IITK HC, belives that a dose of paracetamol with blood transfusion can save thelife of Mukesh.  You have to help him.  Dr.  Mohan has a warehouse full of paracetamol, as we allknow very well but he does not have blood.  and in the lockdown state he must source the bloodfrom within the campus.  Being a man who does not want to spam the entire mailing list, he wantsto only send a mail to those who can donate blood to Mukesh.


### Prerequisites

What things you need to install the software and how to install them

```
pip
Any text editor as per requirement
Python packages like:
    selenium
    beautifulsoup
    tkinter
    requests
    Chromedriver 

```

### Installing

A step by step series of examples that tell you how to get a development env running

For Chromedriver, install its zip file from the internet corresponding to the version of chrome you are using and the OS 
you are using (Windows, macOS, Linux, etc)

For packages like selenium, beautifulsoup, tkinter and requests open the terminal and type
'''
pip install <package name>

'''
repeat the process for all the packages and get the packages downloaded to your system


Example:
'''
pip install selenium

'''
### Process

First using the selenium, beautifulsoup and Chromedriver, we need to scrap the database of all the students and 
convert it into a csv file and save it. This is the database that we are going to search into in our program.
site scraped: https://search.pclub.in/

Then using the ktinker, an amazing GUI builder in python, we created a GUI with some labels at the top, entries as the user's 
email account and password and the bllod group he is searching for and the button which calls the action_of_button function 
to carryforward the further task.

The function Action_of_button calls two functions search and send email.

The function search opens the csv file and reads the csv and finds the email corresponding to the blood group input and returns the 
list of these emails.

The function send_mail takes the users email and password and the recipients' email list and mails them using the inbuilt module 
smtplib.


## Authors

* **Sidhartha Watsa** 

## Acknowledgments

* Google
* Wickipedia 
