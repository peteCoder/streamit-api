from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({"details": "Welcome to Streamit API"}, safe=False)




