from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.template import Context
from email.message import EmailMessage
from email import message
from django.http import HttpResponseRedirect
from .models import EmailSending, EmailForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            wish = 'Thank You For Subscribing!'
            name = 'Sunrise Multispeciality Hospital Navi-Mumbai'
            address = 'Shiv Kalpataru Arcade, Plot 1, Sector - 17, Kamothe, Navi Mumbai'
            contact = '022-27431050, 983320483, 8976031050, 8928689509'
            website = 'www.sunrisemultispecialityhospital.in'
            # content = 'You Have Got One Subscribe form ' + email
            data = wish + '\n\n' + name + '\n\n' + 'Address :' + '\n' + address + '\n' + contact + '\n' + website
            send_mail(
                'Sunrise Multispecialtiy Hospital, Kamothe',
                data,
                settings.EMAIL_HOST_USER,
                [email]
            )

            # from_email = settings.EMAIL_HOST_USER
            # text_content = 'This is an Important Email'
            # html_content = """
            #         <!DOCTYPE html>
            #             {% load static %}
            #             <html lang="en">
            #                 <head>
            #                     <meta charset="UTF-8">
            #                 </head>
            #                 <body>
            #                     <h1>Sunrise Multispeciality Hospital Mumbai.</h1>
            #                     <h5>This is Test Mail....!!</h5>
            #                     <h5>This is Test Mail....!!</h5>
            #                     <h5>This is Test Mail....!!</h5>
            #                     <img src="{% static 'image/Logo/Logo.png' %}" alt="not found">
            #                 </body>
            #             </html>
            # """
            # msg = EmailMultiAlternatives(name, text_content, from_email, [email])
            # msg.attach_alternative(html_content, 'text/html')
            # msg.send()

            # from_email = settings.EMAIL_HOST_USER
            # plain_text = get_template('EmailSending/mail.txt')
            # htmly = get_template('EmailSending/testmail.html')
            # text_content = plain_text.render()
            # html_content = htmly.render()
            # msg = EmailMultiAlternatives(name, text_content, from_email, [email])
            # msg.attach_alternative(html_content, 'text/html')
            # msg.send()

            # from_email = settings.EMAIL_HOST_USER
            # text_body = render_to_string("EmailSending/mail.txt")
            # html_body = render_to_string("EmailSending/testmail.html")
            # msg = EmailMultiAlternatives(subject=name, from_email=from_email,
            #                              to=[email], body=text_body)
            # msg.attach_alternative(html_body, "text/html")
            # msg.send()

            # html_message = render_to_string('EmailSending/testmail.html')
            # message = EmailMessage(html_message, settings.EMAIL_HOST_USER)
            # message.get_content_subtype = 'html'
            # message.send()

            # send_mail(
            #     'Sunrise Hospital, Navi-Mumbai',
            #     data,
            #     settings.EMAIL_HOST_USER,
            #     ['business@yodiso.com', 'amolpomaji2020@gmail.com']
            # )
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = EmailForm()
    return render(request, 'Hospital/home.html', {'form': form})


# def home(request):
#     if request.method == 'POST':
#         email = request.POST.get('sendemail')
#         content = '<h1>You Have Got One Subscribe form this ' + email + ' Address. <br> <h1>Thank You For Subscribing!</h1>'
#         print(email, content)
#         send_mail(
#             # Subject
#             '....!',
#             # Content On the Sending Email
#             content,
#             # From Email Address
#             settings.EMAIL_HOST_USER,
#             # Receiver Email
#             [email]
#         )
#         data = EmailForm()
#         data.email = email
#         data.content = content
#         if data.is_valid():
#             data.save(commit=True)
#         # EmailSending(email=email, content=content)
#         # EmailSending.save()
#         return HttpResponseRedirect('/home')
#     else:
#         return render(request, 'Hospital/home.html')


def contact(request):
    return render(request, 'Hospital/contact.html')


def about(request):
    return render(request, 'Hospital/about.html')


def doctors(request):
    return render(request, 'Hospital/doctors.html')


def tpa_insurances(request):
    return render(request, 'Hospital/tpa_insurances.html')


def general_medicine(request):
    return render(request, 'Speciality/general_medicine.html')


def pediatrician_neonatologist(request):
    return render(request, 'Speciality/pediatrician_neonatologist.html')


def obstetrician_gynecologist(request):
    return render(request, 'Speciality/obstetrician_gynecologist.html')


def general_laparoscopic_surgery(request):
    return render(request, 'Speciality/general_laparoscopic_surgery.html')


def orthopedics(request):
    return render(request, 'Speciality/orthopedics.html')


def dermatology_skin_vd(request):
    return render(request, 'Speciality/dermatology_skin_vd.html')


def ent(request):
    return render(request, 'Speciality/ent.html')


def psychiatry(request):
    return render(request, 'Speciality/psychiatry.html')


def psychology_and_counselling(request):
    return render(request, 'Speciality/psychology_and_counselling.html')


def physiotherapist(request):
    return render(request, 'Speciality/physiotherapist.html')


def dietitian_and_nutritionist(request):
    return render(request, 'Speciality/dietitian_nutritionist.html')


# ---------------------------------------------- Super Speciality Section ----------------------------------------------

def neurologist(request):
    return render(request, 'Super_Speciality/neurologist.html')


def nephrology(request):
    return render(request, 'Super_Speciality/nephrology.html')


def haematology_oncology(request):
    return render(request, 'Super_Speciality/haematology_oncology.html')


def urology(request):
    return render(request, 'Super_Speciality/urology.html')


def pediatric_surgery(request):
    return render(request, 'Super_Speciality/pediatric_surgery.html')


def plastic_surgeon(request):
    return render(request, 'Super_Speciality/plastic_surgeon.html')


def dietitian_and_nutrition(request):
    return render(request, 'Super_Speciality/dietitian_and_nutrition.html')


def testmail(request):
    return render(request, 'EmailSending/testmail.html')
# ---------------------------------------------- End Super Speciality Section ------------------------------------------
