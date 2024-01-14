from django.shortcuts import render
from django.db import models
from .models import Guideline, Folder, Document

def mapping_folders(folder):
    mapping_folder = []
        
    mapping_folder.append({
        "title": folder.title,
        "has_child": True if len(folder.children.all()) != 0 else False,
        "children": [],
    })
    
    if mapping_folder[0]["has_child"]:
        for child in folder.children.all():
            level1 = {
                "title": child.title,
                "has_child": True if len(child.children.all()) != 0 else False,
                "children": [],
            }
            if level1["has_child"]:
                for child2 in child.children.all():
                    level2 = {
                        "title": child2.title,
                        "has_child": False,
                        "children": [],
                        "document": child2.document.id
                    }
                    level1["children"].append(level2)

            mapping_folder[0]["children"].append(level1)
    
    return mapping_folder

def documents_view(request):
    guideline = Guideline.objects.get(title="Processadora Guideline")
    items = mapping_folders(guideline.folder)
    if request.htmx:
        html_markdown = Document.objects.get(id=1)
        context = {"items": items[0]["children"], "doc": html_markdown}
        return render(request, "pages/guides.html#document-content", context)
    else:
        html_markdown = {
            "text": "# Visão Geral",
            "title": "Adicionar uma nova tabela indicando qual documento é o principal"
        }
        # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
        context = {"items": items[0]["children"], "doc": html_markdown}
        return render(request, "pages/guides.html", context)
    
def document_view(request, documentId):
    guideline = Guideline.objects.get(title="Processadora Guideline")
    items = mapping_folders(guideline.folder)
    if request.htmx:
        html_markdown = {
            "text": Document.objects.get(id=documentId).content,
            "title": "Colchão"
        }
        print(html_markdown)
        context = {"items": items[0]["children"], "doc": html_markdown}
        return render(request, "pages/guides.html#document-content", context)
    else:
        html_markdown = {
            "text": "# Visão Geral",
            "title": "Adicionar uma nova tabela indicando qual documento é o principal"
        }
        # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
        context = {"items": items[0]["children"], "doc": html_markdown}
    return render(request, "pages/guides.html", context)