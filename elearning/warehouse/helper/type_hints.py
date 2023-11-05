from typing import NewType

from elearning.warehouse.models import Product, Question

Division = NewType("Division", Product)
Bootcamp = NewType("Bootcamp", Product)
Course = NewType("Course", Product)
Project = NewType("Project", Product)
Lesson = NewType("Lesson", Product)
Chapter = NewType("Chapter", Product)
Practice = NewType("Practice", Product)

Checkbox = NewType("Checkbox", Question)
Radio = NewType("Radio", Question)
Placeholder = NewType("Placeholder", Question)
Conditional = NewType("Conditional", Question)
Code = NewType("Code", Question)
