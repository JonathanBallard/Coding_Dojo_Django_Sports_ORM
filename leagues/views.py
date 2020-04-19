from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"baseball": League.objects.filter(sport="Baseball"),
		"womens": League.objects.filter(name__startswith="Women's"),
		"hockey": League.objects.filter(sport__contains="Hockey"),
		"not_football": League.objects.exclude(sport="Football"),
		"conferences": League.objects.filter(name__icontains="Conferences"),
		"atlantic": League.objects.filter(name__icontains="Atlantic"),
		"teams": Team.objects.all(),
		"dallas": Team.objects.filter(location="Dallas"),
		"raptors": Team.objects.filter(team_name="Raptors"),
		"city": Team.objects.filter(location__icontains="City"),
		"t_teams": Team.objects.filter(team_name__startwith="T"),
		"all_teams_alph": Team.objects.all().order_by('location'),
		"all_teams_alph_desc": Team.objects.all().order_by('-team_name'),
		"players": Player.objects.all(),
		"cooper": Player.objects.filter(last_name="Cooper"),
		"joshua": Player.objects.filter(first_name="Joshua"),
		"cooper_not_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_or_wyatt": Player.objects.filter(
			Q(first_name="Alexander") | Q(first_name = "Wyatt")
		),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")