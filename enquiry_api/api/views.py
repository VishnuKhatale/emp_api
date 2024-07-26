from rest_framework import viewsets
from .models import Enquiry
from .serializers import EnquirySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 


class enquiry_viewset(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, id=None):
        try:
            if id:
                enquire = Enquiry.objects.get(id=id)
                serializer = EnquirySerializer(enquire)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            
            enquires = Enquiry.objects.all()
            serializer = EnquirySerializer(enquires, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except Enquiry.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request):
       serializer = EnquirySerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
       else:
          return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request, id=None):
        try:
            enquire = Enquiry.objects.get(id=id)
            serializer = EnquirySerializer(enquire, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Enquiry.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        try:
            enquires = Enquiry.objects.filter(id=id)
            enquires.delete()
            return Response({"status": "success", "data": "Data Deleted"}, status=status.HTTP_200_OK)
        except Enquiry.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)