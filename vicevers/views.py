from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def user(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    count_words = len((user_text).split())
    print(count_words)
    return render(request,'user.html',{'usertext':user_text,
                                       'reverse':reverse_text,
                                       'countwords': count_words})