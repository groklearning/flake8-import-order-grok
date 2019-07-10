# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from flake8_import_order import ImportType
from flake8_import_order.styles import Style

__all__ = ["GrokImportOrderStyle"]

NAME_TYPE_CONSTANT, NAME_TYPE_CLASS, NAME_TYPE_FUNCTION = range(3)
RELATIVE_SET = {ImportType.APPLICATION, ImportType.APPLICATION_RELATIVE}


def sort_name_key(name):
    """
    Classifies a name as being either CAPITAL_CASE, CamelCase, or
    underscore_case.
    """
    if name.isupper():
        return NAME_TYPE_CLASS if len(name) == 1 else NAME_TYPE_CONSTANT
    elif name.islower():
        return NAME_TYPE_FUNCTION
    else:
        return NAME_TYPE_CLASS if name[0].isupper() else NAME_TYPE_FUNCTION


class GrokImportOrderStyle(Style):
    """
    All groups need a line break between them, except between __future__ and
    builtins.

    All groups must be alphabetical horizontally and vertically. Within an
    import unit, names must be constants first, followed by classes, followed
    by functions (CAPITAL_CASE, CamelCase, underscore_case).

    Group ordering:
    1. __future__
    2. builtins
    3. django
    4. third-party, grouped by package
    5. grok
    """

    @staticmethod
    def import_key(import_):
        package = None if import_.package is None else import_.package.lower()
        if import_.type in (ImportType.FUTURE, ImportType.STDLIB):
            return (
                ImportType.FUTURE,
                import_.type,
                package,
                import_.is_from,
                import_.level,
                import_.modules,
                import_.names,
            )
        elif import_.type in {ImportType.THIRD_PARTY}:
            django_first = 0 if import_.package == "django" else 1
            return (
                import_.type,
                django_first,
                package,
                import_.is_from,
                import_.level,
                import_.modules,
                import_.names,
            )
        else:
            return (
                import_.type,
                package,
                import_.is_from,
                import_.level,
                import_.modules,
                import_.names,
            )

    @staticmethod
    def same_section(previous, current):
        if previous.type == ImportType.FUTURE and current.type == ImportType.STDLIB:
            return True

        app_or_third = current.type in {ImportType.THIRD_PARTY, ImportType.APPLICATION}
        same_type = current.type == previous.type
        both_relative = {previous.type, current.type} <= RELATIVE_SET
        same_package = previous.package == current.package
        return (not app_or_third and same_type or both_relative) or (
            app_or_third and same_package
        )

    @staticmethod
    def sorted_names(names):
        # Names within an import line must be alphabetical.
        return sorted(names, key=sort_name_key)
