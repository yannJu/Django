#markdown 을 이용하여 사용자 정의 필터 생성
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def mark(value):
    extensions = ['nl2br', 'fenced_code'] #nl2br : nl 태그를 br 태그로 바꾸겠다, fenced_code :  decorator 를 약간 넣겠다
    # print(markdown.markdown(value, extensions=extensions))
    return mark_safe(markdown.markdown(value, extensions=extensions)) #markdown을 적용

#{%%} 와 같은 태그 정의
#{%avatar user.id%} 처럼 사용
# 직접 공부해보기
# @register.simple_tag()
# def avatar(uid):
#     tag = f'<img class="avarta" src="https://randomuser.me/api/portraits/men/{{uid}}.jpg"/>'
#     return mark_safe(tag)