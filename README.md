# pandachecker
Checks website if all is fine in the world...

The program will ping & check if the following websites are online:
  baseness.com
  netflix.com
  npr.org
  ucsc.edu
  google.com
  facebook.com
  netflix.com
  myeconlab.com
  instagram.com
  wikipedia.com
  deanza.edu
  nytimes.com

Will check the websites status one time.
If website is down, an error message would be sent as a text via Twilio API.

## Basic Instructions

### 1. download

    git clone https://github.com/ahandsel/pandachecker.git

### 2. deps

    cd pandachecker
    pip3 install -r requirements.txt
    
### 3. run

    python3 pandachecker.py
    
If you want to use this as a monitoring tool, `cron`
=======