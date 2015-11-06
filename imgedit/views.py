from django.http import HttpResponse
from trips.models import Picture
from PIL import Image
from PIL import ImageEnhance

import tempfile

def rotate_image_right(request):

    image = None
    if request.method == 'GET':
        image = request.GET['image']
    
    if image:  
        filePath = '/home/jakemilessilva/mysite/media/'
        file = filePath + image
        im = Image.open(file)
        rotated = im.rotate(-90)
        rotated.save(file, "JPEG")

    return HttpResponse(image)
    
def change_image_color(request):

    image = None
    if request.method == 'GET':
        image = request.GET['image']
    
    if image:  
        filePath = '/home/jakemilessilva/mysite/media/'
        file = filePath + image
        im = Image.open(file)
        enhancer = ImageEnhance.Contrast(im).enhance(1.5)
        enhancer.save(file, "JPEG")
        
    return HttpResponse(file)