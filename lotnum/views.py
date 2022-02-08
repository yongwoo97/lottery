from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import LotteryNumber
from .serializer import NumSerializer
from .NumberGetter import numget

@api_view(['GET', ])
@permission_classes((AllowAny,))
def GetNum(request, pk):
    if request.method == 'GET':
        try:
            last_number = LotteryNumber.objects.get(number=pk)
            serializer = NumSerializer(last_number)
            return Response(serializer.data)
        except:
            try:
                new_number = numget(pk)
                win_number = LotteryNumber(
                    date=new_number['date'],
                    number=new_number['number'],
                    n1=new_number['n1'],
                    n2=new_number['n2'],
                    n3=new_number['n3'],
                    n4=new_number['n4'],
                    n5=new_number['n5'],
                    n6=new_number['n6'],
                    n7=new_number['n7']
                )
                win_number.save()
                return Response(new_number)
            except:

                return Response({'message': 'does not exists'}, status=404)

