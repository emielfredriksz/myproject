from rest_framework.response import Response
from django.template.response import TemplateResponse
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.viewsets import GenericViewSet
from rest_framework.reverse import reverse
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from django_filters import rest_framework as filters
import django_filters
from .sentiment import GetSentiment
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'reviews': reverse('review-list', request=request, format=format)
    })

class ReviewFilter(django_filters.FilterSet):
    neg = filters.NumberFilter(field_name="neg", lookup_expr='gte')
    neu = filters.NumberFilter(field_name="neu", lookup_expr='gte')
    pos = filters.NumberFilter(field_name="pos", lookup_expr='gte')
    comp = filters.NumberFilter(field_name="comp", lookup_expr='gte')

    class Meta:
        model = Review
        fields = ['neg', 'neu', 'pos', 'comp']

class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ReviewFilter

    def sentiment(self, request, *args, **kwargs):
        renderer_classes = [TemplateHTMLRenderer]
        review = self.get_object()
        serializer = ReviewSerializer(review, context={'request':request})
        return Response(GetSentiment(review.text)+ f"<a href={serializer.data['url']}>Back to Review</a>")

