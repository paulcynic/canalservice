from django.shortcuts import render
from .models import Order


def index(request):
    items = Order.objects.all()
    return render(request, 'canal/index.html', {'items':items})


# def add_and_save(request):
#     if request.method == 'POST':
#         bbf = BbForm(request.POST)
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#         else:
#             context = {'form': bbf}
#             return render(request, 'bboard/create.html', context)
#     else:
#         bbf = BbForm()
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)

