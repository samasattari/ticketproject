from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

department = (
    ('tec', 'tec'), # technical
    ('fin', 'fin'), # finsncial
    ('rev', 'rev'), # reviews
)

status = (
    ('open', 'open'),
    ('close', 'close'),
    ('ending', 'ending'),
)

priority = (
    ('very high', 'very high'), 
    ('high', 'high'), 
    ('medium', 'medium'), 
    ('low', 'low'),
    ('very low', 'very low'), 
)

process = (
    ('task', 'task'),
    ('sub task', 'sub task'),
 )


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="کاربر")
    title = models.CharField(max_length=100 , null=True, blank=True, verbose_name="عنوان")
    department = models.CharField(max_length=10, choices=department, null=True, blank=True, verbose_name="دپارتمان")
    content = models.TextField(verbose_name="محتوا")
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ  و زمان")
    update_date_time = models.DateTimeField(auto_now=True, verbose_name="تاریخ و زمان ویرایش")
    status = models.CharField(max_length=10, choices=status, default='open', null=True, blank=True, verbose_name="وضعیت")
    priority = models.CharField(max_length=10, choices=priority, default='medium', null=True, blank=True, verbose_name="اولویت")
    process = models.CharField(max_length=10, choices=process, null=True, blank=True, verbose_name="ثبت روند")
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)

condition = (
    ('do', 'do'),
    ('dont', 'dont'),
)


class Process(models.Model):
    description = models.TextField(verbose_name="شرح کار")
    assigment = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=" واگذاری")
    condition = models.CharField(max_length=10, choices=condition, null=True, blank=True, verbose_name="وضعیت")
    create_date = models.DateField(verbose_name="تاریخ ایجاد")
    do_date = models.DateField(verbose_name="تاریخ  انجام")
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)