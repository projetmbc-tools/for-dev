How to write files readable by `orpyste` ?
==========================================

The specification of the files readable by `orpyste` is named `peuf`. So the question becomes : *"What is a well formatted `peuf` file ?"*.
To answer this, let's look at the following example.

```
/*
Long comment: here, we use the first block as a container.

Note the use of two consecutive double points so as to indicate a block.
*/  
book::
// Short comment: then the block `general` uses a key-value storing.
    general::
        author = M. Nobody
        title  = Does this book have a title ?
        date   = 2012, May the 1st

// Short comment: the last block `resume` uses a verbatim content.
    resume::
        This book is an ode to the passing time...


////
```


Let's explain the content of the preceding example.

1. You can comment your `peuf` files using C-like comments but **a comment can only start at the very beginning of a line**.

1. Datas are structured in blocks which can be of three different kinds.

    * A block is indicated using two consecutive double points and its content is indented.

    * A block can be a container like the block `book`. This is for gathering different blocks.

    * The block `general` stores key-value datas with the possibility to choose the separators. **Here we have used `=` but it is not an obligation.** You can also choose to allow or not multiple use of the same key.

    * The last kind of blocks is for a verbatim content. The last empty lines are removed except if you use the magic comment `////` as we have done. In our example the block `resume` has a content made of `This book is an ode to the passing time...` followed by two empty lines.
