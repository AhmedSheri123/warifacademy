from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.fields import citys, StateFields, YesNoFields, NationalityFields, GenderFields, HowHearFields, DisabilityTypeFields, DisabilityAmputationTypeFields, DisabilityMovementFields, DisabilityMindFields, DisabilityHearFields, DisabilityEaysFields, DisabilityAloneFields, DisabilityOthersFields, CertTypeFields, JobTypeFields, JobPropertiesFields, LanguageLevelFields, LearningDomainFields
from accounts.models import UserProfile, EmployeeProfile, CompanyCreateJobModel, EmployeeJobRequest, StrNumCodeGen, EmailVerificationCodeModel, ViewersCounterByIPADDR
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.db.models import Q
from accounts.email_sender import SendEmail
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def SendEmailVerification(userprofile):
    secret = StrNumCodeGen(100)
    EmailVerification = EmailVerificationCodeModel(userprofile=userprofile, secret=secret, is_active=True, creation_date=datetime.datetime.now())
    EmailVerification.save()

    html = f"""
    <html>
    <body>
        <p>مرحبا,<br>
        يرجى الضغط على زر التاكيد لتاكيد حسابك
        <br>
        <a href="http://127.0.0.1:8000/accounts/EmailVerificationCode/{secret}">تاكيد الحساب</a> 
        فرصة سعيدة
        </p>
    </body>
    </html>
    """
    # try:
    send_mail(subject='قادرون', message=html, from_email=settings.EMAIL_HOST_USER, recipient_list=[userprofile.user.email])
    # SendEmail(html=html, receiver_email=userprofile.user.email, Subject='قادرون', is_html=True)
    return True
    # except:return False


def index(request):
    jobs = CompanyCreateJobModel.objects.filter(Q(post_state='3') | Q(post_state='5'))

    REMOTE_ADDR = request.META.get('REMOTE_ADDR')
    ViewersCounter = ViewersCounterByIPADDR.objects.filter(ip_addr=REMOTE_ADDR)
    if not ViewersCounter:
        ViewersCounterCreate = ViewersCounter.create(ip_addr=REMOTE_ADDR, creation_date=datetime.datetime.now())
        ViewersCounterCreate.save()
        
    return render(request, 'pages/index.html', {'jobs':jobs.order_by('-id')})

def AvailableJobs(request):
    jobs = CompanyCreateJobModel.objects.filter(Q(post_state='3') | Q(post_state='5'))
    search = request.GET.get('search')
    if search:jobs = jobs.filter(job_desc__contains=search)

    return render(request, 'pages/jobs/AvailableJobs.html', {'jobs':jobs.order_by('-id')})


def ViewJob(request, id):
    job = CompanyCreateJobModel.objects.get(id=id)
    if request.method == 'POST':
        apply_job = request.POST.get('apply_job')
        user = request.user
        if user.is_authenticated:
            if user.userprofile.is_employee:
                employee_job_request = EmployeeJobRequest.objects.filter()
                if apply_job == '1':
                    if employee_job_request.filter(employee=request.user).exists():
                        messages.error(request, 'انت بلفعل طلبت هذه الوظيفة من قبل')
                        return redirect('EmployeeMain')
                    else:
                        if job.post_state == '3':
                            employee_job_request = employee_job_request.create(employee=user, company_job=job, post_state='1', creation_date=datetime.datetime.now())
                            employee_job_request.save()
                            messages.success(request, 'تم طلب الوظيفة بنجاح')
                        else:
                            messages.error(request, 'حدث مشكلة اثناء التحقق')
                            return redirect('EmployeeMain')

            else:messages.error(request, 'يرجى التسجيل بحساب المستخدم العادي ليمكنك تفعيل هذا الاجراء')

        else:return redirect('employeePortal')#messages.error(request, 'يرجى انشاء حساب او تسجيل الدخول اذا كان لديك حساب من قبل')
                    
    
    company = job.userprofile.companyprofile
    
    
    return render(request, 'pages/jobs/ViewJob.html', {'company':company, 'job':job})


def employeePortal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        state = request.POST.get('state')
        age = request.POST.get('age')
        is_disability = request.POST.get('is_disability')
        city = request.POST.get('city')
        district = request.POST.get('district')
        nationality = request.POST.get('nationality')
        gender = request.POST.get('gender')
        how_hear = request.POST.get('how_hear')
        how_hear_other = request.POST.get('how_hear_other')
        have_car = request.POST.get('have_car')
        disability_type = request.POST.get('disability_type')
        disability_movement = request.POST.get('disability_movement')
        disability_amputation_type = request.POST.get('disability_amputation_type')
        disability_idntify_amputation = request.POST.get('disability_idntify_amputation')
        disability_mind = request.POST.get('disability_mind')
        disability_Disturbances = request.POST.get('disability_Disturbances')
        disability_hear = request.POST.get('disability_hear')
        disability_eays = request.POST.get('disability_eays')
        disability_body = request.POST.get('disability_body')
        disability_alone = request.POST.get('disability_alone')
        disability_learn = request.POST.get('disability_learn')
        disability_atrabat = request.POST.get('disability_atrabat')
        disability_speak = request.POST.get('disability_speak')
        disability_others = request.POST.get('disability_others')
        disability_others_identy = request.POST.get('disability_others_identy')
        environment = request.POST.get('environment')
        cert_type = request.POST.get('cert_type')
        learning_domain = request.POST.get('learning_domain')
        major = request.POST.get('major')
        job_type = request.POST.get('job_type')
        job_properties = request.POST.get('job_properties')
        have_experience = request.POST.get('have_experience')
        have_experience_years = request.POST.get('have_experience_years')
        have_experience_work = request.POST.get('have_experience_work')
        have_experience_last_work = request.POST.get('have_experience_last_work')
        last_salary = request.POST.get('last_salary')
        baisc_experience_english = request.POST.get('baisc_experience_english')
        baisc_experience_arabic = request.POST.get('baisc_experience_arabic')
        baisc_experience_computer = request.POST.get('baisc_experience_computer')
        district_cert = request.FILES.get('district_cert')
        cv = request.FILES.get('cv')
        username = StrNumCodeGen(8)
        password = request.POST.get('password')



        employee_profile = EmployeeProfile.objects.create()
        employee_profile.name = name
        employee_profile.phone = phone
        employee_profile.state = state
        employee_profile.age = age
        employee_profile.is_disability = is_disability
        employee_profile.employee_city = city
        employee_profile.district = district
        employee_profile.nationality = nationality
        employee_profile.gender = gender
        employee_profile.how_hear = how_hear
        employee_profile.how_hear_other = how_hear_other
        employee_profile.have_car = have_car
        employee_profile.disability_type = disability_type
        employee_profile.disability_movement = disability_movement
        employee_profile.disability_amputation_type = disability_amputation_type
        employee_profile.disability_idntify_amputation = disability_idntify_amputation
        employee_profile.disability_mind = disability_mind
        employee_profile.disability_Disturbances = disability_Disturbances
        employee_profile.disability_hear = disability_hear
        employee_profile.disability_eays = disability_eays
        employee_profile.disability_body = disability_body
        employee_profile.disability_alone = disability_alone
        employee_profile.disability_learn = disability_learn
        employee_profile.disability_atrabat = disability_atrabat
        employee_profile.disability_speak = disability_speak
        employee_profile.disability_others = disability_others
        employee_profile.disability_others_identy = disability_others_identy
        employee_profile.employee_environment = environment
        employee_profile.cert_type = cert_type
        employee_profile.learning_domain = learning_domain
        employee_profile.major = major
        employee_profile.job_type = job_type
        employee_profile.job_properties = job_properties
        employee_profile.have_experience = have_experience
        employee_profile.have_experience_years = have_experience_years
        employee_profile.have_experience_work = have_experience_work
        employee_profile.have_experience_last_work = have_experience_last_work
        employee_profile.last_salary = last_salary
        employee_profile.baisc_experience_english = baisc_experience_english
        employee_profile.baisc_experience_arabic = baisc_experience_arabic
        employee_profile.baisc_experience_computer = baisc_experience_computer
        employee_profile.district_cert = district_cert
        employee_profile.cv = cv
        employee_profile.employee_password = password
        employee_profile.post_state = '1'
        employee_profile.creation_date = datetime.datetime.now()
        employee_profile.save()


        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        userprofile = UserProfile.objects.create(user=user, is_employee=True, creation_date=datetime.datetime.now(), employeeprofile=employee_profile)
        userprofile.save()



        Verification_result = SendEmailVerification(userprofile)
        if Verification_result:
            messages.success(request, 'تم ارسال رسالة تاكيد عبر البريد الالكتروني الخاصة بك')
        else:
            messages.error(request, 'حدث خطاء اثناء ارسال رسالة تاكيد عبر البريد الالكتروني')

        return redirect('SignIn')
    return render(request, 'pages/reports/employee.html', {'citys':citys, 'StateFields':StateFields, 'YesNoFields':YesNoFields, 'NationalityFields':NationalityFields, 'GenderFields':GenderFields, 'HowHearFields':HowHearFields, 'DisabilityTypeFields':DisabilityTypeFields, 'DisabilityAmputationTypeFields':DisabilityAmputationTypeFields, 'DisabilityMovementFields':DisabilityMovementFields, 'DisabilityMindFields':DisabilityMindFields, 'DisabilityHearFields':DisabilityHearFields, 'DisabilityEaysFields':DisabilityEaysFields, 'DisabilityAloneFields':DisabilityAloneFields, 'DisabilityOthersFields':DisabilityOthersFields, 'CertTypeFields':CertTypeFields, 'JobTypeFields':JobTypeFields, 'JobPropertiesFields':JobPropertiesFields, 'LanguageLevelFields':LanguageLevelFields, 'LearningDomainFields':LearningDomainFields})




def PrivacyPolicy(request):

    return render(request, 'pages/PrivacyPolicy.html')


def TermsConditions(request):

    return render(request, 'pages/TermsConditions.html')
