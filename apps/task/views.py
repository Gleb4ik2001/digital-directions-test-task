from rest_framework import viewsets, permissions, filters, generics
from .models import Task
from .serializers import TaskSerializer,RegisterSerializer
from django.contrib.auth.models import User


class TaskListAPIView(generics.ListAPIView):
    """Получение списка задач текущего пользователя с фильтрацией и сортировкой"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['due_date']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskCreateAPIView(generics.CreateAPIView):
    """Создание новой задачи"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    """Получение одной задачи по id (только своей)"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskUpdateAPIView(generics.UpdateAPIView):
    """Обновление существующей задачи (PUT/PATCH)"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDestroyAPIView(generics.DestroyAPIView):
    """Удаление задачи"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class RegisterView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]