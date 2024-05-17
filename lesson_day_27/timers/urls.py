from django.urls import path
from .views import TimerListCreate , TimerRetrieveUpdateDestroy

urlpatterns=[
    path("timers/",TimerListCreate.as_view(), name="timer-list"),
    path("timers/<int:pk>", TimerRetrieveUpdateDestroy.as_view(), name="timer-detail"),
]