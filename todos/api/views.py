# APIS

from rest_framework.viewsets import ModelViewSet

from todos.models import Todo
from todos.api.serializers import TodosSerializer


class TodosViewSet(ModelViewSet):
    serializer_class = TodosSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()
        print("queryset: ", queryset)
        return queryset
