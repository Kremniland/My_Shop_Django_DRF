from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from django.contrib. messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, TemplateView

from basket.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .models import CustomUser, EmailVerification
from services.services import TitleMixin


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Подтверждение email'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        '''берем данные из гет запроса при переходе юзера по ссылке'''
        code = kwargs['code']
        user = CustomUser.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        # если список не пустой и время жизни ссылки не истекло то верифицируем юзера
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            # обязательно вернуть так или не отработает шаблон
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             # Проверяем есть ли пользователь с такими username password
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('prostoapp:index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Успешная регистрация!'
    title = 'Регистрация'


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Успешная регистрация!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


class UserProfileView(TitleMixin, UpdateView):
    '''login_required вешаем на url'''
    model = CustomUser
    form_class = UserProfileForm
    template_name ='users/profile.html'
    title = 'Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


# @login_required  # не авторизованного user перенаправит на LOGIN_URL
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(
#             instance=request.user,
#             data=request.POST,
#             files=request.FILES  # Для сохранения изображения
#             )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', context)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('prostoapp:index'))
