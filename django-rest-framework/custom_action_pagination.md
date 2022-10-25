# Adding a custom pagination class to an action 

## 1. Create your custom pagination class 

```python
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 10000

```

## 2. Add it to your action 

```python
from .pagination import LargeResultsSetPagination

class MyViewSet(viewsets.ModelViewSet):
    ...
    # pass in pagination_class
    @action(detail=False, methods=["GET"], pagination_class=LargeResultsSetPagination)
    def my_action(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

## 3. Write a test 

```python
@pytest.mark.django_db()
def test_pagination(tp, user, password):eeds to page through results
    """
    count = 600
    baker.make("models.MyModel", quantity=count)
    url = tp.reverse("my-action-url")
    tp.client.login(username=user.email, password=password)
    response = tp.get_check_200(url)
    # Actual results returned is pagination default
    assert len(response.json()["results"]) == 200
    # Atual count is reflected and accurate
    assert response.json()["count"] == count
    assert response.json()["next"] is not None
```
