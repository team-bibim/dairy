from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Diary
from .serializers import DiarySerializer


# Create your views here.
#일기장 목록 API
class DiaryListAPIView(APIView):
    #Read
    def get(self, request):
        serializer = DiarySerializer(Diary.objects.all(), many=True)
        return Response(serializer.data)

    #Create
    def post(self, request):
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#일기장 내용 API
class DiaryDetailAPIView(APIView):
    def get_object(self, pk):
        #pk에 해당하는 Diary 객체 get
        return get_object_or_404(Diary, pk=pk)

    def get(self, request, pk):
        diary = self.get_object(pk)
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    def put(self, request, pk):
        diary = self.get_object(pk)
        serializer = DiarySerializer(diary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        diary = self.get_object(pk)
        diary.delete()
        return Response(status=204)