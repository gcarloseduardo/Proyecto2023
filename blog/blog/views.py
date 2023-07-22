from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def nosotros(request):
    return render(request,'nosotros.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         print("ESTO ES EL CORREO INGRESADO POR EL USUARIO", email)
#         print("ESTO ES LA CONTRASEÑA", password)

#     return render(request, 'usuarios/login.html')
