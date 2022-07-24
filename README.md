# Automation - Web Scraper

One of the most popular uses of Python is automation.

## API

This is a scraper that scrapes through a document and returns emails and phone numbers. We assume that the phone numbers have the area code 206 when one is not provided. 

## Navigation

Given a document potential-contacts, find and collect all email addresses and phone numbers.
Phone numbers may be in various formats.
(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
phone numbers should be stored in xxx-yyy-zzzz format.
Once emails and phone numbers are found they should be stored in two separate documents emails.txt and numbers.txt 
The information should be sorted in ascending order.
Duplicate entries are not allowed.


## Resources

See the code for [The File Scraper](scraper.py) by clicking on the highlighted words!

Phone Numbers Regex: https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number

Writing to a file with newLines: https://stackoverflow.com/questions/7138686/how-to-write-a-list-to-a-file-with-newlines-in-python3

Worked with Sergii Otryshko, Pedro Perez and Marni Hager
