from django.shortcuts import render,HttpResponse,reverse,redirect
from .forms import Autorform, Libroform
from.models import Escritor,Libro
from django.core.paginator import Paginator
# Create your views here.
#path('autores/',views.autores,name='autores' )
def autores(request):
    #SELECT * FROM escritor
    autores=Escritor.objects.all()
    paginator=Paginator(autores,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    #page1=p.page(1)
    #print(page1.next_page_number())
    form=Autorform()
    return render(request,'autores.html',{"form":form,"page_obj":page_object})
#path('autoresForm/',views.autoresForm,name='autoresForm')



def autoresForm(request):
    form=Autorform()
    if request.method=='POST':
        form=Autorform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuarios:autores'))
    return render(request,"autorForm.html",{"form":form})
#path('autorEdit/<int:id>',views.autorEdit,name='autorEdit')



def autorEdit(request,id):
    autor=Escritor.objects.get(id=id)
    autores=Escritor.objects.all()
    form=Autorform(instance=autor)
    if(request.method=="POST"):
        form=Autorform(data=request.POST,instance=autor)
        form.save()
        return redirect(reverse('usuarios:autores'))
    return render(request,'autorEdit.html',{"form":form,"autores":autores,"id":id})



#path('autorDelete/<int:id>',views.autorDelete,name='autorDelete')
def autorDelete(request,id):
    autor=Escritor.objects.get(id=id)
    autor.delete()
    return redirect(reverse('usuarios:autores'))


#path('libros/',views.libros,name='libros')

def libros(request):
    libros=Libro.objects.all()
    paginator=Paginator(libros,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    form=Libroform()
    return render(request,'libros.html',{"page_obj":page_object,"form":form})

#path('librosForm/',views.libtosForm,name='librosForm')

def libroForm(request):
    form=Libroform()
    if request.method=='POST':
        form=Libroform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuarios:libros'))
    return render(request,"librosForm.html",{"form":form})

#path('librosEdit/<int:id>',views.librosEdit,name='librosEdit')
def libroEdit(request,id):
        if request.method=='POST':
            libro=Libro.objects.get(id=id)
            form=Libroform(instance=libro,data=request.POST)
            form.save()
            return redirect(reverse('usuarios:libros'))

        libros=Libro.objects.all()
        paginator=Paginator(libros,2)
        page_number=request.GET.get('page')
        page_object=paginator.get_page(page_number)
        libro=Libro.objects.get(id=id)
        form=Libroform(instance=libro)
        return render(request,"libroEdit.html",{"page_obj":page_object,"form":form,"id":id})
#path('librosDelete/<int:id>',views.librosDelete,name='librosDelete')
def libroDelete(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect(reverse('usuarios:libros'))