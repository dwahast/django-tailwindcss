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

def folder_view(request):
    # mapping_tree_folder = {}
    guideline = Guideline.objects.get(title="Processadora Guideline")
    items = mapping_folders(guideline.folder)
    print(items)
    
    if request.htmx:
        html_markdown = {
            "text": "# Eita. HTMX! ",
            "title": "Hello World"
        }
        context = {"items": items, "doc": html_markdown}
        return render(request, "pages/home.html#document-content", context)
    else:
        
        html_markdown = {
            "text": "# Visão Geral",
            "title": "Adicionar uma nova tabela indicando qual documento é o principal"
        }
        # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
        context = {"items": items[0]["children"], "doc": html_markdown}
        return render(request, "pages/home.html", context)
    
def document_view(request):
    context = {}
    return render(request, "pages/home.html", context)