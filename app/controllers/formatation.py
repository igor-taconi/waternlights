from datetime import date

from flask_admin.model.typefmt import BASE_FORMATTERS, null_formatter


def date_format(view, value):
    return value.strftime('%H:%M:%S - %d/%m/%Y')


date_formatters = dict(BASE_FORMATTERS)
date_formatters.update(
    {type(None): null_formatter, date: date_format}
)
