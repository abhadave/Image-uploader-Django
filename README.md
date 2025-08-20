# Image-uploader-Django

The project allows users to upload images through a simple web interface.Uploaded images are stored in the server’s MEDIA_ROOT directory.Django’s MEDIA_URL setting provides the public path to access these files.The uploaded images can be displayed in templates using the {{ object.image.url }} tag.Proper configuration in settings.py ensures storage and retrieval of media files.This makes the app useful for galleries, profile pictures, and file-sharing features.
