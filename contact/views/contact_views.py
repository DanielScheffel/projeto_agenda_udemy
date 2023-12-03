from django.shortcuts import render
from contact.models import Contact

# \ para não deixar a linha ficar muito estença

def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .all().order_by('-id')[:10]
    
    # print(contacts.query)
    
    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )