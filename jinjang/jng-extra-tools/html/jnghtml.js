/***
prototype::
    action : the function ``jnghtml`` use a regex like replacement to
             transform a sequence like ``{{ one_jinja_var }}`` into
             a span formatted looking like
             ``<span style="color: red; ...">one_jinja_var</span>``.


ref::
    The initial code comes from cf::``this post ;
                                      https://stackoverflow.com/a/74336061/4589608 ``.
***/
jnghtml = _ =>
    document.body.outerHTML = document.body.outerHTML
// PARAMS WILL COME LATER...
        // .replace(/\[\[.*?\]\]/g, "")
// VARIABLES
        .replace(
            /\{\{(.*?)\}\}/g,
              `<span style="color: red; font-weight: bold; `
            + `border: solid 1px; padding: 1px 3px">$1</span>`
        );
