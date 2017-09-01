"""
Program will ping the list of website to see if they are online.

Will give an error message if the website is down.

import URLs from weblist.txt => addressListB
# => each line should become its own element via splitlines()

check status of websites in the addressListB
# if error => Text my number via Twilio
# if no error => Do nothing
"""
import subprocess
import send_sms

with open('weblist.txt', 'r+') as theList:
    addressListB = theList.read().splitlines()

print(addressListB) #test if data transfered over correctly

# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None)

try:
    for anAddress in addressListB:
        subprocess.run(["ping", "-c", "1", anAddress], check=True)
except subprocess.CalledProcessError:
    send_sms.error_msg()

print()
print()
print('Finished Checking URLs')
