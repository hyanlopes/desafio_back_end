from django.http import HttpResponse
from django.shortcuts import render
from project.utils import read_cnab
from rest_framework.views import Request
from store.models import Store

from .forms import UploadFileForm
from .serializers import ManagementSerializer


def upload_file(request: Request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]
        for i in file.readlines():
            line = read_cnab(i.decode("utf-8"))
            store, _ = Store.objects.get_or_create(name=line["store_name"])
            line["store_id"] = store.id
            serializer = ManagementSerializer(data=line)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            store.Management.add(serializer.instance)
        return HttpResponse(f"Seu arquivo '{str(file)}' foi armazenado com sucesso")
    else:

        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


# Create your views here.
