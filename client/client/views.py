from django.shortcuts import render
from django.http import HttpResponse
from .models import User_Info


def index(request):
	if request.method == 'POST':
		Name = request.POST['Name']
		LName = request.POST['LName']
		Fonction = request.POST['Fonction']
		Profil = request.FILES['imgInp']
		Adresse = request.POST['Adresse']
		Naissance = request.POST['Date']
		Lieu = request.POST['Lieu']
		Commune = request.POST['Commune']
		Departement = request.POST['Departement']
		Sexe = request.POST['Sexe']
		Statut = request.POST['Statut']
		Dependant = request.POST['Dependant']
		Telephone_1 = request.POST['Telephone_1']
		Telephone_2 = request.POST['Telephone_2']
		Email = request.POST['email']

		user = User_Info(Name=Name, 
			LName=LName, 
			Fonction=Fonction, 
			Profil=Profil,
			Adresse=Adresse,
			Naissance=Naissance,
			Lieu=Lieu,
			Commune=Commune,
			Departement=Departement,
			Sexe=Sexe,
			Statut=Statut,
			Dependant=Dependant,
			Telephone_1=Telephone_1,
			Telephone_2=Telephone_2,
			Email=Email
			)

		user.save()
	count = User_Info.objects.count()
	user_list = User_Info.objects.all()
	return render(request, 'index.html', {'count': count, 'user_list': user_list})
