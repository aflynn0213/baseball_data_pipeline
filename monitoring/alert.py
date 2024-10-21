import smtplib
import logging
import requests

def send_email_alert(subject, message, recipients):
    """Send an email alert."""
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail('your_email@example.com', recipients, email_message)
        server.quit()
        print("Email alert sent!")
    except Exception as e:
        logging.error(f"Failed to send email alert: {str(e)}")

def send_slack_alert(webhook_url, message):
    """Send an alert to a Slack channel."""
    try:
        payload = {'text': message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Slack alert sent!")
        else:
            logging.error(f"Failed to send Slack alert: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to send Slack alert: {str(e)}")

def send_alert(subject, message, alert_type='email', recipients=None, webhook_url=None):
    """Generic function to send different types of alerts."""
    if alert_type == 'email' and recipients:
        send_email_alert(subject, message, recipients)
    elif alert_type == 'slack' and webhook_url:
        send_slack_alert(webhook_url, message)
    else:
        logging.error("Invalid alert type or missing parameters.")

# Example usage:
if __name__ == "__main__":
    send_alert(subject="Model Accuracy Dropped", 
               message="The accuracy has dropped below 90%.", 
               alert_type="email", 
               recipients=["admin@example.com"])
