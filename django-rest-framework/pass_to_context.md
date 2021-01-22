# Passing extra info in `context` to your DRF serializer

This is something I always have to look up, so I'm writing it down here.

The `get_serializer()` and `get_serializer_class` methods do different things. See [ClassyDRF](http://www.cdrf.co/3.9/rest_framework.viewsets/ModelViewSet.html).

`get_serializer_class()` returns the serializer class itself.

`get_serializer()` calls `get_serializer_class`, then calls `get_serializer_context()`, and returns the serializer class with the context added as a kwarg.

There are a few options for adding custom data to the serializer context:

1. Override `get_serializer_context()` and add fields you need to the context dictionary there. Best for cases where you want to add context to all endpoints in the viewset.

2. Get the serializer directly, bypassing `get_serializer()`, and generate the context with `get_serializer_context()` and add your fields there.

3. Get the serializer from `get_serializer_class()`, retrieve the context from `get_serializer_context()`, and add your fields to the context before continuing to process the serializer.

Method #3 shown below.


```python
from rest_framework import viewsets

from . import models, serializers


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MySerializerClass

    def list(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        context = {**super().get_serializer_context(),
            "extra": "my_extra_stuff",
        }
        serializer = serializer_class(queryset, many=True, context=context)
        # rest of processing goes here
```

You can then access `self.context["extra"]` from any method in the serializer.

```python
class MyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyModel
        fields = (...)

    def get_field(self, obj):
        extra = self.context["extra"]
        # continue processing
```
