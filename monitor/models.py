from django.db import models



class Store(models.Model):

    store_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=20)


class StoreMenuHours(models.Model):

    store_id = models.IntegerField(primary_key=True)
    dayOfWeek = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()


class StoreTimeZone(models.Model):

    store_id = models.IntegerField(primary_key=True)
    timezone_str = models.CharField(max_length=30)
    