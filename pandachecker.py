"""
Program will ping the list of website to see if they are online.
Will give an error message if the website is down.
"""
import subprocess

addressListA = ['baseness.com',
           'npr.org',
           'ucsc.edu',
           'google.com',
           'facebook.com',
           'myeconlab.com',
           'instagram.com',
           'wikipedia.com',
           'nytimes.com', 'netflix.com'
           ];

# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None)


for anAddress in addressListA:
    subprocess.run(["ping", "-c", "1", anAddress ], check=True)

subprocess.check_output(["echo", "Hello World!"])

print('please work')
