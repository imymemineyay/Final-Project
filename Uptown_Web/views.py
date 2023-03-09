from django.shortcuts import render, redirect
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        return render(request, './index.html')

    def post(self, request):
        return render(request, './index.html')

##############################################################

# 대쉬보드, 생산, 품질 페이지는 로그인 해야 보여지게 만들어야 함
# def form_valid(self,form):
#         current_user = self.request.user
#         if current_user.is_authenticated:
#             form.instance.author = current_user
#             return super(PostCreate,self).form_valid(form)
#         else:
#             return redirect('users/login.html')

class Dashboard(APIView):
    def get(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './dashboard.html')
        else:
            return redirect('users:login')

    def post(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './dashboard.html')
        else:
            return redirect('users:login')
    

class Production(APIView):
    def get(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './production.html')
        else:
            return redirect('users:login')

    def post(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './production.html')
        else:
            return redirect('users:login')
        
        

class Quality(APIView):
    def get(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './quality.html')
        else:
            return redirect('users:login')

    def post(self, request):
        current_user = self.request.user
        if current_user.is_authenticated:
            return render(request, './quality.html')
        else:
            return redirect('users:login')


##############################################################

class Error404(APIView):
    def get(self, request):
        return render(request, './404.html')

    def post(self, request):
        return render(request, './404.html')


class Business(APIView):
    def get(self, request):
        return render(request, './business.html')

    def post(self, request):
        return render(request, './business.html')
    

class Cooperative(APIView):
    def get(self, request):
        return render(request, './cooperative.html')

    def post(self, request):
        return render(request, './cooperative.html')


class Crew(APIView):
    def get(self, request):
        return render(request, './crew.html')

    def post(self, request):
        return render(request, './crew.html')


class Forgot_password(APIView):
    def get(self, request):
        return render(request, './forgot_password.html')

    def post(self, request):
        return render(request, './forgot_password.html')
    

class Inquiry(APIView):
    def get(self, request):
        return render(request, './inquiry.html')

    def post(self, request):
        return render(request, './inquiry.html')


class Location(APIView):
    def get(self, request):
        return render(request, './location.html')

    def post(self, request):
        return render(request, './location.html')


class Login(APIView):
    def get(self, request):
        return render(request, './login.html')

    def post(self, request):
        return render(request, './login.html')
    

class My_account(APIView):
    def get(self, request):
        return render(request, './my_account.html')

    def post(self, request):
        return render(request, './my_account.html')


class My_page(APIView):
    def get(self, request):
        return render(request, './my_page.html')

    def post(self, request):
        return render(request, '.my_page.html')


class Okr(APIView):
    def get(self, request):
        return render(request, './okr.html')

    def post(self, request):
        return render(request, './okr.html')
    

class Overview(APIView):
    def get(self, request):
        return render(request, './overview.html')

    def post(self, request):
        return render(request, './overview.html')



class Register(APIView):
    def get(self, request):
        return render(request, './register.html')

    def post(self, request):
        return render(request, './register.html')