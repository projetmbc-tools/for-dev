`jinjaNG` tools for HTML like files
===================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the script file `jngutils-html.js`. Note the use of `<!--: if False :--> ... <!--: endif :-->` suchas to load the script `jngutils-html.js` only when working on the template. **We suppose here that the `JavaScript` and `HTML` files are located in the smae folder.**

~~~html
<!DOCTYPE html>
<html>
<head>
<!--: if False :-->
<script type = "text/javascript"
        src  = "jngutils-html.js">
</script>
<!--: endif :-->
</head>

<!--: if False :-->
<body onload = "<:TOOLS:>()">
<!--: else :-->
<body>
<!--: endif :-->
<p>
  The smallest {{ txt_example }} in the world.
</p>
</html>
~~~

This template will produce the output shown in the following picture.

---

![output](images/exavar.png)

---

> **WARNING.**
>
> The `jinja` variables can't be used as one `CSS` parameter.


What is done behind the scenes?
-------------------------------

The `JavaScript` code acts directly on the `document.body.outerHTML` using a regex to make hard replacements.
