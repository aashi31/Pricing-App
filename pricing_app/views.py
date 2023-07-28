from django.http import JsonResponse
from django.shortcuts import render
from .models import PricingConfiguration

def calculate_price(request):
    if request.method == 'GET':
        distance_traveled = float(request.GET.get('distance_traveled', 0))
        time_traveled = float(request.GET.get('time_traveled', 0))

        # Calculate additional distance if distance traveled is greater than 3 km
        additional_distance = max(distance_traveled - 3, 0)

        # Get the pricing configuration based on the current day of the week
        day_of_week = request.GET.get('day_of_week', '')
        try:
            config = PricingConfiguration.objects.filter(days_of_week__contains=day_of_week, is_enabled=True).latest('id')
        except PricingConfiguration.DoesNotExist:
            return JsonResponse({'error': 'No active pricing configuration for the selected day.'}, status=404)

        base_price = config.distance_base_price
        additional_price = config.distance_additional_price
        time_multiplier = config.time_multiplier_factor
        waiting_charges = config.waiting_charges

        # Calculate the total price based on the pricing formula
        price = (base_price + (additional_distance * additional_price)) + (time_traveled * time_multiplier) + waiting_charges
        return JsonResponse({"price": price})
    else:
        # If the request method is not GET, return a Method Not Allowed response
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

def homepage(request):
    return render(request, 'pricing_app/homepage.html')
