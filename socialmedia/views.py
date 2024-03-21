from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView,FormView
from django.contrib.auth.models import User


from socialmedia.models import Userprofile,Posts
from socialmedia.forms import RegistrationForm,LoginForm,PostForm,ProfileForm


# <-------------------------->

class USerregistrationView(View):
    def get(self,request,*args, **kwargs):
        loginform=LoginForm()
        regform=RegistrationForm()
        return render(request,"signin.html",{"loginform":loginform,"regform":regform})
    
    def post(self,request,*args, **kwargs):
        loginForm=LoginForm(request.POST)
        regform=RegistrationForm(request.POST)
        
        if 'signup' in request.POST:
            if regform.is_valid():
                regform.save()
                return render (request,"signin.html")
            else:
                return render (request,"signin.html",{"regform":regform})
        elif 'signin' in request.POST:
            if loginForm.is_valid():
                user_name=loginForm.cleaned_data.get('username')
                pswd=loginForm.cleaned_data.get('password')
                print(user_name,pswd)
                user_obj=authenticate(request,username=user_name,password=pswd)
                print(user_obj)
                if user_obj:
                    print(user_obj)
                    print("valid credintial")
                    login(request,user_obj)
                
                    return redirect("homepage")
                else:
                    print("Login Faild")
                    return render (request,"signin.html",{'loginform':loginForm})
            else:
                return render(request,'signin.html',{"loginform":loginForm})
    

# class SignUpView(CreateView):
#     template_name="signin.html"
#     form_class = RegistrationForm
#     success_url=reverse_lazy("signup")
    

# class SiginView(FormView):
#     def get(self,request,*args, **kwargs):
#         form=LoginForm()
#         return render(request,"signin.html",{"form":form})
#     def post(self,request,*args, **kwargs):
#         form=LoginForm(request.POST)
       
#         if form.is_valid():
#             user_name=form.cleaned_data.get('username')
#             pswd=form.cleaned_data.get('password')
#             print(user_name,pswd)
#             user_obj=authenticate(request,username=user_name,password=pswd)
#             print(user_obj)
#             if user_obj:
#                 print(user_obj)
#                 print("valid credintial")
#                 login(request,user_obj)
            
#                 return redirect("homepage")
#             else:
#                 print("login failed")
#                 return render(request,"signin.html",{"form":form})
#         else:

#             return render(request,'signin.html',{"form":form})
   
class SignoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("login")



class HomeIndexView(TemplateView):
    template_name="homepage.html"
    
class CreatePostView(View):
    def get(self,request,*args, **kwargs):
        form = PostForm()
        return render(request,"postadd.html")
    def post(self,request,*args, **kwargs):
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return render(request,"postadd.html",{"form":form})
        else:
            return render(request,"postadd.html",{"form":form})


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs=request.user.profile

        return render(request, "profile.html",{"pro":qs})
    
    
class ProfileUpdateView(UpdateView):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, "editprofile.html", {"form": form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        us_obj = Userprofile.objects.get(user=id)
        print(us_obj)
        form = ProfileForm(request.POST, instance=us_obj, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "editprofile.html",{"form":form})
        else:
            return render(request, "editprofile.html",{"form":form})
