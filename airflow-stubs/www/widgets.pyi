import flask_appbuilder.fieldwidgets
import flask_appbuilder.widgets
from typing import ClassVar

class AirflowModelListWidget(flask_appbuilder.widgets.RenderTemplateWidget):
    template: ClassVar[str] = ...

class AirflowDateTimePickerWidget:
    data_template: ClassVar[str] = ...
    def __call__(self, field, **kwargs): ...

class AirflowDateTimePickerROWidget(AirflowDateTimePickerWidget):
    def __call__(self, field, **kwargs): ...

class BS3TextFieldROWidget(flask_appbuilder.fieldwidgets.BS3TextFieldWidget):
    def __call__(self, field, **kwargs): ...

class BS3TextAreaROWidget(flask_appbuilder.fieldwidgets.BS3TextAreaFieldWidget):
    def __call__(self, field, **kwargs): ...

class AirflowVariableShowWidget(flask_appbuilder.widgets.RenderTemplateWidget):
    template: ClassVar[str] = ...
