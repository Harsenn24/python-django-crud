import json
from django.shortcuts import render
from django.http.response import JsonResponse
from api_test.decorators import method
from bson.objectid import ObjectId
from .services import serviceTodo

# Create your views here.

@method("POST")
async def todo_create(req):
    body = json.loads(req.body)

    await serviceTodo.create(
        name=body.get("name"),
        description=body.get("description")
    )
    response = JsonResponse({
        "status": True
    }, status=200)
    return response


@method("GET")
async def list_todo(req):

    result = await serviceTodo.get_all()

    if len(result) == 0:
        return JsonResponse({"error": "data not found"}, status=400)

    response = JsonResponse({
        "data": result
    }, status=200)

    return response


@method("GET")
async def list_detail(req, id):
    try:
        id = ObjectId(id)
    except:
        return JsonResponse({"error": "id not valid"}, status=400)

    result = await serviceTodo.getbyid(id)

    if len(result) == 0:
        return JsonResponse({"error": "id not found"}, status=400)

    response = JsonResponse({
        "data": result[0]
    }, status=200)
    return response


@method("PUT")
async def update_data(req, id):

    try:
        id = ObjectId(id)
    except:
        return JsonResponse({"error": "id not valid"}, status=400)

    body = json.loads(req.body)

    result = await serviceTodo.update_partial(id, body)

    print(result)

    response = JsonResponse({
        "data": result
    }, status=200)
    return response


@method("DELETE")  # json
async def delete_todo(req, id):
    
    try:
        id = ObjectId(id)
    except:
        return JsonResponse({"error": "id not valid"}, status=400)

    result = await serviceTodo.delete(id)
    response = JsonResponse({
        "data": result
    }, status=200)
    return response


#  @method("GET")
# async def query_todo(req):
#     username = req.GET.get("username")  # endpoint?username=___

#     response = JsonResponse({
#         "data": username
#     }, status=200)
#     return response


# @method("POST")  # form-data / multipart/form-data
# async def post_todo(req):
#     username = req.POST.get("username")
#     any_file = req.FILES.get("my_file_field")
#     many_file = req.FILES.getlist('my_file_field')

#     response = JsonResponse({
#         "data": username
#     }, status=200)
#     return response
