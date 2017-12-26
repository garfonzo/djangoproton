SASS is a CSS extension language that lets you write CSS is a more reusable way. Using SASS in your projects have always been a headache and a barrier to entry for many beginner developers. There is a lot of setup just so you can start writing in SASS. 

Of course you do not have to use SASS in your project but the option is automatically there for you in case you want or need to start writing SASS.

With Django Proton, you are able to write SASS in any of your apps and not worry about any compiling because all `scss` files in your project are automatically compiled together when the Django server runs.

## How it works

Django Proton comes with a [SASS compiler](https://github.com/jrief/django-sass-processor) that looks for `scss` files inside your apps static folder. For example: `your_app/static/your_app/style.scss`. Once the Django server is ran, Django Proton will search all of your apps `scss` files and compile them down into `css` inside the staticfiles directory in the project root.

## Getting Started

Simply start creating `scss` files inside your apps static folder. If your app is called `my_app` then this location will be at `my_app/static/my_app/`. From this location you are able to create any subdirectories of `scss` files and Django Proton will find them and compile them. 

In other words you may put your SASS files at `my_app/static/my_app/css/sass/style.scss` and Django Proton will still find them and compile them.

All files are compiled into your projects staticfiles directory. The compiled files will be located inside `project_name/staticfiles/compiled/`

### Inside Templates

You'll need to use a special static tag inside your templates if you want Django Proton to correctly locate them.

There is a special `sass_src` tag that you can use inside your Jinja2 templates.

This is an example of a `scss` file located at `my_app/static/my_app/static.scss`

```html
{% load sass_tags %}
    
<link href="{% sass_src 'my_app/style.scss' %}" rel="stylesheet" type="text/css" />
```

Although it is pointing to the `scss` file, because of the special `sass_src` template tag, Django Proton will compile it into `css` and return that file instead.

Django Proton will compile the SASS files whenever the server is ran. Because of performance issues, it will only do this once and only compile again when the timestamps of **_any_** of the files are newer than the compiled sass files (as you may have updated the `scss` files and need to recompile).