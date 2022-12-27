Without the special `about.yaml` file
-------------------------------------

If you are not using an `about.yaml` file, the `Builder` class looks for all the `MD` files to merge them into one, ordering the files using `natsorted` from the package `natsort`.
