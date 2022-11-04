How to use sections ?
=====================

The following partial snippet shows how to use sections which allow to work with virtual files containing classical `peuf` contents indicating by `...` here.

```
==
Section 1
==

...


==
Section 2 after the section 1
==

...
```


Above we have used minimal forms for naming sections using only two equal signs. You can use more signs and maybe you would prefer the following convention.

```
=========
Section 1
=========

...


=============================
Section 2 after the section 1
=============================

...
```


Working with this kind of `peuf` files needs to import `Read` or `ReadBlock` from `orpyste.section` instead of `orpyste.data`.


For querypaths and also json representations, the sections are indicated by putting their name inside `<...>`.
