#!/usr/bin/env python3

import os
import subprocess
import re

def ignore_emails(ignore_file):
    # Open the file and read its contents into a string
    with open(ignore_file, 'r') as f:
        text = f.read()

    # Use the re module to search for email addresses that match the desired pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    ignore_emails = re.findall(email_pattern, text)

    return ignore_emails

def find_personal_emails(ignore_emails, repo_path):

    # Use git command to get the list of all files in the repository
    files = subprocess.check_output(['git', 'ls-files'], cwd=repo_path).decode().strip().split('\n')

    # Initialize a set to store the found emails
    found_emails = set()

    # Iterate through each file and search for emails
    for file in files:
        with open(os.path.join(repo_path, file), 'r') as f:
            # Read the file content
            content = f.read()

        # Search for emails in the file content
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
        for email in re.findall(email_pattern, content):
            # Check if the email is not in the ignore list
            if email not in ignore_emails:
                found_emails.add(email)

    return found_emails


#ignore_file = '/home/sk893122/ex-invid/exercise-nv/.ignore_emails'
#repo_path = '/home/sk893122/ex-invid/exercise-nv/'
ignore_file = '/home/sk893122/ex-invid/exercise-nv/exercise-nv/.ignore_emails'
repo_path = '/home/sk893122/ex-invid/exercise-nv/exercise-nv'

ignore_emails = ignore_emails(ignore_file)
found_emails = find_personal_emails(ignore_emails, repo_path)

print ("ignore_emails: ", ignore_emails)
print ("--------------------------------")
print ("found_emails: ", found_emails)

