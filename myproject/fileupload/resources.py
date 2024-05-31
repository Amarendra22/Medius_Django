from import_export import resources
from .models import uFile

class uFileResource(resources.ModelResource):
    class meta:
        model = uFile