from django import forms


class BootstrapFormMixin:
    """Adds Bootstrap classes and basic a11y attributes to every field."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            is_checkbox = isinstance(field.widget, forms.CheckboxInput)
            css_class = "form-check-input" if is_checkbox else "form-control"
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing} {css_class}".strip()
            if field.required:
                field.widget.attrs["aria-required"] = "true"
