
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from product.serializers import ProductSerializer, PublicationSerializer,StudentSerialization,StudentSerialization1
from product.models import Product, Publication,Student
from rest_framework import viewsets,permissions
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublicationViewSet(viewsets.ModelViewSet):

    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]
#eatch studentdetails according to primary key
@csrf_exempt
def student_detail(request, pk):
    try:
        stu_details = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = StudentSerialization(stu_details)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':

        serializer = StudentSerialization(stu_details)
        return JsonResponse(serializer.data)


    elif request.method == 'PUT':

        data = JSONParser().parse(request)
        serializer = StudentSerialization1(stu_details, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    #stu_details = Student.objects.get(id=pk)
    #stu_serilializer = StudentSerialization(stu_details)
    # json_data = JSONRenderer().render(stu_serilializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(stu_serilializer.data)
@csrf_exempt
def delete_student(request, pk):
    try:
        stu_details = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    stu_details.delete()
    print("Delete..........")
    return HttpResponse(status=204)


def student_list(request):

    stu_details = Student.objects.all()
    stu_serilializer = StudentSerialization(stu_details, many=True)
    json_data = JSONRenderer().render(stu_serilializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def addstudent(request):
    data = JSONParser().parse(request)
    serializer = StudentSerialization1(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)




