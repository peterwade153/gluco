from rest_framework import serializers

from api.models import GlucoseLevel


class GlucoseLevelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = GlucoseLevel
        read_only_fields = ['id', 'gerätezeitstempel']
        fields = read_only_fields + ['user_id', 'seriennummer', 'aufzeichnungstyp','glukosewert_verlauf','glukose_scan']

        extra_kwargs = {'user_id': {'required': True,'allow_blank': False}}
        extra_kwargs = {'seriennummer': {'required': True}}
        extra_kwargs = {'aufzeichnungstyp': {'required': True}}
        extra_kwargs = {'glukosewert_verlauf': {'required': True}}
        extra_kwargs = {'glukose_scan': {'required': True}}


    def create(self, validated_data):
        reading = GlucoseLevel.objects.create(**validated_data)
        return reading
