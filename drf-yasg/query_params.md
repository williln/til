# How to document your query parameters for `drf_yasg`

Sometimes your API takes a specific set of query parameters and you want the consumers of your Swagger AIP documentation to be able to test out these query parameters, which means `drf_yasg` needs to serialize them appropriately.

To do this, decorate your API method with `@swagger_auto_schema` and pass a serializer into the `query_serializer` argument.

```python
# views.py
from drf_yasg.utils import swagger_auto_schema

from .serializers import BookQueryParamSerializer

class BookViewSet(ModelViewSet):

    ...

    @swagger_auto_schema(query_serializer=BookQueryParamSerializer)
    def list(self, request, *args, **kwargs):
        ...



# serializers.py

class BookQueryParamSerializer(serializers.Serializer):
    author_last_name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
```

Something to be aware of is making sure your query params use the same fields as any filter classes or filterset classes you're using on that endpoint. I have encountered errors in Swagger when those didn't match. (In that case, it was because I was taking query params that would be used for filtering, and also query params that would be used for other processing. I wound up filtering my queryset manually and removing the filterset class I had been using.)
