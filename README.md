# Possiveis nomes
1. MyDock
2. Doca
3. Guidelines

# Similar Companies/Ideas
https://developers.notion.com/reference/intro
https://docs.gusto.com/embedded-payroll/docs/introduction
https://readme.com/
https://swagger.io/
https://bump.sh/



# Introduction
Esse projeto tem por intuito satisfazer uma necessidade de pequenas empresas em solucionar de forma fácil o gerenciamento de APIs, i.e. gerenciar a Especificação da API, o manual, e suas versões.
Além disso podendo trazer mais funcionalidades dentro do contexto. Como:
1. Intermediar a comunicação do cliente com o provedor do serviço (um chat)
2. Utilizar de IA para pesquisas e respostas rápidas. (um chat de IA ou um personagem distinto, em paralelo com uma conversa real)
3. Simplificar a visualização dos produtos possíveis e contratados. Assim uma tela de login, junto de um gerencial dos serviços contratados. Bem comum em sites de ferramentas, mas trazido a nível de empresas B2B. Onde o desenvolvedor sofre com problemas de copmunicação.
4. Em algum momento distante possibilitar a visualização de custos e pagamentos do serviço.
5. Visualização de uso da API
6. Plataforma para multiplas empresas encontrarem APIs de outras empresas
7. Inicialmente uma página para empresas sustentarem APIs para seus clientes de forma mais simples, rápida e barata


# Django x Tailwindcss

Learn how to integrate Tailwind.css into your Django projects.

## Installation Steps

- Create an env with python -m venv venv
    - source /venv/bin/activate 
    - Install python packages with: pip install -r src/requirements.txt
- Install nodejs
    - Install tailwind with npm install -D tailwindcss
    - npx tailwindcss init

## Running Steps
- npm run dev
- source venv/bin/activate
- python src/manage.py runserver

## Limpar a base de dados
- python src/manage.py flush

## Criar usuario admin

Tailwind is a paradigm shift for how you'll use CSS in your _all_ of your web applications and Django projects.  Instead of using classes like `btn-primary` you'll use a list of more robust classes to describe how you want your element to render. Such as:

- `bg-blue-500` (the background color)
- `text-white` (the text color)
- `rounded-lg` The border radius
- `hover:bg-blue-800` The background color when someone _hovers_ on this element
- `px-5` The horizontal padding on the left or the right of the contents

And so much more. Writing CSS classes like this is almost _too_ verbose since it seems to violate DRY but it does not. Instead, this verboseness unlocks a clarity in how you document your CSS classes and how things are rendered. It took me a long time to adopt Tailwind because of this verboseness but once I did, I have never looked back. Tailwind is incredible.

In this [course](https://www.codingforentrepreneurs.com/courses/django-x-tailwindcss/), we will learn how to setup Django project to leverage Tailwind.css from scratch.


__References__
- [Course](https://www.codingforentrepreneurs.com/courses/django-x-tailwindcss/)
- [Code Repo](https://github.com/codingforentrepreneurs/django-tailwindcss)
- [Django Docs](https://djangoproject.com)
- [Tailwind.css Docs](https://tailwindcss.com)