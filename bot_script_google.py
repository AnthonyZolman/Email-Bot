import os 
from email_templates import email_template
from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.image import MIMEImage
import logging
import ssl
import smtplib
import certifi
import pandas as pd

#This block is to move the email_sender & email_password out of the main function and improve security
#Refer to .env file for info
load_dotenv()
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")

#This block is a configuration for the logging information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#This block initiates all of our variables 
email_receiver = ''
recipient_name = ''
sender_name = ''

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


    #This is what is going to be included in our email (Subject & Body)
    def main():
        #This sets a variable to the object email_template()
        #so we are able to use 'subject' and 'body' from the 
        #case function
       email_data = email_template(recipient_name)
       
       return email_data

    #loop repeats 
    if __name__ == "__main__":
        email_data = main()
            

    #This defines the email as an object for the smtp program
    em = EmailMessage()
    em['From'] = f"{email_data['sender']} <{email_sender}>"
    em['To'] = email_receiver
    em['Subject'] = email_data['subject']
    em.set_content(email_data['body'])

    def attach_image(em, filename):
        with open(filename, 'rb') as img_file:
            img = MIMEImage(img_file.read())
        em.add_attachment(img, filename=filename)

    #This appends a different image to the email depending on the format
    if email_data['case'] == 1:

        attach_image(em, 'images/series_9.png')

    elif email_data['case'] == 2:

        attach_image(em, 'images/_Japan.jpg')
   


    #this creates protected & encrypted connection SSL -> email server
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    #This finally sends the email to the user, it tries and if there is an error, that is logged
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_context) as smtp:

            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

            logging.info(f"Email sent to {recipient_name}")

    except Exception as e:

        logging.error(f"Error sending email to {recipient_name}: {e}")

#end main functionx