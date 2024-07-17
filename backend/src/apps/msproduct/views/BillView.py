from msproduct.models import Bill
from msproduct.serializers import BillSerializer
from rest_framework import generics


class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillSingle(generics.RetrieveAPIView):
    serializer_class = BillSerializer

    def get_object(self):
        obj = Bill.objects.get(user=self.kwargs["user"], total=0)
        return obj
