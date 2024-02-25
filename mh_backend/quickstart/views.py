from django.shortcuts import render
from rest_framework import viewsets

from quickstart.models import Branch
from quickstart.serializers import BranchSerializer

# Create your views here.
class BranchViewSet(viewsets.ReadOnlyModelViewSet):
    """"""
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
