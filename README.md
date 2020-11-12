# course_selector
A python script to help user automatically select courses in McGill. 

Preparation: 
1. A Linux Server
2. Download PhantomJS browser/driver
3. pip3 install selenium

What is does?
The program automatically login to your mcgill account and try to select the course you specified.
If the waitlist is available, you will be immediately added to the waitlist. 
If not, the program will report the error and quit.

Using it with crontab, it can run every 15 minutes to check if the waitlist is available. 
