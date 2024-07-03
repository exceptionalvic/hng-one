from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status, mixins
from rest_framework.decorators import api_view, renderer_classes, APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import *
from django.utils import timezone
from django.views.generic import TemplateView

from .utils import get_visitor_data


class WelcomeView(APIView):

    def get(self, request):
        visitor_data = get_visitor_data(request)
        print(visitor_data)
        visitor_name = request.query_params.get("visitor_name", None)
        city_temperature = ""
        if visitor_name is not None:
            response_data ={
                "client_ip": f"{visitor_data['ip']}",
                "location": f"{visitor_data['city']}",
                "greeting": f"Hello, {visitor_name}!, the temperature is {visitor_data['temperature']} degrees Celcius in {visitor_data['city']}"
            }
            print(response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail':'Visitor name missing'}, status=status.HTTP_400_BAD_REQUEST)



