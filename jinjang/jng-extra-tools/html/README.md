`jinjaNG` tools for HTML like files
===================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the script file `jnghtml.js`. Note the use of `<!--: if False :--> ... <!--: endif :-->` suchas to load the script `jnghtml.js` only when working on the template. **We suppose here that the `JavaScript` and `HTML` files are located in the smae folder.**

~~~html
<!DOCTYPE html>
<html>
<head>
<!--: if False :-->
<script type = "text/javascript"
        src  = "jnghtml.js">
</script>
<!--: endif :-->
</head>

<!--: if False :-->
<body onload = "jnghtml()">
<!--: else :-->
<body>
<!--: endif :-->
<p>
  The smallest {{ txt_example }} in the world.
</p>
</html>
~~~

The tiny template above will produce the ouput shown in the picture below.

---

![output](images/exavar.png)

---

> **WARNING.**
>
> The `jinja` variables can't be used as one `CSS` parameter.


What is done behind the scenes?
-------------------------------

The `JavaScript` code acts directly on the `document.body.outerHTML` using a regex to make hard replacements.
