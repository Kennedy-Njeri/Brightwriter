# Brightwriter


Django app for assisting in essay writing by creating orders and checking out payment using Paypal


Brightwriter App enables clients to upload their files get invoices for their order.Also allows them to checkout using paypal API.
Here Are The Steps;
1. Register for An Account
2. Create An Order
3. Once payment is made your order is processed
4. Once your order is processed you are notified, hence your doc is ready for download

N/B once a person registers or creates an order he or she gets a confirmation email

For Devs
1. Clone the project or download the project directly
2. Activate your environment using   source ./venv/bin/activate 
3. Run pip install -r requirements.txt to get all package dependencies
4. Run pip freeze to see installed dependencies;
amqp==2.4.2
billiard==3.6.0.0
celery==4.3.0
certifi==2019.3.9
chardet==3.0.4
Django==2.1.7
django-crispy-forms==1.7.2
django-paypal==1.0.0
django-smtp-ssl==1.0
idna==2.8
kombu==4.5.0
pytz==2018.9
requests==2.21.0

5. Make sure you have a message broker like Redis, RabbitMq for purpose of Celery
6.Run python manage.py runserver
7. Then python manage.py migrate to migrate all the tables 
8. Make sure you have a paypal sandbox account;
in settings.py add;

PAYPAL_RECEIVER_EMAIL = 'xxxxx-facilitator@gmail.com'
PAYPAL_TEST = True

details from your paypal sandbox account

9. Using Ngrok run ngrok http 8000

10. Go to settings.py in allowed hosts add the following e.g
dfd38b9a.ngrok.io from your ngrok terminal
11. Go to Chrome paste that ngrok address to run your app
12. Go to your admin in Orders You will see the paid status change once you pay

Thats All You need....You can extend the App  

