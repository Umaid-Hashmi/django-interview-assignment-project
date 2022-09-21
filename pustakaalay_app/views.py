from urllib import request
from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .custom_adapter import MyOwnAdapter 

from .models import User
from .models import Book

from .forms import LoginForm

from .serializers import UserSerializer
from .serializers import BookSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def try_request():
    try:
            user_objs = User.objects.all()
            serializer = UserSerializer(user_objs, many=True)
            if serializer.data["is_librarian"] == True:
                return Response({'status': 200, 'payload': serializer.data})
    except Exception as e:
            return Response({"status": 403, "message" : "Access Forbidden"})



class UserDetailAPI(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [IsAuthenticated]
    MyOwnAdapter.json_response(request=request)

    def get(self, request):
        try_request()

    def delete(self, request):
        try_request()
    
    def post(self, request):
       try_request()
    
    def put(self, request):
        try_request()




class BookDetailAPI(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [IsAuthenticated]
    MyOwnAdapter.json_response(request=request)

    def get(self, request):
        try_request()
        
    def delete(self, request):
        try_request()
    
    def post(self, request):
       try_request()
    
    def put(self, request):
        try_request()


def index(request):
    if request.COOKIES.get('pustakaalay_user') :
        template = loader.get_template('pustakaalay_app/home.html')
        context = { 'username' : request.COOKIES.get('pustakaalay_user'), 'books' : Book.objects.filter(borrower__username=request.COOKIES.get('pustakaalay_user'))  }
        response = HttpResponse(template.render(context, request))
        return response
    elif request.method == 'POST' :
        login_form = LoginForm(request.POST)
        if login_form.is_valid() :
            try :
                user = User.objects.get(username=login_form.cleaned_data['username'])
                if user.password == login_form.cleaned_data['password'] :
                    if user.is_librarian :
                        template = loader.get_template('pustakaalay_app/librarian.html')
                    else :
                        template = loader.get_template('pustakaalay_app/home.html')
                    context = { 'username' : user.username, 'books' : Book.objects.filter(borrower__username=user.username) }
                    response = HttpResponse(template.render(context, request))
                    response.set_cookie('pustakaalay_user', user.username)
                    return response
                else :
                    error = 'incorrect password'
                    login_form = LoginForm(request.POST)
                    template = loader.get_template('pustakaalay_app/index.html')
                    context = { 'login_form' : login_form, 'error' : error }
                    return HttpResponse(template.render(context, request))
            except User.DoesNotExist :
                error = 'username "' + login_form.cleaned_data['username'] + '" is not registered with pustakaalay'
                login_form = LoginForm()
                template = loader.get_template('pustakaalay_app/index.html')
                context = { 'login_form' : login_form, 'error' : error }
                return HttpResponse(template.render(context, request))
    else :
        login_form = LoginForm()
        template = loader.get_template('pustakaalay_app/index.html')
        context = { 'login_form' : login_form }
        return HttpResponse(template.render(context, request))

def logout(request):
    template = loader.get_template('pustakaalay_app/logout.html')
    context = {}
    response = HttpResponse(template.render(context, request))
    response.delete_cookie('pustakaalay_user')
    return response

def delete_account(request):
    if request.method == 'POST' :
        context = { 'confirm_delete' : True }
    else :
        context = { 'books' : Book.objects.filter(borrower__username=request.COOKIES.get('pustakaalay_user')), 'user' : User.objects.get(username=request.COOKIES.get('pustakaalay_user')) }
    template = loader.get_template('pustakaalay_app/delete_account.html')
    response = HttpResponse(template.render(context, request))
    return response

def book_manager(request):
    context = { 'books' : Book.objects.all(), 'user' : User.objects.get(username=request.COOKIES.get('pustakaalay_user')) }
    template = loader.get_template('pustakaalay_app/book_manager.html')
    response = HttpResponse(template.render(context, request))
    return response



class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
