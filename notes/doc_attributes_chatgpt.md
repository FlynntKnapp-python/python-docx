#

I'm using Python `python-docx` and it's `Document` class.

Can you show me a side-by-side list of `Document` class attributes next to an instantiated `doc = Document()` object attributes?

To provide a side-by-side list of the `Document` class attributes and the attributes of an instantiated object (e.g., `doc = Document()`), I'll first instantiate a `Document` object from the `python-docx` library, then introspect its class and the object itself to list their attributes. This will help us see the attributes defined at the class level versus those available on the instance.

Let's proceed with the code to achieve this comparison.

It looks like I forgot to import `zip_longest` from the `itertools` module, which is necessary to pair the class and instance attributes side-by-side, especially when the lists have different lengths. Let's correct this and try again.

Here's a side-by-side comparison of attributes from the `Document` class and an instantiated `doc` object using the `python-docx` library. This list includes both the attributes defined by the class and those available on the instance:

| `Document` Class Attributes | `doc` Instance Attributes |
|-----------------------------|---------------------------|
| `__annotations__`           | `_Document__body`         |
| `__builtins__`              | `__class__`               |
| `__call__`                  | `__delattr__`             |
| `__class__`                 | `__dir__`                 |
| `__closure__`               | `__doc__`                 |
| `__code__`                  | `__eq__`                  |
| `__defaults__`              | `__format__`              |
| `__delattr__`               | `__ge__`                  |
| `__dict__`                  | `__getattribute__`        |
| `__dir__`                   | `__getstate__`            |
| `__doc__`                   | `__gt__`                  |
| `__eq__`                    | `__hash__`                |
| `__format__`                | `__init__`                |
| `__ge__`                    | `__init_subclass__`       |
| `__get__`                   | `__le__`                  |
| `__getattribute__`          | `__lt__`                  |
| `__getstate__`              | `__module__`              |
| `__globals__`               | `__ne__`                  |
| `__gt__`                    | `__new__`                 |
| `__hash__`                  | `__reduce__`              |
| `__init__`                  | `__reduce_ex__`           |
| `__init_subclass__`         | `__repr__`                |
| `__kwdefaults__`            | `__setattr__`             |
| `__le__`                    | `__sizeof__`              |
| `__lt__`                    | `__slots__`               |
| `__module__`                | `__str__`                 |
| `__name__`                  | `__subclasshook__`        |
| `__ne__`                    | `_block_width`            |
| `__new__`                   | `_body`                   |
| `__qualname__`              | `_element`                |
| `__reduce__`                | `_parent`                 |
| `__reduce_ex__`             | `_part`                   |
| `__repr__`                  | `add_heading`             |
| `__setattr__`               | `add_page_break`          |
| `__sizeof__`                | `add_paragraph`           |
| `__str__`                   | `add_picture`             |
| `__subclasshook__`          | `add_section`             |
|                             | `add_table`               |
|                             | `core_properties`         |
|                             | `element`                 |
|                             | `inline_shapes`           |
|                             | `paragraphs`              |
|                             | `part`                    |
|                             | `save`                    |
|                             | `sections`                |
|                             | `settings`                |
|                             | `styles`                  |
|                             | `tables`                  |

This comparison shows that the `Document` class itself includes a variety of Python's built-in attributes and methods (as do all classes), whereas the instantiated `doc` object has both inherited methods and attributes specific to its role in representing a Word document, such as methods for adding headings, paragraphs, pictures, and tables, as well as attributes representing the document's elements, properties, and styles.

Can you remake that table list where if the same attributes are paired side-by-side where the `class` and `object` have the same attribute name?

Sure, let's refine the comparison to pair identical attribute names side-by-side when both the `Document` class and the instantiated `doc` object share the same attribute name. For this, I'll adjust the approach to directly match identical attribute names between the class and the instance, leaving spaces where there's no direct match.

Here's a revised comparison focusing on pairing identical attribute names between the `Document` class and the instantiated `doc` object, alongside unique attributes to each:

| Matched Attributes     | Unique to Class or Object  |
|------------------------|----------------------------|
| `__class__`            | `__annotations__`          |
| `__delattr__`          | `__builtins__`             |
| `__dir__`              | `__call__`                 |
| `__doc__`              | `__closure__`              |
| `__eq__`               | `__code__`                 |
| `__format__`           | `__defaults__`             |
| `__ge__`               | `__dict__`                 |
| `__getattribute__`     | `__get__`                  |
| `__getstate__`         | `__globals__`              |
| `__gt__`               | `__kwdefaults__`           |
| `__hash__`             | `__name__`                 |
| `__init__`             | `__qualname__`             |
| `__init_subclass__`    | `add_table`                |
| `__le__`               | `core_properties`          |
| `__lt__`               | `element`                  |
| `__module__`           | `inline_shapes`            |
| `__ne__`               | `paragraphs`               |
| `__new__`              | `part`                     |
| `__reduce__`           | `save`                     |
| `__reduce_ex__`        | `sections`                 |
| `__repr__`             | `settings`                 |
| `__setattr__`          | `styles`                   |
| `__sizeof__`           | `tables`                   |
| `__str__`              |                            |
| `__subclasshook__`     |                            |

This table lists attributes that are identical between the class and instance in the first column, and unique attributes (to either the class or the instance) in the second column. Attributes like `__init__`, `__str__`, and `__repr__` are common Python magic methods present in both the class and instance. The second column shows attributes that are unique to either the class or the instantiated object, indicating specialized functionality or metadata.

Can you modify the list to have the columns `Class Attributes` and `Instance Attributes` and the rows show the attributes. If the attribute is in both the `Class Attributes` and `Instance Attributes`, the attribute will be listed in both rows? That way I can easily see what attributes are common to both class and instance, as well as the attributes which are unique?

Certainly, let's organize the attributes into two columns, `Class Attributes` and `Instance Attributes`, listing attributes in both when they're common to both the class and the instance. Unique attributes will only appear under their respective columns. This will clearly show the attributes shared between the class and the instance, as well as those that are unique to each.

Here's the organized list with the columns `Common Attributes`, `Class Only Attributes`, and `Instance Only Attributes`. This format allows for easy identification of attributes that are common to both the `Document` class and its instance (`doc`), as well as those unique to each.

| Common Attributes   | Class Only Attributes   | Instance Only Attributes |
|---------------------|-------------------------|--------------------------|
| `__class__`         | `__annotations__`       | `_Document__body`        |
| `__delattr__`       | `__builtins__`          | `__slots__`              |
| `__dir__`           | `__call__`              | `_block_width`           |
| `__doc__`           | `__closure__`           | `_body`                  |
| `__eq__`            | `__code__`              | `_element`               |
| `__format__`        | `__defaults__`          | `_parent`                |
| `__ge__`            | `__dict__`              | `_part`                  |
| `__getattribute__`  | `__get__`               | `add_heading`            |
| `__getstate__`      | `__globals__`           | `add_page_break`         |
| `__gt__`            | `__kwdefaults__`        | `add_paragraph`          |
| `__hash__`          | `__name__`              | `add_picture`            |
| `__init__`          | `__qualname__`          | `add_section`            |
| `__init_subclass__` |                         | `add_table`              |
| `__le__`            |                         | `core_properties`        |
| `__lt__`            |                         | `element`                |
| `__module__`        |                         | `inline_shapes`          |
| `__ne__`            |                         | `paragraphs`             |
| `__new__`           |                         | `part`                   |
| `__reduce__`        |                         | `save`                   |
| `__reduce_ex__`     |                         | `sections`               |
| `__repr__`          |                         | `settings`               |
| `__setattr__`       |                         | `styles`                 |
| `__sizeof__`        |                         | `tables`                 |
| `__str__`           |                         |                          |
| `__subclasshook__`  |                         |                          |

This table clearly shows the attributes shared between the class and instance, such as `__init__`, `__str__`, and other dunder methods inherent to Python objects, alongside those attributes unique to the class (like `__annotations__`, `__builtins__`, etc.) and unique to the instance (such as `add_heading`, `add_paragraph`, and other methods specific to manipulating Word documents).

Sure, let's adjust the format to have two columns: one for `Class Attributes` and another for `Instance Attributes`. In this layout, if an attribute is present in both, it will be listed in both columns, allowing for an easy comparison of shared and unique attributes.

Here's the adjusted list with two columns: one for `Class Attributes` and another for `Instance Attributes`. Attributes present in both are listed in both columns, making it easy to see which attributes are common to both class and instance, as well as which are unique to each.

| Class Attributes     | Instance Attributes |
|----------------------|---------------------|
| `__class__`          | `__class__`         |
| `__delattr__`        | `__delattr__`       |
| `__dir__`            | `__dir__`           |
| `__doc__`            | `__doc__`           |
| `__eq__`             | `__eq__`            |
| `__format__`         | `__format__`        |
| `__ge__`             | `__ge__`            |
| `__getattribute__`   | `__getattribute__`  |
| `__getstate__`       | `__getstate__`      |
| `__gt__`             | `__gt__`            |
| `__hash__`           | `__hash__`          |
| `__init__`           | `__init__`          |
| `__init_subclass__`  | `__init_subclass__` |
| `__le__`             | `__le__`            |
| `__lt__`             | `__lt__`            |
| `__module__`         | `__module__`        |
| `__ne__`             | `__ne__`            |
| `__new__`            | `__new__`           |
| `__reduce__`         | `__reduce__`        |
| `__reduce_ex__`      | `__reduce_ex__`     |
| `__repr__`           | `__repr__`          |
| `__setattr__`        | `__setattr__`       |
| `__sizeof__`         | `__sizeof__`        |
| `__str__`            | `__str__`           |
| `__subclasshook__`   | `__subclasshook__`  |
| `__annotations__`    | `_Document__body`   |
| `__builtins__`       | `__slots__`         |
| `__call__`           | `_block_width`      |
| `__closure__`        | `_body`             |
| `__code__`           | `_element`          |
| `__defaults__`       | `_parent`           |
| `__dict__`           | `_part`             |
| `__get__`            | `add_heading`       |
| `__globals__`        | `add_page_break`    |
| `__kwdefaults__`     | `add_paragraph`     |
| `__name__`           | `add_picture`       |
| `__qualname__`       | `add_section`       |
|                      | `add_table`         |
|                      | `core_properties`   |
|                      | `element`           |
|                      | `inline_shapes`     |
|                      | `paragraphs`        |
|                      | `part`              |
|                      | `save`              |
|                      | `sections`          |
|                      | `settings`          |
|                      | `styles`            |
|                      | `tables`            |

This table now clearly separates attributes that are common to both the class and the instantiated object (listed in both columns), as well as those unique to each (listed in one column but not the other). Attributes such as magic methods (`__init__`, `__str__`, etc.) are present in both, highlighting Python's class-object architecture. Meanwhile, instance-specific attributes like `add_heading`, `add_paragraph`, and `_element` underscore the instantiated object's role and capabilities within the `python-docx` library's functionality.