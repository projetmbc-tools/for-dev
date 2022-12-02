/**
prototype::
    action : ????


ref::
    The initial code comes from cf::``this post ; https://stackoverflow.com/a/74336061/4589608 ``.
**/
jinjang =_=>
  document.body.outerHTML=document.body.outerHTML
    // .replace(/\[\[.*?\]\]/g, "")
    .replace(
        /\{\{(.*?)\}\}/g,
        `<span style="color: red; font-weight: bold; `
        +
        `border: solid 1px; padding: 1px 3px">$1</span>`
    );
