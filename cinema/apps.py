from django.apps import AppConfig
import os
import uuid
from django.utils.text import slugify


class CinemaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cinema"


def movie_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/movies/", filename)
