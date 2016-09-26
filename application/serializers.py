from rest_framework import serializers

from events.serializers import EventSerializer
from application.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Application

        fields = (
            'id',
            'event',
            'mail',
            'first_name',
            'last_name',
            'sur_name',
            'user_info',
            'job',
            'user_image',
            'info_source',
            'created_at',
            'is_accepted'
            )
        read_only_fields = ('id',)

        # def create(self, validated_data):
        #     return Application.objects.create(**validated_data)

        def get_validation_exclusions(self, *args, **kwargs):
            exclusions = super(ApplicationSerializer, self).get_validation_exclusions()

            return exclusions + ['event']
