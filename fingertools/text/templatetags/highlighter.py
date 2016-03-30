from django import template

register = template.Library()

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from django.utils.safestring import mark_safe

@register.filter
def html_highlight(txt):
	try:
		lexer = get_lexer_by_name(txt.language)
	except ClassNotFound:
		lexer = guess_lexer(txt.language)
	form = HtmlFormatter(linenos=True)
	res = highlight(txt.text, lexer, form)
	return mark_safe(res)
