from django.shortcuts import render


def home(requtst):
	return render(requtst, 'products/home.html')
