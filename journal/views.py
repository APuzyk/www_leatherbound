# from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator
from .models import Entry
from datascience.calls import runEntryModels


class EntryList(generic.ListView):
    # queryset = Entry.objects.order_by("-created_on")
    template_name = "index.html"

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        return super(EntryList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Entry.objects.filter(
            author=self.request.user
            ).order_by("-created_on")


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = "entry_detail.html"

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        return super(EntryDetail, self).dispatch(*args, **kwargs)


class EntryCreate(generic.CreateView):
    model = Entry
    template_name = "entry_create.html"
    fields = ("title", "content")

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        return super(EntryCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        runEntryModels(self.object)
        return response


class EntryEdit(generic.UpdateView):
    model = Entry
    template_name = "entry_edit.html"
    fields = ("title", "content")

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user != self.get_object().author:
            raise Http404()
        return super(EntryEdit, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        runEntryModels(self.object)
        return response


class EntryDelete(generic.DeleteView):
    model = Entry
    template_name = "entry_delete.html"
    success_url = reverse_lazy("home")

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        if self.request.user != self.get_object().author:
            raise Http404()
        return super(EntryDelete, self).dispatch(*args, **kwargs)
