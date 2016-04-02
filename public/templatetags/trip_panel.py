from django import template
register = template.Library()


@register.inclusion_tag('public/_trip_panel.html')
def trip_panel(trip):
	return {
		'trip': trip
	}
