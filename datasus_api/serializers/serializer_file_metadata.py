from rest_framework import serializers
from ..models.cnes.lt import LTCnes
from ..models.cnes.pf import PFCnes
from ..models.file_metadata import FileMetadata


class FileMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileMetadata
        fields = ['filename', 'insertion_timestamp']