from rest_framework.routers import DefaultRouter

from todos.api.views import TodosViewSet

router = DefaultRouter()
router.register('', TodosViewSet, basename="todos")

urlpatterns = router.urls
