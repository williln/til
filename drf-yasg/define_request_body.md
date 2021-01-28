# How to serialize your request parameters for POST/PUT/PATCH requests

When creating Swagger API docs with `drf_yasg`, you want to be able to define the parameters the requester will use when calling API endpoints that perform updates. `drf_yasg` does a decent job with this with DRF's built-in methods from the ModelViewSet as long as you're using `get_serializer_class` appropriately. But for custom action endpoints, or situations where you're instantiating your serializer manually in the method, it can get tricky.

Pass the `request_body` argument to the `@swagger_auto_schema` decorate on your API method. If your API endpoint takes parameters (say, a new `first_name` and `last_name` to update the user), make sure those fields are in a serializer and pass that serializer to `request_body`. If your action takes no parameters (a `DELETE` endpoint or a `PUT` endpoint that updates a specific status), import `no_body` and pass that to `request_body`.

```python
from drf_yasg.utils import no_body, swagger_auto_schema

from .serializers import BookTitleSerializer

class BookViewSet(ModelViewSet):

    ...

    @swagger_auto_schema(request_body=BookTitleSerializer)
    @action(detail=True, methods=["post"])
    def update_title(self, request, pk=None):
        serializer = BookTitleSerializer(data=request.data)
        ...

    @swagger_auto_schema(request_body=no_body)
    @action(detail=True, methods=["post"])
    def mark_unavailable(self, request, pk=None):
        obj = self.get_object()
        ...

```
