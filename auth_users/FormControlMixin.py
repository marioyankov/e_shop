class FormControlMixin():
    def __init_fields__(self, *args, **kwargs):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
