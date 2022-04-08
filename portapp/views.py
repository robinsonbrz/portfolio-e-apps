from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, 'portapp/index.html')


def about(request):
    return render(request, 'portapp/about.html')


def expertise(request):
    return render(request, 'portapp/expertise.html')


def portfolio(request):
    return render(request, 'portapp/portfolio.html')


def contato(request):
    return render(request, 'portapp/contato.html')


def enviaemail(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]
    print(name, email, subject, message)
    return HttpResponse('OK')









    
"""     if request.method == 'POST':
        print("Post\n\n\n\n\n\n")
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        ) """
