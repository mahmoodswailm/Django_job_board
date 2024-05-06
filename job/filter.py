import django_filters
from .models import Job

# filter
class JobFilter(django_filters.FilterSet):
    Description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields= ["title","job_type","Description","experience","category"]
        
