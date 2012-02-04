from django import template

register = template.Library()

@register.filter()
def make_lead(post, length=500):
    return post[:length]+'...'
