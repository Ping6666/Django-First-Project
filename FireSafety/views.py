from django.shortcuts import render, get_object_or_404
from django.views.generic import (DetailView, View)

# Create your views here.
from .models import firesafetyDataset


class firesafetyDetailView(DetailView):
    template_name = 'firesafety_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(firesafetyDataset, id=id_)


class firesafetySearchListView(View):
    template_name = 'firesafety_list.html'
    queryset = firesafetyDataset.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        search_str_ = self.request.POST.get('search_')
        if not search_str_:
            context = {'object_list': None, 'search_result': search_str_}
        else:
            context = {
                'object_list':
                self.get_queryset().filter(
                    place_name__contains=search_str_).union(
                        self.get_queryset().filter(
                            place_address__contains=search_str_),
                        self.get_queryset().filter(
                            violate_name__contains=search_str_),
                        self.get_queryset().filter(
                            place_purpose__contains=search_str_),
                    ),
                'search_result':
                search_str_
            }
        return render(request, self.template_name, context)
