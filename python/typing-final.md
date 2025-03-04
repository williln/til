# `typing.final` 

## Links 

- [Python docs: `typing.final`](https://docs.python.org/3/library/typing.html#typing.final)

## Notes 

Adding the `@final` decorator to a class or class method indicates that the object cannot be overridden. You can't subclass that class and you can't override that method in a subclass. 

You can add it to either a class or a method on a class. 

Example from the docs: 

```python
class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...

@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...
```
