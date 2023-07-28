# Pricing-App
Make sure you have the following software installed on your machine:
Python (3.7 or higher)
Django (3.2.20 or higher)

Step-1: Install the required dependencies:
pip install -r requirements.txt

Step-2: Create a superuser (for accessing the Django admin interface):
python manage.py createsuperuser

Step-3: Usage
Access to the Pricing App is working at my local system.
On the homepage, enter the distance traveled (in km), time traveled (in hours), and select the day of the week from the dropdown.
Click the "Calculate Price" button to calculate the total price based on the pricing configuration. (You can view the code, currently, I am facing some issues on the server side so the button is not working properly. I will fix it soon.)

Step-4: API Endpoint: The Pricing App also provides an API endpoint for calculating the price based on the input parameters. 
distance_traveled (float): The distance traveled in kilometers.
time_traveled (float): The time traveled in hours.
day_of_week (string): The day of the week (e.g., "Mon", "Tue", etc.).
The API will respond with a JSON object containing the calculated price.

Step-5: Contributing:
Contributions to the Pricing App are welcome! If you find any issues or want to add new features, please feel free to open an issue or submit a pull request.
