from django.http import HttpResponse
from django.shortcuts import render

message = ""


def index(request):
    return render(request, 'index.html')


def page1(request):
    context = {"a": 5, "b": "слово"}
    return render(request, "page1.html", context)


def page2(request):
    return HttpResponse("Это вторая страница сайта")


def page3(request):
    f1 = open("C:\Django\_files\_file01.txt", "r")
    txt01 = f1.readline()
    f1.close()
    return HttpResponse(f'''Число из файла {txt01}''')


def info(request):
    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", 'r')
    txt01 = f1.readline()
    f1.close()

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_vyruchka.txt", 'r')
    txt02 = f1.readline()
    f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    var = {'a': txt01, 'b': txt02, 'c': rezervuar_kolonka0, 'd': rezervuar_kolonka1, 'e': rezervuar_kolonka2,
           'f': rezervuar_kolonka3}
    return render(request, "info.html", var)


def vyv_info(request):
    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolonka_toplivo0.txt", 'r')
    txt01 = f1.readline()
    f1.close()
    return HttpResponse(f'''Колонка топлива №1: {txt01}''')


def testform(request):
    a = request.POST.get("number1", "1")
    kol_top = request.POST.getlist("number2")
    nomer_kolonki = request.POST.get("number3")
    kl_info = {'kl': a, 'kt': kol_top, 'nk': nomer_kolonki}
    return render(request, "kolonka_info.html", kl_info)


def zapravka(request):
    return render(request, "zapravka.html")


def zapravka_info(request):
    tsena_topliva = [55.9, 48.9, 54.2, 63.2]
    global message

    def zapravka_kolonka(file_path, rezervuar_kolonka):
        global message
        if rezervuar_kolonka[nvt] >= int(kt):
            rezervuar_kolonka[nvt] = rezervuar_kolonka[nvt] - int(kt)
            zapis_file(file_path, rezervuar_kolonka)
            vyruchka_zk = vyruchka + int(kt) * tsena_topliva[nvt]
            f1 = open("d:\\Dannye\_azs_mn_trk_graph\_vyruchka.txt", "w")
            f1.write(str(vyruchka_zk))
            f1.close()
            message = "Заправка произведена успешна"
        else:
            message = "Недостаточно топлива для заправки"

    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    def zapis_file(file_path, rezervuar_kolonka):
        f1 = open(file_path, "w")
        for i in range(4):
            f1.write(str(rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    nk = request.POST.get("nomer_kolonki")
    vt = request.POST.get("vid_topl")
    kt = request.POST.get("kol_topliva")

    if vt == "92":
        nvt = 0
    if vt == "95":
        nvt = 1
    if vt == "100":
        nvt = 2
    if vt == "ДТ":
        nvt = 3

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", 'r')
    kolvo_kolonok = f1.readline()
    f1.close()

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_vyruchka.txt", 'r')
    vyruchka = float(f1.readline())
    f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    if nk == "Колонка 1":
        zapravka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt", rezervuar_kolonka0)
    if nk == "Колонка 2":
        zapravka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt", rezervuar_kolonka1)
    if nk == "Колонка 3":
        zapravka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt", rezervuar_kolonka2)
    if nk == "Колонка 4":
        zapravka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt", rezervuar_kolonka3)

    zap = {'nom_kol': nk, 'vid_top': vt, 'kol_top': kt, 'nom_vid_top': nvt, "mess": message}
    return render(request, "zapravka_info.html", zap)


def popolnenie(request):
    return render(request, "popolnenie.html")


def popolnenie_info(request):
    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    def zapis_file(file_path, rezervuar_kolonka):
        f1 = open(file_path, "w")
        for i in range(4):
            f1.write(str(rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    nk = request.POST.get("nomer_kolonki")
    vt = request.POST.get("vid_topl")
    ds = request.POST.get("vid_deistvia")

    if vt == "92":
        nvt = 0
    if vt == "95":
        nvt = 1
    if vt == "100":
        nvt = 2
    if vt == "ДТ":
        nvt = 3

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", 'r')
    kolvo_kolonok = f1.readline()
    f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    if ds == "Залить резервуар полностью":
        if nk == "Колонка 1":
            rezervuar_kolonka0[nvt] = 5000
            zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt", rezervuar_kolonka0)
        if nk == "Колонка 2":
            rezervuar_kolonka1[nvt] = 5000
            zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt", rezervuar_kolonka1)
        if nk == "Колонка 3":
            rezervuar_kolonka2[nvt] = 5000
            zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt", rezervuar_kolonka2)
        if nk == "Колонка 4":
            rezervuar_kolonka3[nvt] = 5000
            zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt", rezervuar_kolonka3)
        message = "Резервуар залит полностью"
        zap = {'nom_kol': nk, 'vid_top': vt, 'kol_top': ds, 'nom_vid_top': nvt, "mess": message}
        return render(request, "popolnenie_info.html", zap)
    else:
        f1 = open("d:\\Dannye\_azs_mn_trk_graph\_popolnenie_prom.txt", "w")
        f1.write(str(nk))
        f1.write(",")
        f1.write(str(nvt))
        f1.close()
        zap = {'nom_kol': nk, 'vid_top': vt, 'kol_top': ds, 'nom_vid_top': nvt}
        return render(request, "popolnenie_prom.html", zap)

def popolnenie_prom(request):
    pass
    # return render(request, "popolnenie_prom.html")


def popolnenie_prom_info(request):
    global message

    def popolnenie_kolonka(file_path, rezervuar_kolonka):
        global message
        if rezervuar_kolonka[nvt] + kt > 5000:
            message = "Пополнение невозможно. Некорректное значение"
        else:
            rezervuar_kolonka[nvt] = rezervuar_kolonka[nvt] + kt
            zapis_file(file_path, rezervuar_kolonka)

    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    def zapis_file(file_path, rezervuar_kolonka):
        f1 = open(file_path, "w")
        for i in range(4):
            f1.write(str(rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    kt = int(request.POST.get("kol_topliva"))

    par_popolnenia = []
    f1 = open("d:\\Dannye\_azs_mn_trk_graph\_popolnenie_prom.txt", "r")
    b = f1.readline()
    f1.close()
    c = b.split(",")
    for i in c:
        ch = i
        par_popolnenia.append(ch)

    nk = par_popolnenia[0]
    nvt = int(par_popolnenia[1])
    message = "Пополнение произведено успешно"

    if nk == "Колонка 1":
        popolnenie_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt", rezervuar_kolonka0)
    if nk == "Колонка 2":
        popolnenie_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt", rezervuar_kolonka1)
    if nk == "Колонка 3":
        popolnenie_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt", rezervuar_kolonka2)
    if nk == "Колонка 4":
        popolnenie_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt", rezervuar_kolonka3)

    ppl = {'kol_ppl_top': kt, 'mess': message}
    return render(request, "popolnenie_prom_info.html", ppl)


def korrektirovka(request):
    return render(request, "korrektirovka.html")


def korrektirovka_info(request):
    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    def zapis_file(file_path, rezervuar_kolonka):
        f1 = open(file_path, "w")
        for i in range(4):
            f1.write(str(rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    ds = request.POST.get("vid_deistvia")

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", 'r')
    kolvo_kolonok = f1.readline()
    f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    message = "Выручка очищена"
    if ds == "Очистить выручку":
        f1 = open("D:\Dannye\_azs_mn_trk_graph\_vyruchka.txt", 'w')
        vyruchka = 0
        f1.write(str(vyruchka))
        f1.close()
        zap = {"mess": message}
        return render(request, "korrektirovka_info.html", zap)

    elif ds == "Очистить резервуары":
        rezervuar_kolonka = [0, 0, 0, 0]
        zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt", rezervuar_kolonka)
        zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt", rezervuar_kolonka)
        zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt", rezervuar_kolonka)
        zapis_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt", rezervuar_kolonka)
        message = "Резервуары очищены"
        zap = {"mess": message}
        return render(request, "korrektirovka_info.html", zap)

    else:
        return render(request, "korrektirovka_prom.html")


def korrektirovka_prom(request):
    pass
    # return render(request, "korrektirovka_prom.html")


def korrektirovka_prom_info(request):
    global message

    def korrektirovka_kolonka(file_path, rezervuar_kolonka):
        global message
        if int(kt) <= 5000:
            rezervuar_kolonka[nvt] = int(kt)
            zapis_file(file_path, rezervuar_kolonka)
            message = "Корректировка произведена успешно"
        else:
            message = "Некорректное значение"

    def get_rez_from_file(file_path):
        rezervuar_kolonka = []
        filename = file_path
        f1 = open(filename, "r")
        b = f1.readline()
        f1.close()
        c = b.split(" ")
        for i in c:
            ch = int(i)
            rezervuar_kolonka.append(ch)
        return rezervuar_kolonka

    def zapis_file(file_path, rezervuar_kolonka):
        f1 = open(file_path, "w")
        for i in range(4):
            f1.write(str(rezervuar_kolonka[i]))
            if i < 3:
                f1.write(" ")
        f1.close()

    nk = request.POST.get("nomer_kolonki")
    vt = request.POST.get("vid_topl")
    kt = request.POST.get("kol_topliva")

    if vt == "92":
        nvt = 0
    if vt == "95":
        nvt = 1
    if vt == "100":
        nvt = 2
    if vt == "ДТ":
        nvt = 3

    f1 = open("D:\Dannye\_azs_mn_trk_graph\_kolvo_kolonok.txt", 'r')
    kolvo_kolonok = f1.readline()
    f1.close()

    rezervuar_kolonka0 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt")
    rezervuar_kolonka1 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt")
    rezervuar_kolonka2 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt")
    rezervuar_kolonka3 = get_rez_from_file("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt")

    if nk == "Колонка 1":
        korrektirovka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar0.txt", rezervuar_kolonka0)
    if nk == "Колонка 2":
        korrektirovka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar1.txt", rezervuar_kolonka1)
    if nk == "Колонка 3":
        korrektirovka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar2.txt", rezervuar_kolonka2)
    if nk == "Колонка 4":
        korrektirovka_kolonka("d:\\Dannye\_azs_mn_trk_graph\_rezervuar3.txt", rezervuar_kolonka3)

    zap = {'nom_kol': nk, 'vid_top': vt, 'kol_top': kt, 'nom_vid_top': nvt, "mess": message}
    return render(request, "korrektirovka_prom_info.html", zap)
