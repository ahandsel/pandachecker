"""
Program will ping the list of website to see if they are online.

Will give an error message if the website is down.

import URLs from weblist.txt => addressList
# => each line should become its own element via splitlines()

check status of websites in the addressList
# if error => Text my number via Twilio
# if no error => Do nothing
"""

import subprocess
import send_sms

with open('weblist.txt', 'r+') as theList:
    addressList = theList.read().splitlines()

print(addressList) #test if data transfered over correctly

# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None)

BadLinks = ""

for anURL in addressList:
    test = subprocess.run(["ping", "-c", "1", anURL])
    if test.returncode != 0:
        send_sms.error_msg(anURL)
        BadLinks += anURL
        BadLinks += ", "

print()
print("* * * * * * * * * ")
print('Finished Checking URLs')
if len(BadLinks) > 0:
    print("The following links are down: " + BadLinks)
print("* * * * * * * * * * * * * * * * * * * * * * * * ")

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
Example Results:
- Since Netflix.com & DeAnza.edu prevents pings, they will be considered "down" & a text msg should be sent
- All other links should go through with no issues and no text msgs.

e.g. for basanese.com:
PING basanese.com (45.32.236.82): 56 data bytes
64 bytes from 45.32.236.82: icmp_seq=0 ttl=51 time=343.322 ms

--- basanese.com ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 343.322/343.322/343.322/0.000 ms

>> test = CompletedProcess(args=['ping', '-c', '1', 'basanese.com'], returncode=0)

e.g. Netflix.com
PING netflix.com (52.42.235.31): 56 data bytes

--- netflix.com ping statistics ---
1 packets transmitted, 0 packets received, 100.0% packet loss

>> CompletedProcess(args=['ping', '-c', '1', 'netflix.com'], returncode=2)

"""
"""
Old Code:

for anURL in addressList:
    subprocess.run(["ping", "-c", "1", anURL], check=True)

try:
    for anURL in addressList:
        subprocess.run(["ping", "-c", "1", anURL], check=True)
except subprocess.CalledProcessError:
    send_sms.error_msg()
"""