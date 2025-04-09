from flask_appbuilder.fieldwidgets import BS3TextAreaFieldWidget, BS3TextFieldWidget
from flask_appbuilder.widgets import RenderTemplateWidget

class AirflowModelListWidget(RenderTemplateWidget):
    template: str

class AirflowDateTimePickerWidget:
    data_template: str
    def __call__(self, field, **kwargs): ...

class AirflowDateTimePickerROWidget(AirflowDateTimePickerWidget):
    def __call__(self, field, **kwargs): ...

class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs): ...

class BS3TextAreaROWidget(BS3TextAreaFieldWidget):
    def __call__(self, field, **kwargs): ...

class AirflowVariableShowWidget(RenderTemplateWidget):
    template: str
