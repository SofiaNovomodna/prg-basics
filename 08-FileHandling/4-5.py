import re

def email_sender(email):
    pattern = 'Return-Path: <(.+@example.com)>'
    with open(email) as file:
        context = file.read()
    sender = re.findall(pattern,context)
    print ('email sender', sender[0])

email_sender('email.txt')


def email_recipient(email):
    pattern = 'for <(.+@example.com)>'
    with open(email) as file:
        context = file.read()
    recipient = re.findall(pattern,context)
    print ('email recipient', recipient[0])

email_recipient('email.txt')


def email_subject(email):
    pattern = 'Subject: (.+)'
    with open(email) as file:
        context = file.read()
    Subject = re.findall(pattern,context)
    print ('email Subject', Subject[0])

email_subject('email.txt')


def email_body(email):
    #pattern = 'Content-Transfer-Encoding: 7bit(.+)'
    with open(email) as file:
        context = file.read()
    context = context.splitlines()
    print_ = False
    for line in context:
        if print_ == True:
            print (line)
        if line == '':
            print_ = True
    #body = re.findall(pattern,context)
    #print ('email body', body[0])

email_body('email.txt')