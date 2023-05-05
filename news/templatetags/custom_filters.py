from django import template
register = template.Library()
swear_word = ["колибри", "птица", "птиц", "птицы"]


@register.filter()
def cenz(text):
    for i in text.split():
        if i.lower() in swear_word:
            text = text.replace(i, f'***{i[0]}***')

    return text

