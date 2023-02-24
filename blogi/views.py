from django.shortcuts import render

from.models import Postaus


# Create your views here.
def postaukset(request):
    postaukset = Postaus.objects.all()  
    context = {'postaukset': postaukset}
    return render(                      # Rivit 10-14 voisi kaikki olla samalla rivillä
        request, 
        'blogi/postauslista.html',
        context,
    )

def nayta_postaus(request, id):
    return render(request, 'blogi/postaus.html')

    
