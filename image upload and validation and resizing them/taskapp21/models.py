
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import os.path
 

class MyModel(models.Model):
    photo = models.ImageField(upload_to="media",null=True,blank=True)
    thumbnail = models.ImageField(upload_to="thumbnaill",null=True,blank=True)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(MyModel, self).save(*args, **kwargs)

    def make_thumbnail(self):

        image = Image.open(self.photo)
        image.thumbnail((300,300), Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.photo.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    #image resize function
    #def save(self,*args,**kwargs):
    #    imageTemporary=Image.open(self.image)
    #    outputIostream=BytesIO()
    #    imageTemporaryResized=imageTemporary.resize((300,300))
    #    imageTemporaryResized.save(outputIostream,format="PNG",quality=100)
    #    outputIostream.seek(0)
    #    #self.thumbnail=imageTemporaryResized
    #    self.thumbnail=InMemoryUploadedFile(outputIostream,"ImageField","%s.png" %self.image.name.split(',')[0])
    #    super(MyModel,self).save(*args,**kwargs)
    #    print("###############################################################################")

