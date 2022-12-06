from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


class ListView(TemplateView):
    model = None
    context_key = 'object'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex[self.context_key] = self.get_objects()
        return contex

    def get_objects(self):
        return self.model.objects.all()
class FormView(View):
    template_name = None
    form_class = None
    redirect_url = ''

    def get_context_data(self, **kwargs):
        return kwargs

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context)

class DetailView(TemplateView):
    context_key = 'object'
    model = None
    key_kwarg = 'pk'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_object()
        return context


    def get_object(self):
        pk = self.kwargs.get(self.key_kwarg)
        return get_object_or_404(self.model, pk=pk)

class CreateView(View):

    form_class = None

    template_name = None

    model = None

    redirect_url = None

    def get(self, request, *args, **kwargs):

        form = self.form_class()

        context = {'form': form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():

            return self.form_valid(form)

        else:

            return self.form_invalid(form)

    def form_valid(self, form):

        self.object = form.save()

        return redirect(self.get_redirect_url())

    def form_invalid(self, form):

        context = {'form': form}

        return render(self.request, self.template_name, context)

    def get_redirect_url(self):

        return self.redirect_url