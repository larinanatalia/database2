from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTags

class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            data = form.cleaned_data
            if data.get('main_tag') is True:
                counter += 1
            else:
                continue
        if counter == 0:
            raise ValidationError('Укажите основной раздел')
        elif counter > 1:
                raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass