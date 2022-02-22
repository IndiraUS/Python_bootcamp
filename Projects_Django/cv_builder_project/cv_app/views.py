
from django.http import HttpResponse

from django.shortcuts import redirect, render

from .models import resume

from django.template.loader import get_template

from xhtml2pdf import pisa

# Create your views here.


def index(request): 
    return render(request,'index.html')


def create_cv(request):    
    if request.method == 'POST':
        cv_type = request.POST['cvtemplates']
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['Phone']
        c_objective = request.POST['CareerObjective']
        skills = request.POST['Skills']
        experience = request.POST['Experience']
        education = request.POST['Education']
        address = request.POST['Address']
        hobbies = request.POST['Hobbies']

        obj = resume(cv_template = cv_type,name = name,email = email,phone = phone,career_objective = c_objective,skills = skills,experience = experience,education = education,address = address,hobbies = hobbies)
        obj.save()
        
        #return render(request,'cvForm.html')  
        return redirect('/create_cv/')       
    else:
         return render(request,'cvForm.html')  



def contact_developer(request):
    return render(request,'contact.html')

def update_cv(request):    
    if request.method == "GET":
        data = resume.objects.get(id=id)
        context = {'resumes':data}
        return render(request, 'cv_db.html',context)
    else:
        resume_id = request.POST["id"]
        resume.objects.filter(id=id).update(id=resume_id)
        return redirect("cv_db.html")
    #view_cv_database



def delete_cv(request, id):    
    if request.method == 'GET':
        resume.objects.filter(id = id).delete()
        resumes = resume.objects.all()
        context = {
                'resumes': resumes
                }
        return render(request,'cv_db.html',context)
    else:
        resumes = resume.objects.all()
        context = {
                'resumes': resumes
        }
        return render(request,'cv_db.html',context)


def view_cv_database(request):
    resumes = resume.objects.all()
    context = {
                'resumes': resumes
    }
    return render(request,'cv_db.html',context)


def render_context_to_cv(request,id):
    if request.method == 'POST':
        resumes = resume.objects.all()

        context = {
                  'resumes': resumes
         }
        return render(request,'CVTemplates/srt-resume.html',context)

    else: 
        data = resume.objects.get(id=id)
        context = {
                  'resumes': data
         }
        return render(request,'CVTemplates/srt-resume.html',context)

def download_pdf(request,id):
    data = resume.objects.get(id=id)

    context = {
                  'resumes': data
              }

    template_path =  'CVTemplates/srt-resume.html'

    #pdf_file_name = data.name + "_" + data.cv_template
    pdf_file_name = data.name + "_CV"

    response = HttpResponse(content_type='application/pdf')

    #response['Content-Disposition'] = 'attachment; filename="cv_1.pdf"'
    response['Content-Disposition'] = 'attachment; filename="' + pdf_file_name + '".pdf"'


    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # if error then
    if pisa_status.err:
       return HttpResponse('Error in pdf file generation : ',pisa_status.error)
    return response
         
          

def print_radio(request):
    '''if 'choice' in request.POST:
        return HttpResponse("Radio button is on")'''
    if request.method == 'POST':
        id = request.POST.get("choice")
        return HttpResponse(id)    
    else:
        return render(request,'sample.html')    

                

    