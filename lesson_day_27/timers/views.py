from rest_framework import generics
from .models import Timer
from .serializers import TimerSerializers



# Create your views here.
class TimerListCreate(generics.ListCreateAPIView):
    queryset=Timer.objects.all()
    serializer_class=TimerSerializers

class TimerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Timer.objects.all()
    serializer_class=TimerSerializers
