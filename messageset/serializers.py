# coding=utf-8
from rest_framework import serializers
from lteadmin import utils
from .models import Task, Notification, SiteMail, ReadStatus

__author__ = 'lyhapple'


class SiteMailSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    status = serializers.SerializerMethodField()
    status_value = serializers.IntegerField(source='status')
    sender_avatar = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_sender_avatar(self, obj):
        return obj.sender.staff_of.avatar.url

    class Meta:
        model = SiteMail
        fields = SiteMail.Config.list_display_fields + (
            'sender_avatar', 'status_value'
        )
        read_only_fields = (
            'id', 'send_time', 'sender_avatar', 'status_value'
        )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            'id', 'title', 'contents', 'status', 'read_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at'
        )


class TaskSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_percent(self, obj):
        return '%s%%' % obj.percent

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'percent', 'start_app', 'status',
            'start_time', 'end_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at', 'status'
        )