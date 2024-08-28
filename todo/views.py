from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from .models import *
from .serializers import * 


@api_view(['GET'])
def get_todo(request):
    response = {'status' : 200}
    todo_objs = Task.objects.all() 
    serializers = TaskSerializer(todo_objs , many = True)
    response['data'] = serializers.data
    return Response(response)

@api_view(['POST'])
def post_todo(request):
    response = {'status' : 200}
    data = request.data 
    serializers = TaskSerializer(data = data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# @api_view(['GET'])
# def get_todo(request):
#     response = {'status': 200}
#     todo_objs = Task.objects.all()
#     serializers = TaskSerializer(todo_objs, many=True)
#     response['data'] = serializers.data
#     return Response(response)

# # Function-based view to handle POST requests for creating a new task
# @api_view(['POST'])
# def post_todo(request):
#     response = {'status' : 200}
#     data = request.data 
#     serializers = TaskSerializer(data = data)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(response)
    

#     return Response(serializers.errors)

# # Class-based view to handle both listing all tasks (GET) and creating a new task (POST)
# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# # Class-based view to handle retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) a specific task
# class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer












# # Function-based view for getting all tasks and creating a new task
# @api_view(['GET', 'POST'])
# def task_list_create(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Function-based view for retrieving, updating, and deleting a specific task
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     elif request.method in ['PUT', 'PATCH']:
#         serializer = TaskSerializer(task, data=request.data, partial=(request.method == 'PATCH'))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Class-based views for listing and creating tasks
# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# # Class-based views for retrieving, updating, and deleting a specific task
# class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer