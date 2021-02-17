from django.urls import path
from Hospital import views

app_name = 'Hospital'
urlpatterns = [
    path('', views.home, name=''),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('tpa_insurances/', views.tpa_insurances, name='tpa_insurances'),

    # Speciality
    path('general_medicine/', views.general_medicine, name='general_medicine'),
    path('pediatrician_neonatologist/', views.pediatrician_neonatologist, name='pediatrician_neonatologist'),
    path('obstetrician_gynecologist/', views.obstetrician_gynecologist, name='obstetrician_gynecologist'),
    path('general_laparoscopic_surgery/', views.general_laparoscopic_surgery, name='general_laparoscopic_surgery'),
    path('orthopedics/', views.orthopedics, name='orthopedics'),
    path('dermatology_skin_vd/', views.dermatology_skin_vd, name='dermatology_skin_vd'),
    path('ent/', views.ent, name='ent'),
    path('psychiatry/', views.psychiatry, name='psychiatry'),
    path('psychology_and_counselling/', views.psychology_and_counselling, name='psychology_and_counselling'),
    path('physiotherapist/', views.physiotherapist, name='physiotherapist'),
    path('dietitian_nutritionist/', views.dietitian_and_nutritionist, name='dietitian_nutritionist'),

    # Super Speciality
    path('neurologist/', views.neurologist, name='neurologist'),
    path('nephrology/', views.nephrology, name='nephrology'),
    path('haematology_oncology/', views.haematology_oncology, name='haematology_oncology'),
    path('urology/', views.urology, name='urology'),
    path('pediatric_surgery/', views.pediatric_surgery, name='pediatric_surgery'),
    path('plastic_surgeon/', views.plastic_surgeon, name='plastic_surgeon'),
    path('dietitian_and_nutrition/', views.dietitian_and_nutrition, name='dietitian_and_nutrition'),

    path('testmail/', views.testmail, name='testmail'),
]
