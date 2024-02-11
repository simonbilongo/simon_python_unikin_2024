from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def template_publier_article(request):
# Vue pour afficher la page publier_article.html
    # nombre1 = 2
    # print(type(nombre1))
    # nombre2= 3.3
    # print(type(nombre2))
    # nom="fiston"
    # print(type(nom))
    # niveau = [1, 2, 3]
    # print(type(niveau))
    # etudiant = {"nom":"simon", "age":22, "niveau":"L1"}
    # print(type(etudiant)) 
    # print(etudiant['nom'])
    articles = Article.objects.filter(compte=request.user).order_by('-id')
    if request.method == 'POST':
        titre_post = request.POST.get('titre')
        contenu_post = request.POST.get('contenu')
        Article.objects.create(
            titre = titre_post,
            contenu = contenu_post,
            compte = request.user
        )
        return redirect('publier_article')
    return render(request, 'publier_article.html', {"articles":articles})

def template_afficher_article(request):
# Vue pour afficher la page afficher_article.html
    articles = Article.objects.all().order_by('-id')
    return render(request, 'afficher_article.html', {"articles":articles})

def template_creer_compte(request):
    if request.method == 'POST':
        # Récupérations des données saisies au niveau du formulaire de création de compte
        #Personne
        nom_post = request.POST.get('nom')
        postnom_post = request.POST.get('postnom')
        prenom_post = request.POST.get('prenom')
        sexe_post = request.POST.get('sexe')
        telephone_post = request.POST.get('telephone')
        profession_post = request.POST.get('profession')
        date_naissance_post = request.POST.get('date_naissance')
        lieu_naissance_post = request.POST.get('lieu_naissance')
        #ROle
        role_post = request.POST.get('role')
        #Compte
        username_post = request.POST.get('username')
        mot_de_passe_post = mot_de_passe_post = request.POST.get('mot_de_passe')
        email_post = request.POST.get('email')
        # Enregistrement de ces données dans la bdd
        personne_created = Personne.objects.create(
            nom = nom_post,
            postnom = postnom_post,
            prenom = prenom_post,
            sexe = sexe_post,
            telephone = telephone_post,
            profession = profession_post,
            date_naissance = date_naissance_post,
            lieu_naissance = lieu_naissance_post,
        )   
        compte_created =Compte.objects.create(
            username = username_post,
            password = mot_de_passe_post,
            email = email_post,
            personne = personne_created,
        )   
        compte_created.set_password(compte_created.password)
        compte_created.save()
        role_created, created = Role.objects.get_or_create(
            libelle = role_post
        )
        #Ajout du role dans le compte de l'utilisateur
        compte_created.role.add(role_created)
        compte_created.save()
        # Personne.objects.filter().a.delele()
        return redirect('se_connecter')
    else:
        return render(request, 'creer_compte.html')

def template_se_connecter(request):
    if request.method == 'POST':
        username_post = request.POST.get('username')
        mot_de_passe_post = request.POST.get('mot_de_passe')
        compte = authenticate(request, username = username_post, password = mot_de_passe_post)
        print(compte, username_post, mot_de_passe_post)
        if compte is not None:
            login(request, compte)
            return redirect('afficher_article')
            
    return render(request, 'seconnecter.html')

def commenter(request):
    pk=request.GET.get('pk')
    article = Article.objects.get(pk=pk)
    commentaires = Commentaire.objects.all().order_by('-id')
    if request.method == 'POST':
        description_post = request.POST.get('description')
        Commentaire.objects.create(
            description = description_post,
            article = article,
            compte = request.user
        )
        return redirect(f'/commenter?pk={pk}') 
    return render(request, 'commenter.html', {"article":article, "commentaires":commentaires})

def se_deconnecter(request):
    logout(request)
    return redirect('se_connecter')


def somme(a, b):
    som = a+b
    return som

#``