from rest_framework import views, status
from rest_framework.response import Response

from .models import Medicine
from .serializers import MedicineGetSerializer


class MedicineAPIView(views.APIView):

    serializer_class = MedicineGetSerializer

    def get(self, request):
        queryset = Medicine.objects.all()
        medicines = MedicineGetSerializer(queryset, many=True)
        return Response(medicines.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        medicine = serializer.save()
        resp = self.serializer_class(medicine)
        return Response(resp.data, status=status.HTTP_201_CREATED)


class MedicineDetailAPIView(views.APIView):

    serializer_class = MedicineGetSerializer

    def get(self, request, c_pk):
        queryset = Medicine.objects.get(pk=c_pk)
        companies = MedicineGetSerializer(queryset)
        return Response(companies.data)

    def patch(self, request, c_pk):
        medicine = Medicine.objects.filter(pk=c_pk).first()
        serializer = MedicineGetSerializer(medicine, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_206_PARTIAL_CONTENT)

    def delete(self, request, c_pk):
        medicine = Medicine.objects.filter(pk=c_pk)
        medicine.delete()
        return Response({"msg": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)