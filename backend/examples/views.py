import random


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NumberSerializer


@api_view(['GET'])
def number_view(request):
    number = random.randint(0, 100)
    serializer = NumberSerializer({'value': number})

    return Response(serializer.data)
