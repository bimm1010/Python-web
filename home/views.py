from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    myname = "Hoàng Nam"
    taisan1 = ["Điện thoại", "PC", "laptop"]
    trangthai = "Đã có vợ"
    context = {'name': myname, "taisan": taisan1, "trangthai": trangthai}
    return render(request, 'home/index.html', context)


def viewlist(request):
    list_question = Question.objects.all()
    context = {"quest": list_question}
    return render(request, 'home/question_list.html', context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    context = {"qs": q}
    return render(request, "home/detail_question.html", context)


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("lỗi ko có lựa chọn")
    c.vote = c.vote + 1
    c.save()
    return render(request, "home/result.html", {"q": q})
