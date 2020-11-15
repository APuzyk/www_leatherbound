# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .serializers import EntrySerializer
from .models import Entry
from datascience.calls import runEntryModels
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'entries': reverse('entry-list', request=request, format=format)
    })
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(author=user)


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    permission_classes = [IsOwner, IsAuthenticated]
    serializer_class = EntrySerializer
    lookup_field = 'uuid'



# class ListEntries(APIView):
#     def get(self, request, format=None):


# class EntryDetail(generic.DetailView):
#     model = Entry
#     template_name = "entry_detail.html"

#     @method_decorator(login_required(login_url="login"))
#     def dispatch(self, *args, **kwargs):
#         return super(EntryDetail, self).dispatch(*args, **kwargs)


# class EntryDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Entry.objects.get(pk=pk)
#         except Entry.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         entry = self.get_object(pk)
#         serializer = EntrySerializer(entry)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         entry = self.get_object(pk)
#         serializer = EntrySerializer(entry, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         entry = self.get_object(pk)
#         entry.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class EntryCreate(generic.CreateView):
#     model = Entry
#     template_name = "entry_create.html"
#     fields = ("title", "content")

#     @method_decorator(login_required(login_url="login"))
#     def dispatch(self, *args, **kwargs):
#         return super(EntryCreate, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         response = super().form_valid(form)
#         runEntryModels(self.object)
#         return response


# class EntryEdit(generic.UpdateView):
#     model = Entry
#     template_name = "entry_edit.html"
#     fields = ("title", "content")

#     @method_decorator(login_required(login_url="login"))
#     def dispatch(self, *args, **kwargs):
#         if self.request.user != self.get_object().author:
#             raise Http404()
#         return super(EntryEdit, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         response = super().form_valid(form)
#         runEntryModels(self.object)
#         return response


# class EntryDelete(generic.DeleteView):
#     model = Entry
#     template_name = "entry_delete.html"
#     success_url = reverse_lazy("home")

#     @method_decorator(login_required(login_url="login"))
#     def dispatch(self, *args, **kwargs):
#         if self.request.user != self.get_object().author:
#             raise Http404()
#         return super(EntryDelete, self).dispatch(*args, **kwargs)
