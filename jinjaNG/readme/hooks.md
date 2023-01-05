Hooks: doing pre and post-processing
------------------------------------

### What we need?

In the previous section, we saw how to produce a `LaTeX` file by feeding a template. It would be handy to be able to compile the resulting file in `PDF` format to make it readable by anyone. To do this easily, `jinjaNG` offers the possibility to work with pre and post-processing, or "hooks".



### How to do this?

We need to work with a `YAML` configuration file. For simplicity, we use the default settings by working in a directory that looks like this.

~~~
+ myfolder
    * cfg.jng.yaml
    * data.json
    * template.tex
~~~


Writing external commands is done in the `cfg.jng.yaml` file. Here, we just use the `post` block for post-processing, but we could also use a `pre` block for pre-processing. Note the use of `{output}` which will be replaced by the path of the file built by `jinjaNG`.

~~~yaml
hooks:
  post:
    - latexmk -interaction=nonstopmode -pdf "{output}"
    - latexmk -interaction=nonstopmode -c   "{output}"
~~~

> One important thing to know is that the commands must be written relative to the parent folder of the template.


Once the `cfg.jng.yaml` file has been built, it is sufficient to do the following on the command line (we have omitted the output). The `auto` value of the `--config` option indicates that the configurations are in the `cfg.jng.yaml` file.

~~~
> cd path/to/the/myfolder
> jinjang --config auto data.json template.tex output.tex
[...]
~~~


The contents of `myfolder` have been changed as follows.

~~~
+ myfolder
    * cfg.jng.yaml
    * data.json
    * output.pdf
    * output.tex
    * template.tex
~~~


> If there are multiple templates in a folder, or to use test configurations, it is useful to be able to choose the configuration file explicitly.
> In this type of situation, it is sufficient to proceed via `jinjang --config path/to/speconfig.yaml ...` for example.
