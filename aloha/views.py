from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger

from aloha.models import Product
from forms import RegisterForm


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def table(request):
    return render(request, 'tables.html')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")


@login_required
@csrf_protect
def search(request):
    if 'query' in request.GET and request.GET['query']:
        # query = request.GET.get("query")
        page = request.GET.get("page")
        page_size = 3
        # product_id = "0012" + query + "123123"
        # product_name = "aha" + query + "thisis a product name"
        # Product.objects.create(
        #     product_id=product_id,
        #     product_name=product_name,
        #     large_category="big category",
        #     medium_category="mid category",
        #     small_category="detail category",
        #     production_company="GATAJAVA Co Ltc",
        #     product_line="Internet",
        #     retail_price=12,
        #     inbound_price=6
        # )
        products = Product.objects.filter(product_name__icontains='ha')
        # try:
        #     products = paginator.page(page)
        # except PageNotAnInteger:
        #     products = paginator.page(1)
        try:
            page = int(page)
        except TypeError:
            page = 0
        start_line_num = (page - 1) * page_size
        return render_to_response('tables.html',
                                  {
                                      'products': products,
                                      'start_line_num': start_line_num,
                                      'page_size': page_size,
                                      'request': request
                                  })


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('blog_index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)
