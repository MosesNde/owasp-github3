 import json
 import os
 import requests
 from flask import Flask, request
 
 
     token = os.environ.get('TOKEN')
 
     if request.args['token']!= token:
        exit(1)
 
     event = request.get_json()
 
     if not event:
        return "event empty"
 
     message = Message(url, event)
     if (event['eventKey'] == 'pr:opened' or event['eventKey'] == 'pr:merged' or event['eventKey'] == 'pr:declined'):
         comment = message.pr_approved(event)
         r = message.send_message(comment)
 
    return r
 
 
 if __name__ == "__main__":