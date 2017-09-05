from django import template


register = template.Library()

@register.filter
def sssss(x,y):
    return int(x)*2+int(y)

@register.filter
def get_item(dictionary, key):
    if key is None:
        return ""
    return dictionary.get(int(key), '')    
