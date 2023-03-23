from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class City(models.Model):

    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.city


class Street(models.Model):

    stree_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"

    def __str__(self):
        return self.street


class Address(models.Model):

    address_id = models.AutoField(primary_key=True)

    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    street = models.ForeignKey(Street, on_delete=models.RESTRICT)
    number = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return "г. {}, {}, д. {}".format(self.city, self.street, self.number)

    def get_absolute_url(self):
        return reverse("avito_address_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_address_update", args=(self.pk,))


class DealStatus(models.Model):

    dealStatus_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Статус сделки"
        verbose_name_plural = "Статусы сделок"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("avito_deal_status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_deal_status_update", args=(self.pk,))


class PostStatus(models.Model):

    postStatus_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Статус объявления"
        verbose_name_plural = "Статусы объявлений"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("avito_post_status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_post_status_update", args=(self.pk,))


class PostCategory(models.Model):

    postCategory_id = models.AutoField(primary_key=True)
    # Fields
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Категория объявления"
        verbose_name_plural = "Категории объявлений"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("avito_post_category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_post_category_update", args=(self.pk,))


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    phone_number = models.CharField(max_length=11)
    birth_date = models.DateField(null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'surname', 'phone_number', 'birth_date', 'email']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return "{}".format(self.username)

    def get_absolute_url(self):
        return reverse("avito_user_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_user_update", args=(self.pk,))


class Post(models.Model):

    post_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    category = models.ForeignKey(PostCategory, on_delete=models.RESTRICT)
    status = models.ForeignKey(
        PostStatus, default="Активно", on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Обявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("avito_post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_post_update", args=(self.pk,))


class Comment(models.Model):

    comment_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT,
                             related_name='%(class)s_requests_created')           # На кого отзыв
    user_comment = models.ForeignKey(
        CustomUser, on_delete=models.RESTRICT)   # От кого

    text = models.TextField(max_length=100)
    rating = models.PositiveSmallIntegerField()

    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("avito_comments_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_comments_update", args=(self.pk,))


class Deal(models.Model):

    deal_id = models.AutoField(primary_key=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    status = models.ForeignKey(DealStatus, on_delete=models.RESTRICT)
    date = models.DateTimeField(editable=True)

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        return reverse("avito_deal_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_deal_update", args=(self.pk,))


class File(models.Model):

    # Fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    link = models.URLField()

    class Meta:
        verbose_name = "Вложение"
        verbose_name_plural = "Вложения"

    def __str__(self):
        return str(self.post)

    def get_absolute_url(self):
        return reverse("avito_files_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("avito_files_update", args=(self.pk,))
