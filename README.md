# WebServerCheck

Checks to see version of webserver and if root is enabled

To run start services with

python View.py

Then open another terminal and run the client

python GetWebserverClient.py --ip "127.0.0.1"

Response should look like below

{u'webserver': u'nginx', u'webserver_version': u'nginx/1.6.2', u'Root_Enabled': False}
