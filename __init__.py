
def get_product_model():
    "Return the Product model"
    from django.core.exceptions import ImproperlyConfigured
    from django.conf import settings
    from django.db.models import get_model

    try:
        app_label, model_name = settings.FASTCART_PRODUCT_MODEL.split('.')
    except ValueError:
        raise ImproperlyConfigured("FASTCART_PRODUCT_MODEL must be of the form 'app_label.model_name'")
    product_model = get_model(app_label, model_name)

    if product_model is None:
        raise ImproperlyConfigured("FASTCART_PRODUCT_MODEL refers to model '%s' that has not been installed" % settings.FASTCART_PRODUCT_MODEL)
    return product_model
