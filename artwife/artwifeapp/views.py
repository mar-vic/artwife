from django.shortcuts import render


def index(request):
    # template = loader.get_template("artwifeapp/index.html")
    # return HttpResponse(template.render({}, request))
    return render(request, "artwifeapp/index.html", {})
