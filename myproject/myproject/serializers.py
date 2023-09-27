from rest_framework import serializers
from rest_framework.fields import empty
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='review-detail')
    sentiment = serializers.HyperlinkedIdentityField(view_name='review-sentiment')

    class Meta:
        model = Review
        read_only_fields =('url', 'neg', 'neu', 'pos', 'comp', 'sentiment')
        fields = ['id', 'url', 'text', 'neg', 'neu', 'pos', 'comp', 'sentiment']