from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("겟을 호출")
        return render(request, 'jista/main.html')

    def post(self, request):
        print("호스트 호출")
        return render(request, 'jista/main.html')