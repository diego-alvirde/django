from django.shortcuts import render

# Create your views here.
def cart(request):
    #Crear una sesión
    #request.session['cart_id'] = '123'
    #Obtener valor de una sesión
    #valor = request.session.get('cart_id')    
    #Eliminar una sesión
    #request.session['cart_id'] = None

    return render(request, 'carts/carts.html', {

    })