from djongo import models # djongoのモデルを利用する

class Posts(models.Model):
    title = models.TextField(verbose_name='タイトル')
    contents = models.TextField(verbose_name='内容')
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')
    post_no = models.TextField(primary_key=True, verbose_name='投稿番号')
    categories = models.JSONField(default=list)
    tags = models.JSONField(default=list)
    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

class Labels(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='ラベル番号')
    name = models.TextField(verbose_name='ラベル名')
    type = models.TextField(verbose_name='ラベルタイプ')
    class Meta:
        db_table = 'labels'

    def __str__(self):
        return self.name