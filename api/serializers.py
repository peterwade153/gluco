from rest_framework import serializers

from api.models import GlucoseLevel


class GlucoseLevelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = GlucoseLevel
        fields = '__all__'

