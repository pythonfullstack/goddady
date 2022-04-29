from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        """
        define custom validation
        :return:
        """


class TaskQueueQuerySet(models.QuerySet):
    """
        TODO Define TaskQueue Operations
    """

    def drop(self):
        pass

    def retry(self):
        pass

    def assign(self):
        pass


class TaskQueue(models.Model):
    CREATE_EMR = 'create_emr'
    UPDATE_EMR = 'update_emr'
    DELETE_EMR = 'delete_emr'
    TASKS = (
        (CREATE_EMR, 'Create EMR'),
        (UPDATE_EMR, 'Update EMR'),
        (DELETE_EMR, 'Delete EMR'),
    )

    WAITING = 'waiting'
    PROCESSING = 'processing'
    FAILED = 'failed'

    STATUSES = (
        (WAITING, 'Waiting'),
        (PROCESSING, 'Processing'),
        (FAILED, 'Failed'),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=128, db_index=True)
    content_object = GenericForeignKey()
    task = models.CharField(max_length=16, db_index=True, choices=TASKS)
    status = models.CharField(max_length=10, choices=STATUSES, db_index=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_queue')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskQueueQuerySet.as_manager()

    class Meta:
        unique_together = ('team', 'content_type', 'object_id', 'task')

    def clean(self):
        """
        define custom validation
        :return:
        """


class Environment(models.Model):
    """
        AWS EMR settings
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """
        define custom validation
        :return:
        """


class EnvironmentInstance(models.Model):
    DEV = 'dev'
    STAGING = 'staging'
    PROD = 'prod'

    STAGES = (
        (DEV, "Dev"),
        (STAGING, "Staging"),
        (PROD, "Prod")
    )

    sku = models.CharField(max_length=50, primary_key=True, help_text='Environment Instance SKU')
    stage = models.CharField(max_length=10, choices=STAGES)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='environment_instance')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku

    def clean(self):
        """
        define custom validation
        :return:
        """


class EMR(models.Model):
    PENDING = 'pending'
    RUNNING = 'running'
    TERMINATED = 'terminated'

    STATUSES = (
        (PENDING, "Pending"),
        (RUNNING, "Running"),
        (TERMINATED, "Terminated"),
    )

    status = models.CharField(max_length=10, choices=STATUSES, default=PENDING, db_index=True,
                              help_text='EMR Instance Status')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='emr')
    environment_instance = models.ForeignKey(EnvironmentInstance, on_delete=models.CASCADE, related_name='emr')

    task_queue = GenericRelation(TaskQueue)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.team.name}_{self.environment_instance.stage}_{self.status}'

    def clean(self):
        """
        define custom validation
        :return:
        """
