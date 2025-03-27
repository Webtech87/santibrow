from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def index(request):
	form = ContactForm()
	context = {
		'title': 'SantiBrow',
		'form': form,
	}
	return render(request, 'index.html', context)