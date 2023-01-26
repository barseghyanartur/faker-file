from typing import List

from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from ninja import File, NinjaAPI, UploadedFile

from .models import Upload
from .schema import UploadIn, UploadOut

# from ninja_extra import (
#     ControllerBase,
#     NinjaExtraAPI,
#     api_controller,
#     http_delete,
#     http_generic,
#     http_get,
#     http_post,
#     pagination,
#     status,
# )
# from ninja_extra.controllers.response import Detail


#
__all__ = (
    "API",
    # "UploadsController",
    "create_upload",
    "delete_upload",
    "list_uploads",
    "retrieve_upload",
    "update_upload",
)

API = NinjaAPI(urls_namespace="api")
# API = NinjaExtraAPI(urls_namespace="api")
STORAGE = FileSystemStorage()


@API.post("/uploads")
def create_upload(request, payload: UploadIn, file: UploadedFile = File(...)):
    import IPython

    IPython.embed()
    from pprint import pprint

    pprint(request)
    pprint(payload)
    pprint(file)
    filename = STORAGE.save(file.name, file)
    payload_dict = payload.dict()
    payload_dict["file"] = filename
    upload = Upload.objects.create(**payload_dict)
    return {"id": upload.id}


@API.get("/uploads/{upload_id}", response=UploadOut)
def retrieve_upload(request, upload_id: int):
    upload = get_object_or_404(Upload, id=upload_id)
    return upload


@API.get("/uploads", response=List[UploadOut])
def list_uploads(request):
    qs = Upload.objects.all()
    return qs


@API.put("/uploads/{upload_id}")
def update_upload(request, upload_id: int, payload: UploadOut):
    upload = get_object_or_404(Upload, id=upload_id)
    for attr, value in payload.dict().items():
        setattr(upload, attr, value)
    upload.save()
    return {"success": True}


@API.delete("/uploads/{upload_id}")
def delete_upload(request, upload_id: int):
    upload = get_object_or_404(Upload, id=upload_id)
    upload.delete()
    return {"success": True}


# @api_controller("/uploads")
# class UploadsController(ControllerBase):
#     model = Upload
#
#     @http_post()
#     def create(self, payload: UploadIn, file: UploadedFile = File(...)):
#         filename = STORAGE.save(file.name, file)
#         payload_dict = payload.dict()
#         payload_dict["file"] = filename
#         upload = Upload.objects.create(**payload_dict)
#         return {"id": upload.id}
#
#     @http_generic(
#         "/{int:upload_id}", methods=["put", "patch"], response=UploadOut
#     )
#     def update(self, upload_id: int):
#         """Django Ninja will serialize Django ORM model to schema
#         provided as `response`"""
#         upload = self.get_object_or_exception(Upload, id=upload_id)
#         return upload
#
#     @http_delete(
#         "/{int:upload_id}",
#         response=Detail(status_code=status.HTTP_204_NO_CONTENT),
#     )
#     def delete(self, upload_id: int):
#         upload = self.get_object_or_exception(Upload, id=upload_id)
#         upload.delete()
#         return self.create_response(
#             "", status_code=status.HTTP_204_NO_CONTENT
#         )
#
#     @http_get("", response=pagination.PaginatedResponseSchema[UploadOut])
#     @pagination.paginate(pagination.PageNumberPaginationExtra, page_size=50)
#     def list(self):
#         return Upload.objects.all()
#
#     @http_get("/{upload_id}", response=UploadOut)
#     def get(self, upload_id: int):
#         upload = self.get_object_or_exception(Upload, id=upload_id)
#         return upload
#
#
# API.register_controllers(UploadsController)
