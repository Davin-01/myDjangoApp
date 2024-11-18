from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item
from .forms import ItemForm


# Create Item (Already implemented)
def create_item(request):
    if request.method == 'POST':
        form = ItemForm()
        if form.is_valid():
            form.save()
            messages.success(request, "Item created successfully!")
            return redirect('landing')
        else:
            return render(request, 'myapp/create_item.html', {'form': form})

    form = ItemForm()
    return render(request, 'myapp/create_item.html', {'form': form})


# Read Item Details
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'myapp/item_detail.html', {'item': item})


# Update Item
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm()
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully!")
            return redirect('landing')
        else:
            return render(request, 'myapp/update_item.html', {'form': form, 'item': item})

    form = ItemForm()
    return render(request, 'myapp/update_item.html', {'form': form, 'item': item})


# Delete Item
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully!")
        return redirect('landing')

    return render(request, 'myapp/delete_item.html', {'item': item})


def landing(request):
    items = Item.objects.all()
    print(items)
    return render(request, 'landing.html', {'items': items})


def register_user(request):
    return None


def login_user(request):
    return None


def logout_user(request):
    return None