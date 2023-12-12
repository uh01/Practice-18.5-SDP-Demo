from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required


@login_required
def add_category(request):
    category_form = forms.CategoryForm()
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
        else:
            category_form = forms.CategoryForm()

    return render(request, 'categories/add_category.html', {'form2': category_form})

# @login_required
# def add_category(request):
#     if request.method == 'POST':
#         category_form = forms.CategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.instance.author = request.user
#             category_form.save()
#             return redirect('add_post')
#     else:
#       category_form = forms.CategoryForm()

#     return render(request, 'categories/add_category.html', {'form2': category_form})
