from django import template
register = template.Library()
swear_word = ['пидор', "пидр", "пидрила", "капибара"]


@register.filter()
def cenz(text):
    for i in text.split():
        if i in swear_word:
            text = text.replace(i, f'***{i[0]}***')

    return text

