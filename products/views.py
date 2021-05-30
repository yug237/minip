from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    DeleteView
)
from .models import compP

class PostDetailView(DetailView):
    model = compP

class ProdDetailView(DetailView):
    model = compP
    template_name = 'products/detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = compP
    fields = ['Pcomp', 'Pname', 'Pdesc','Pprice', 'Pimage']

    def form_valid(self, form):
        form.instance.Pemp = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = compP
    success_url = '/home1'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.Pemp:
            return True
        return False


def detail(request):
	context={

		'products'
	}

def home1(request):
	context={

		'products' : compP.objects.all()

	}
	return render(request, 'products/home1.html', context)

def home(request):
	context={

		'products' : compP.objects.all()

	}
	return render(request, 'products/home.html', context)


def landing(request):

	return render(request, 'products/landing.html')

def common(request):

	return render(request, 'products/common.html')

