from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from jenkinsMain.helpers import name_manager, numbers
from jenkinsMain.helpers.nameReader import read_names


@api_view(["POST", "GET"])
def create_get_names(request):
    if request.method == "GET":
        return JsonResponse(data=read_names(), status=status.HTTP_200_OK, safe=False)
    elif request.method == "POST":
        name_manager.generate_name(request.data["name"])
        return JsonResponse(
            data={"message": "data successfully created"},
            status=status.HTTP_201_CREATED,
            safe=False,
        )


@api_view(["PUT"])
def update_name(request, name_id: int):
    name_manager.update_name(name_id, request.data["name"])
    return JsonResponse(
        data={"message": "data successfully updated"},
        status=status.HTTP_200_OK,
        safe=False,
    )


@api_view(["DELETE"])
def delete_name(request, name_id: int):
    try:
        name_manager.delete_name(name_id)
        return JsonResponse(
            data={"message": "Name successfully deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
    except Exception as e:
        return JsonResponse(
            data={"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def sin_of_number(request):
    try:
        number = request.data.get("number")
        result = numbers.calculate_sin(number)
        return JsonResponse({"sin": result}, status=status.HTTP_200_OK)
    except (ValueError, TypeError):
        return JsonResponse(
            {"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def cos_of_number(request):
    try:
        number = request.data.get("number")
        result = numbers.calculate_cos(number)
        return JsonResponse({"cos": result}, status=status.HTTP_200_OK)
    except (ValueError, TypeError):
        return JsonResponse(
            {"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def random_number(request):
    try:
        start = int(request.query_params.get("start", 0))
        end = int(request.query_params.get("end", 100))
        result = numbers.generate_random_number(start, end)
        return JsonResponse({"random_number": result}, status=status.HTTP_200_OK)
    except (ValueError, TypeError):
        return JsonResponse(
            {"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST
        )
