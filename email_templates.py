import random
import logging

#This is what is going to be included in our email (subject & body)
def email_template(recipient_name):
        random_number = random.randint(1,3)
        logging.debug(random_number)
        match random_number:
            case 1:
                return {
                    'case': 1,
                    'sender': 'Apple Inc.',
                    'subject': 'Congratulations, You Won!!!',
                    'body': f"""
                    Dear {recipient_name},
                    We are thrilled to inform you that you have been selected as the winner of a brand new Apple Watch Series 9! This exclusive reward is our way of showing appreciation for your continued support.

                    To claim your prize, please click on the link below:

                    Claim Your Apple Watch Series 9: 

                    We hope you enjoy this exciting new gadget and all the amazing features it offers. Should you have any questions or need further assistance, please do not hesitate to contact us.

                    Congratulations once again, and thank you for being a valued member of our community!
                    
                    """ 
                    }
            case 2:
               return {
                    'case': 2,
                    'sender': 'Human Resources',
                    'subject': 'Congratulations, You Won!!!',
                    'body': f"""
                    Dear {recipient_name},

                    I am thrilled to inform you that you have been selected as the winner of our all-expenses-paid trip to Japan! This is a well-deserved recognition of your hard work and dedication.

                    Your trip will include visits to some of Japan’s most iconic landmarks, including the breathtaking Mount Fuji. We hope this experience will be both enjoyable and enriching for you.

                    To claim your prize, please click on the following link:

                    Please find attached a special image to commemorate this exciting news.

                    Congratulations once again, and we look forward to hearing all about your adventures in Japan!
                    
                    """
                    }
            case 3:
                return {
                    'case': 3,
                    'sender': 'IT Security',
                    'subject': 'URGENT, Immediate Action Required',
                    'body': f"""
                    Dear {recipient_name},

                    We have detected a login attempt from an unrecognized location. If this was not you, to ensure the security of your account, please verify your email address immediately by clicking the link below:
                    

                    Thank you for your prompt attention to this matter.

                    Best regards,
                    Security Team
                    
                    """
                    }
        
        