from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projecthomepage, name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name='exceptionpagelogic'),
    path('add_task/',views.add_task, name='add_task'),
    path('delete_task/',views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserRegisterLogic/',views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserRegisterpagecall/',views.UserRegisterpagecall, name='UserRegisterpagecall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall, name='UserLoginPageCall'),
    path('add_student/',views.add_student, name='add_student'),
    path('student_list/',views.student_list, name='student_list'),
    path('datetimepagecall/',views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic, name='datetimepagelogic'),
    path('randompagecall/',views.randompagecall, name='randompagecall'),
    path('randomlogic/',views.randomlogic, name='randomlogic'),
    path('calculatorpagecall/',views.calculatorpagecall, name='calculatorpagecall'),
    path('calculatorlogic/',views.calculatorlogic, name='calculatorlogic'),

]