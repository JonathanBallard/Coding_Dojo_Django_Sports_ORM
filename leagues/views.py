from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

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

		# Assignment 2
		"atlantic_soccer_conference" : Team.objects.filter(league="Atlantic Soccer Conference"),
		"penguin_players" : Player.objects.filter(curr_team="Boston Penguins"),
		"icbc_players" : Player.objects.filter(curr_team__league="International Collegiate Baseball Conference"),
		"lopez_acaf_players" : Player.objects.filter(curr_team__league="American Conference of Amateur Football", last_name="Lopez"),
		"football_players" : Player.objects.filter(curr_team__league__sport="Football"),
		"sophia_teams" : Team.objects.filter(curr_players__first_name="Sophia"),
		"sophia_leagues" : League.objects.filter(teams__curr_players__first_name="Sophia"),
		"florez_no_washington" : Player.objects.filter(last_name="Florez").exclude(curr_team="Washington Roughriders"),
		"sam_evans_teams" : Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		"tigercat_players" : Player.objects.filter(all_teams__team_name="Manitoba Tiger-Cats"),
		"past_vikings_players" : Player.objects.filter(all_teams__team_name="Wichita Vikings").exclude(curr_team__team_name="Wichita Vikings"),
		"jacob_grey_teams" : Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Oregon Colts"),
		"joshuas_in_afabp" : Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		"teams_with_12_players" : Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
		"all_players_and_team_count_sorted" : Player.objects.all().annotate(num_teams=Count('all_teams')).order_by('num_teams'),







	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")