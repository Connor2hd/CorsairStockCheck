# This is a simple script I created to notify me when something new comes in
# sotck on the Corsair refurb page.

# Import requests
import requests

# Import time to allow for a delay between scrapes
import time

# Import smptlib for emails
import smtplib

# Use BeutifulSoup to parse what is downloaded
from bs4 import BeutifulSoup

while true
    # Set the url to the refurb Corsair page
    url = "http://www.corsair.com/en-us/certified-refurb"
    # Set the header to look like a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Download the page
    response = requests.get(url, headers=headers)
    # parse the downloaded page to get all text
    soup = BeutifulSoup(response.text, "lxml")

    # if the number of times the term "Flash Voyager" apears on the page is less than 1
    if str(soup).find("Flash Voyager") == -1:
        # wait an hour
        time.sleep(3600)
        #continue with the script
        continue

# else if the phrase "Flash Voyager" apears at all
else:
    # create and email
    msg = 'Stock Check: Flash Voyager is in stock'
    # set the from address
    fromaddr = 'Connor@Goliathhosting.com'
    # set the to address
    toaddrs = 'Pepsi-@live.ca'

    # setup the email server
    server = smtplib.smtp('smtp.gmail.com', 587)
    server.starttls()
    # add an account
    server.Login("Connor@GoliathHosting.com", "Password")

    # print the emails contents
    print('From: ' + fromaddr)
    print('To: ' + toaddrs)
    print('Message: ' + msg)

    # Send the emails
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()

    break
