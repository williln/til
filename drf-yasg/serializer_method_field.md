# How to properly serialize a `serializer_method_field` with `drf_yasg`

When you're using `drf_yasg`, your Swagger page (your API auto-documentation) will pick up on the serializers you're using to decide how to display the parameters for requests and the formatting of the responses for your API endpoints.

But when a field in your serializer uses DRF's `serializer_method_field()`, `drf_yasg` is just going to default to showing that field as a string.

To help `drf_yasg` render your serializer accurately, use the `swagger_serializer_method` decorator. It takes one argument, `serializer_or_field`, and that argument can accept either a serializer field or another complete serializer.

```python
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    availability = serializers.SerializerMethodField()

    class Meta:
        model = models.Book
        fields = ("title", "availability")

    swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_status(self, obj):
        return obj.copies_available

```

(Note: this is an imperfect example. I know you could just use the `source` argument when defining the `availability` field, but I was trying to come up with an example on the fly so bear with me.)
