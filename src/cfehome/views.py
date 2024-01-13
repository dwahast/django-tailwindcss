from django.shortcuts import render


def home_view(request):
     
    print("Fui chamado")
    if request.htmx:
        html_markdown = {
            "text": "#FUNCIONAAAAA",
            "title": "Hello World"
        }
        context = {"doc": html_markdown}
        return render(request, "pages/home.html#document-content", context)
    else:
        items = [
            {
                "title": "Faturas"
            },
            {
                "title": "Saldos e Limites"
            },
            {
                "title": "Cobrança",
                "has_child": True,
                "childs": [
                    {"title": "Inadimplência", "link": "/defaulter"},
                    {"title": "Pagamentos", "link": "/payment"}
                ]
            },
            {
                "title": "Campanhas",
            },
        ]
        
        html_markdown = {
            "text": "#Teste String\n##Segundo Titulo",
            "title": "Hello World"
        }
        context = {"items": items, "doc": html_markdown}
        return render(request, "pages/home.html", context)