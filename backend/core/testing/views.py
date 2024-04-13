from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from testing.models import Test, CompletedTest
from testing.serializers import TestListSerializer, TestSerializer, CompletedTestSerializer
from django.views.generic import View
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


class TestViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Test.objects.all()
    serializer_class = TestListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TestListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        test = get_object_or_404(Test, pk=pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)


class CompleteTestView(View):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        test = get_object_or_404(Test, id=pk)
        user = request.user
        score = request.POST.get('score')
        if not score.isnumeric():
            return HttpResponseBadRequest()

        CompletedTest.objects.create(
            user=user,
            test=test,
            score=score
        )

        return HttpResponse('OK')


class CompletedTestView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Test.objects.all()
    serializer_class = CompletedTestSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompletedTestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        test = get_object_or_404(Test, pk=pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)
