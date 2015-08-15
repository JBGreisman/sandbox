########################################################################
# jack_utils.py
# Jack Greisman
########################################################################

import sys

#----------------------------------------------------------------------#
# Send a text message to a phone number
def send_text(message, number):
    import json, urllib2
    from urllib import quote_plus

    dd = "&".join(["-d", "number=%s" % number, "-d", "message=%s" % message])
    req = urllib2.urlopen("http://textbelt.com/text", dd)
    data = json.loads(req.read())

    if not data["success"]:
        print "Error sending text:", data["message"]
    return data["success"]

#----------------------------------------------------------------------#
# Test

def main():

    # Text number
    status = send_text(sys.argv[2], sys.argv[1])
    if (status):
        print "Success!"
    else:
        print "No!"

#----------------------------------------------------------------------#
if __name__ == "__main__":
    main()
