from django import template

register = template.Library()


@register.filter
def vote_can_edit(vote, user) -> bool:
    return vote.can_edit(user)


@register.filter
def vote_can_delete(vote, user) -> bool:
    return vote.can_delete(user)
