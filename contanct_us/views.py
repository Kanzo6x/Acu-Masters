from django.shortcuts import render
from .models import members
def show_cards(request):
    if request.method == "GET":
        team_codes = {
            1:'technical',
            2:'marketing',
            3:'human resources',
            4:'PR & FR',
            5:'operation',
            6:'High Board',
            }
        headings = members.objects.filter(is_heading = True)
        teams = []
        for i in range(1, 6 , 1):
            query = members.objects.filter(team_code=i).exclude(id__in=headings.values_list('id', flat=True))
            if query:
                for member in query:
                    member.team_name = team_codes.get(member.team_code , "Teams")
                teams.append(query)
        return render(request , 'contanct_us/contactus.html' , {'headings':headings , 'teams':teams , 'team_codes':team_codes})
    
        
        
