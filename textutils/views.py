# I have created this file - Mayank

from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    capitalizefirst = request.POST.get('capitalizefirst', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charactercount = request.POST.get('charactercount', 'off')

    purpose = []
    # analyzed = djtext
    if removepunc == 'on':
        purpose.append('Remove Punctuations')
        p_list = '''/[-[\]{}()*+?.,\\^$|#\]/,;'"\\$&"'''
        analyzed = ""
        for i in djtext:
            if i not in p_list:
                analyzed+= i
        djtext = analyzed

    if capitalizefirst == "on":
        purpose.append('Capitalize')
        analyzed = ""
        for i in djtext:
            analyzed+=i.upper()
        djtext = analyzed


    if newlineremove == "on":
        purpose.append('Remove New Line')
        analyzed = ""
        for i in djtext:
            if i != "\n" and i!= '\r':
                analyzed += i
        djtext = analyzed


    if spaceremove == "on":
        purpose.append('Space Remover')
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] ==" ":
                pass
            else:
                analyzed += char

        djtext = analyzed


    if charactercount == "on":
        purpose.append('Character Count')
        count1 = 0
        for i in djtext:
                count1 +=1
        analyzed = f"Number of characters: {count1}\n{djtext}"

    ki = str(purpose).translate("[],\'")

    if charactercount != 'on' and removepunc!= 'on' and spaceremove != 'on' and newlineremove != 'on' and capitalizefirst != 'on' :
        return HttpResponse('ERROR')

    else:
        params = {'purpose': ki, 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


def navigation(request):
    return render(request, 'nav.html')



# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('Remove Punctuation')
#
# def capitalizefirst(request):
#     return HttpResponse('capitalize First')
#
# def newlineremove(request):
#     return HttpResponse('Remove New Line')
#
# def spaceremove(request):
#     return HttpResponse('Remove Space')
#
# def charactercount(request):
#     return HttpResponse('Count Characters')

