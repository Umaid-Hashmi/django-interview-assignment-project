from rest_framework.response import Response
from .adapter import DefaultAccountAdapter
from django.http import HttpRequest, HttpResponse, JsonResponse


class MyOwnAdapter(DefaultAccountAdapter):
    def json_response(request):
        # Craft your own response.
        if request=="GET":
            return Response({"status": 200})
        elif request== "POST":
            return Response({"status": 200})
        elif request== "PUT":
            return Response({"status": 200})
        else :
            if request== "DELETE":
                return Response({"status": 200})
