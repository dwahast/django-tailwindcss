from django.shortcuts import render


def home_view(request):
    items = [
        {"title": "Faturas"},
        {"title": "Saldos e Limites"},
        {"title": "Cobrança", "has_child": True, "childs": [
            {"title": "Inadimplência"},
            {"title": "Pagamentos"}
            ]},
        {"title": "Campanhas"},
    ]
    context = {"items": items}
    return render(request, "pages/home.html", context)