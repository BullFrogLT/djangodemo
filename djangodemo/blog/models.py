# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class AlertReport(models.Model):
    '''
    告警信息表
    '''
    ALERT_LEVEL = (
        (1, '错误（失败）'),
        (2, '警告')
    )
    ALERT_STATUS = (
        (0, '待处理'),
        (1, '已处理')
    )
    id = models.AutoField(primary_key=True)
    alert_from = models.IntegerField('告警来源', default=1)     #0 内部告警 1外部告警
    from_place = models.CharField('所属地市', max_length=50)
    from_system = models.CharField('所属系统', max_length=50)
    from_role = models.CharField('所属角色', max_length=50, blank=True)
    from_machine = models.CharField('所属机器', max_length=50, blank=True)
    from_plugin = models.CharField('插件', max_length=30, blank=True)
    from_check_method = models.CharField('检查项', max_length=100, blank=True)
    alert_title = models.CharField('告警标题', max_length=50)
    level = models.IntegerField('告警级别', choices=ALERT_LEVEL, default=1)
    message = models.TextField('告警信息', blank=True)
    remark = models.TextField('备注', blank=True)
    report_time = models.DateTimeField('上报时间')
    status = models.IntegerField('状态', choices=ALERT_STATUS, default=0)

    class Meta:
        verbose_name = '告警信息上报'
        verbose_name_plural = '告警信息上报'
