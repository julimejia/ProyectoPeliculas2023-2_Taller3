from django.shortcuts import render
from django.http import HttpResponse
 # Asegúrate de que esta importación esté configurada correctamente

def recomendacion(request):
    if request.method == 'POST':
        search_movie = request.POST.get('searchMovie', '')  # Obtiene el valor del campo 'searchMovie' del formulario

        # Llama a la función rec con los datos del formulario
        #resultado = rec.recomendar(search_movie)

        # Puedes hacer algo con el resultado, como mostrarlo en la plantilla o procesarlo de alguna otra manera
        return render(request, 'resultado.html', {'resultado': resultado})
    else:
        # Maneja el caso en el que no se ha enviado el formulario
        return render(request, 'reco.html')
