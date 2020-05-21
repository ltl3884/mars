from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=255, null=True)
    user_name = models.CharField(max_length=255, null=True)
    unique_id = models.CharField(max_length=255, null=True)
    aweme_count = models.IntegerField(null=True)
    follower_count = models.IntegerField(null=True)
    user_score = models.IntegerField(null=True)
    last_update_time = models.DateTimeField(null=True)
    source_type = models.CharField(max_length=45, null=True)
    category = models.CharField(max_length=45, null=True)
    keyword = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    share_url = models.CharField(max_length=255, null=True)
    avatar_larger = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "users"
        indexes = [
            models.Index(fields=['uid']),
            models.Index(fields=['category']),
            models.Index(fields=['keyword'])
        ]


class Aweme(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255, null=True)
    aweme_id = models.CharField(max_length=255, null=True)
    digg_count = models.IntegerField(null=True)
    comment_count = models.IntegerField(null=True)
    desc = models.CharField(max_length=999, null=True)
    vid = models.CharField(max_length=255, null=True)
    cover_addr = models.CharField(max_length=500, null=True)
    video_addr = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(null=True)
    has_downloaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "awemes"
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['aweme_id']),
            models.Index(fields=['created_at'])
        ]