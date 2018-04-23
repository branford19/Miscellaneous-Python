# Import statements
import webbrowser
import sys

# Yes/No dictionary
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

# Question
choice = input("Do you want to search the internet? ").lower()
if choice in yes:
   webbrowser.open('www.google.com.au', new=0, autoraise=True)
elif choice in no:
   echo ("Run me when you would like to")
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
