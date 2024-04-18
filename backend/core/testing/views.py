from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from testing.models import Test, CompletedTest
from testing.serializers import TestListSerializer, TestSerializer, CompletedTestSerializer, UserSerializer
from django.views.generic import View
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.db.models import Exists, OuterRef



class TestViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Test.objects.all()
    serializer_class = TestListSerializer

    def list(self, request):
        user = request.user
        queryset = self.get_queryset()
        queryset = queryset.annotate(
            completed=Exists(
                CompletedTest.objects.filter(
                    user=user, 
                    test=OuterRef('pk')
                )
            )
        )
        serializer = TestListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        test = get_object_or_404(Test, pk=pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

class CompleteTestView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        test = get_object_or_404(Test, id=pk)
        user = request.user
        score = request.data.get('score')
        
        completed_test = CompletedTest.objects.create(
            user=user,
            test=test,
            score=score
        )

        return Response(CompletedTestSerializer(completed_test).data, status=201)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)



