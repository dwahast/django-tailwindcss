from django.shortcuts import render

# from django.db import models
from .models import Guideline, Folder, Document
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


def mapping_folders(folders):
    folder_list = []
    for folder in folders:
        print(f"[{folder.title}]")
        current_folder_documents = []
        folder_documents = Document.objects.filter(parent=folder.id)
        for document in folder_documents:
            current_folder_documents.append(document)

        folder_list.append(
            {"title": folder.title, "documents": current_folder_documents}
        )
    return folder_list


# def documents_view(request):
#     guideline = Guideline.objects.get(title="Processadora Guideline")
#     items = mapping_folders(guideline.folder)
#     if request.htmx:
#         html_markdown = Document.objects.get(id=1)
#         context = {"items": items[0]["children"], "doc": html_markdown}
#         return render(request, "pages/guides.html#document-content", context)
#     else:
#         html_markdown = {
#             "text": "# Visão Geral",
#             "title": "Adicionar uma nova tabela indicando qual documento é o principal"
#         }
#         # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
#         context = {"items": items[0]["children"], "doc": html_markdown}
#         return render(request, "pages/guides.html", context)


def guidelines_view(request):
    guidelines = Guideline.objects.all()
    context = {"guidelines": guidelines}
    print(guidelines)
    return render(request, "pages/guides.html", context)


def guide_view(request, guide):
    guideline = Guideline.objects.get(title=guide)

    guideline_folders = Folder.objects.filter(guideline=guideline.id)

    context = {"folders": mapping_folders(guideline_folders), "guidelineTitle": "Teste"}

    # documentId = guideline.index
    # Redirect to /guide/xx/document/xx
    # with guideline sidebar content

    # documentId = "Colchão Doc"
    # return redirect("document", documentId=1)

    # items = mapping_folders(guideline.folder)
    # if request.htmx:
    #     html_markdown = {
    #         "text": Document.objects.get(id=documentId).content,
    #         "title": "Colchão"
    #     }
    #     print(html_markdown)
    #     context = {
    #         "items": items[0]["children"],
    #         "doc": html_markdown,
    #         "guideline": "Processadora Guideline"
    #     }
    #     return render(request, "pages/guides.html#document-content", context)
    # else:
    #     html_markdown = {
    #         "text": "# Visão Geral",
    #         "title": "Adicionar uma nova tabela indicando qual documento é o principal"
    #     }
    #     # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
    #     context = {"items": items[0]["children"], "doc": html_markdown, "guideline": guide}
    print(context)
    return render(request, "pages/documents.html", context)


def document_view(request, documentId):
    # guideline = Guideline.objects.get(title="Processadora Guideline")
    # context = {
    #     "folders": mapping_folders(guideline_folders),
    #     "guidelineTitle": "Teste"
    # }
    # items = mapping_folders(guideline.folder)
    try:
        document = Document.objects.get(id=documentId)
        guideline_folders = Folder.objects.filter(
            guideline=document.parent.guideline.id
        )
        context = {
            "doc": {"text": document.content, "title": document.title},
            "folders": mapping_folders(guideline_folders),
            "guidelineTitle": document.parent.guideline,
        }

        # if request.htmx:
        # html_markdown = {
        #     "text": document.content,
        #     "title": document.title
        # }
        #     # print(html_markdown)
        #     context = {
        #         "doc": html_markdown,
        #     }
        #     return render(request, "pages/guide.html#document-content", context)
        # else:
        # html_markdown = {
        #     "title": document.title,
        #     "text": document.content
        # }
        # TODO: Adicionar uma nova profundidade na sidebar. Ajustar botoes e htmx
        # context = {"items": items[0]["children"], "doc": html_markdown, "guideline": "Processadora Guideline"}
        return render(request, "pages/documents.html", context)

    except ObjectDoesNotExist:
        return redirect("guide", guide="Processadora Guideline")
