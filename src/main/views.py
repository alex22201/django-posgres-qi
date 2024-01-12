from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer


def main(request):
    return render(
        request,
        'main.html',
    )


@api_view(['GET'])
def api_endpoint(request):
    cryptocurrency_name = request.GET.get('name', None)

    if cryptocurrency_name:
        cryptocurrency = Cryptocurrency.get_by_name(cryptocurrency_name)

        if cryptocurrency:
            serializer = CryptocurrencySerializer(cryptocurrency)
            return JsonResponse(serializer.data)
        else:
            response_data = {'error': f'Not found "{cryptocurrency_name}"'}
            return JsonResponse(response_data, status=404)
    else:
        cryptocurrencies = Cryptocurrency.objects.all()
        serializer = CryptocurrencySerializer(cryptocurrencies, many=True)
        return JsonResponse(serializer.data, safe=False)
