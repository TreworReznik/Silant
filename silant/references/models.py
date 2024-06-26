from django.db import models
from django.urls import reverse

from accounts.models import Profile

'''Справочники'''


class ModelTechnique(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модель техники'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('model_technique_list')


class EngineModel(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Двигатели'
        verbose_name_plural = 'Двигатели'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('engine_model_list')


class TransmissionModel(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модель трансмиссии'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('transmission_model_list')


class ModelDriveBridge(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модель ведущего моста'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('model_drive_bridge_list')


class ControlledBridgeModel(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модель управляемого моста'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('controlled_bridge_model_list')


class TypeMaintenance(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('type_maintenance_list')


class FailureNode(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узел отказа'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('failure_node_list')


class RecoveryMethod(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способ восстановления'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('recovery_method_list')


class ServiceCompany(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.PROTECT, verbose_name='Профиль сервисной компании ')
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Сервисные компании'
        verbose_name_plural = 'Сервисные компании'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('service_company_list')


class OrganizationMaintenance(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Организация, проводившая ТО'
        verbose_name_plural = 'Организация, проводившая ТО'

    def __str__(self):
        return f'{self.title} {self.description}'

    def get_absolute_url(self):
        return reverse('organization_maintenance_list')

