from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    articles = models.ManyToManyField(Article, through = 'ArticleTags', related_name ='tags')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Раздел'

    def __str__(self):
        return self.title

class ArticleTags(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'articletags')
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, related_name = 'articletags')
    main_tag = models.BooleanField(default = False)


