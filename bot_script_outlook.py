import os
import random
import win32com.client as win32
import logging
import pandas as pd
from email_templates import email_template

#This block is a configuration for the logging information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#This block initiates all of our variables 
email_receiver = ''
recipient_name = ''

#this command allows for us to read from the excel sheet that has
#our email list & names
try:
    df = pd.read_excel('email_list.xlsx')
except Exception as e:
    logging.error(f"Error reading Excel file: {e}")

#This for loop runs for the length of the excel sheet
#for how many rows there are with values
for index, row in df.iterrows():

    #this sets the pre-initiated email & name variables
    #equal to whatever the values are within the excel sheet
    email_receiver = row['Email']
    recipient_name = row["Name"]

    def main():
        #This is what is going to be included in our email (Subject & Body)
        #This sets a variable to the object email_template()
        #so we are able to use 'subject' and 'body' from the 
        #case function
       email_data = email_template(recipient_name)
       return email_data

    #loop repeats 
    if __name__ == "__main__":
        email_data = main()

    #This finally sends the email to the user, it tries and if there is an error, that is logged
    try:
        olApp = win32.Dispatch('Outlook.Application')
        olNS = olApp.GetNameSpace('MAPI')

        mailItem = olApp.CreateItem(0)
        mailItem.Subject = email_data['subject']
        mailItem.BodyFormat = 1
        mailItem.Body = email_data['body']
        mailItem.To = email_receiver


        #This appends a different image to the email depending on the format
        if email_data['case'] == 1:

            mailItem.Attachments.Add(os.path.join(os.getcwd(), 'images/series_9.png'))

        elif email_data['case'] == 2:

            mailItem.Attachments.Add(os.path.join(os.getcwd(), 'images/_Japan.jpg'))

        mailItem.Display()

        mailItem.Save()
        mailItem.Send()

    except Exception as e:

        logging.error(f"Error sending email to {recipient_name}: {e}")

    #loop repeats 




