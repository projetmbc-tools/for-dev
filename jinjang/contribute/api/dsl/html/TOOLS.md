`jinjaNG` tools for HTML like files
===================================

How to use the tools?
---------------------

Here is the miminal way to use the tools from the script file `<:TOOLS_LONG:>`. Note the use of `<!--: if False :--> ... <!--: endif :-->` suchas to load the script `<:TOOLS_LONG:>` only when working on the template. **We suppose here that the `JavaScript` and `HTML` files are located in the smae folder.**

~~~html
<!DOCTYPE html>
<html>
<head>
<!--: if False :-->
<script type = "text/javascript"
        src  = "<:TOOLS_LONG:>">
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

The tiny template above will produce an ouput similar to the following one.

<div style="border: solid 1px; padding: 4px 6px, margin-bottom:12px;">
The smallest <span style="color: red; font-weight: bold; `border: solid 1px; padding: 1px 3px">txt_example</span> in the world.
</div>
<br/>

> **WARNING.**
>
> The `jinja` variables can't be used as one `CSS` variable.


What is done behind the scenes?
-------------------------------

The `JavaScript` code acts directly on the `document.body.outerHTML` using a regex to make hard replacements.
