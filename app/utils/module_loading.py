import sys



def import_by_path(dotted_path, error_prefix=''):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImproperlyConfigured if something goes wrong.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        raise Exception("%s%s doesn't look like a module path" % (error_prefix, dotted_path))
    try:
        __import__(module_path)
        module = sys.modules[module_path]
    except ImportError as e:
        raise Exception('%sError importing module %s: "%s"' % (error_prefix, module_path, e))


    try:
        attr = getattr(module, class_name)
    except AttributeError:
        raise Exception('%sModule "%s" does not define a "%s" attribute/class' % (
            error_prefix, module_path, class_name
        ))
    return attr
