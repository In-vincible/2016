from django.shortcuts import render, HttpResponse
from .models import RegistrationInfo
from django.views.decorators.csrf import csrf_exempt
import json
from .send_mail import SendMail
import requests

events_data = {
    'code42day': ('CODE-4-2DAY', 'lehar.jain.ece13@iitbhu.ac.in'),
    'codedef': ('CODEDEF', 'apoorv.agarwal.ece13@itbhu.ac.in'),
    'continnum': ('CONTINNUM','harsh.raj.ece15@itbhu.ac.in'),
    'commnet': ('COMMNET', 'chetan.dashora.ece15@itbhu.ac.in'),
    'ctf': ('CTF', 'ayush.singh.ece13@iitbhu.ac.in'),
    'digisim': ('DIGISIM', 'vidit.agarwal.ece15@itbhu.ac.in'),
    'funckit': ('FUNCKIT', 'shivam.bansal.ece15@itbhu.ac.in'),
    'ichip': ('I-CHIP', 'mithilesh.krishan.ece15@itbhu.ac.in'),
    'krypto': ('SPYBITS', 'shubham.pandey.ece15@itbhu.ac.in'),
    'mosaic': ('MOSIAC', 'sahil.thakur.ece15@itbhu.ac.in'),
    'muse': ('MUSE', 'mithilesh.krishan.ece15@itbhu.ac.in'),
    'raspi': ('RASPI', 't.sairam.ece13@iitbhu.ac.in')
}

MAIL_BODY = '''
Dear %s

Thanks for registering for %s UDYAM'18.
Your Team Details are:
Team Name- %s 
Team Member- %s

Note: As this is an automatically generated email, please don't reply to this mail. Please feel free to contact us either through the mail or by phone in case of any further queries. The contact details are clearly mentioned on the website http://udyamfest.in/ 


Regards
Team UDYAM

‌'''
MAIL_SUBJECT = "UDYAM'18 %s"
@csrf_exempt
def index(request):
    if request.method == 'POST':
        error = 0
        e1='ad'
        try:
            #print (request.body)
            form_detail = json.loads(request.body.decode("utf-8"))
            team = RegistrationInfo()
            teamp=RegistrationInfo.objects.all().last()
            team.id=1
            if (teamp!=None):
                team.id=teamp.id+1
            team.event_name = form_detail[u'event']
            team.contact = json.dumps(form_detail[u'main_contact'])
            team.team_name = form_detail[u'team_name']
            team.team_details = form_detail[u'team_details']
            team.save()
            print(form_detail)
            contacts = [c.get('email') for c in form_detail[u'team_details'] if c]
            print(contacts)
            contacts = str(contacts).replace(',','\n').replace(']','').replace('[','').replace("'","")
            body = MAIL_BODY%(form_detail[u'main_contact']['name'], form_detail[u'event'], form_detail[u'team_name'], contacts)
            subject = MAIL_SUBJECT%form_detail[u'event']
            send_email(form_detail[u'main_contact']['email'], subject, body)
            send_email(events_data[form_detail[u'event']][1], subject, body)
            #mail = SendMail(form_detail)
            #mail.mail_coordinator()
            #mail.mail_representative()

        except Exception as e:
            e1=str(e)
            error = 1
            print(e1)
            #print(type(inst))
            #x,y=inst.args
            #print(x)
            #print(y)
            #print(34)
        return HttpResponse(json.dumps({'error': error, 'es':e1}), content_type='application/json')
    return render(request, 'home.html')


def static_page(request, page):
    page += '.html'
    return render(request, page)

def adminData(request):
    oll = RegistrationInfo.objects.all()
    return render(request, 'adminD.html', {'data': oll})

def send_email(recipient, subject, body):
	return requests.post("https://api.mailgun.net/v3/mg.udyamfest.in/messages",auth=("api", "key-716da2426e77cc5296dacd1e4768672d"),data={"from": "Udyam<no-reply@udyamfest.in>","to": recipient,"subject": subject,"text": body})