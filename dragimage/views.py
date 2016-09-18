from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
from django.core.urlresolvers import reverse
from datetime import date

from forms import UploadFileForm, PhotoUploadForm, CustomerInfoForm, FourthTryForm

def upload_picture(request, uid=None):
    """
    Photo upload/dropzone handler
    :param request:
    :pram uid: Optional picture UID when re-uploading a file.
    : return:
    """

    form = PhotoUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        pic = request.FILES['file']
        # Process whatever to do with the file, resize, thumbnail etc.
        # Get an instance of picture model (defined below)
        # picture = ...
        picture.file = pic
        picture.save()
        return HttpResponse('Image upload successful.')
    return HttpResponseBadRequest("Image upload form not valid.")

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('./tempaltes/dragimagesuccess.html')) #('dragimage:home'))
# http://stackoverflow.com/questions/30077990/trying-to-use-django-and-dropzone
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('firstdrag.html', data, context_instance=RequestContext(request))

def index(request):
    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)

        if (form.is_valid()):
            instance = form.save(commit=False)
            for key, value in request.FILES.iteritems():
                a_path = '/a/b'
                save_uploadfile_to_disk(a_path, file)
                setattr(instance, key, a_path) # path made up, have to clear that
            form.save() # form saved for real
            return HttpResponse('Image upload successful.')
        else:
            print form.errors # for debugging
    else:
        form = CustomerInfoForm()
        context = {'form' : form}
        return render(request, '../templates/thirddrag.html', context)

def save_uploadfile_to_disk(full_path, file):
    with open(full_path, 'w+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def fourthTry(request):
    if request.method == 'POST':
        form = FourthTryForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            form.save()
            return HttpResponseRedirect('/productlist/') # have to add a list of image
    else:
        form = FourthTryForm()
    return render(request, 'fourthdrag.html', {'form': form})