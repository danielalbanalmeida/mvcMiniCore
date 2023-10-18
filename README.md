# mvcMiniCore
![image](https://github.com/danielalbanalmeida/mvcMiniCore/assets/55764851/a96da8ba-7b4a-42e0-b0d8-5261485bb229)

Django follows the Model-View-Controller, which is often the MVT in the context of Django.

1. Model: The Model represents the application's data structure and business logic. In Django, models are defined as python classes that map to database tables.
2. View: The view is responsible for handling user requests and returning appropiate responses. In Django, views are Python functions or classes that take web requests and return web responses.
3. Template: While not explicity part of the MVC pattern, Django includes a Template system for handling the presentation layer. Templates are HTML files with embedded Python code, allowing developers to generate dynamically web pages.

For example here we have a simplified step-by-step process of how Django handles a typical web request:

![image](https://github.com/danielalbanalmeida/mvcMiniCore/assets/55764851/610826ab-5d96-4387-b363-01a9aa33f491)


- An incoming HTTP request is received by Django's web server or another web server.
- Django's URL dispatcher matches the requested URL to a corresponding view function or class based on the URL patterns defined in the project's configuration.
- The matched view function is executed. It may interact with the Model to retrieve or update data and render a Template to generate an HTML response.
- The HTML response is sent back to the client's web browser, displaying the dynamically generated web page.
- If there is any interaction with the user, such as form submissions or links, the process repeats as the user sends new request to different URLs.
