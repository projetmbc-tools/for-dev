Why yet another tiny language to store textual datas ?
======================================================

The package `orpyste` was born from a need to quickly write simple and structured datas to configuration files and for unit tests. Before getting into the details, here is a small example of an `orpyste` file storing informations on players. Sorry for the lack of originality ...


```
joueur_1::
    date  = 1985
    sexe  = masculin
    score = 18974
    alias = Super Mario

joueur_2::
    date  = 1991
    sexe  = féminin
    score = 32007
    alias = Sonic
```

Writing this with XML could be done like this :

```xml
<joueur_1 date="1985"
          sexe="masculin"
          score="18974"
          alias="Super Mario"/>

<joueur_2 date="1991"  
          sexe="féminin"
          score="32007" 
          alias="Sonic"/>
```

Using JSON, we could use the following variable.

```json
{
    "joueur_1": {
        "date": "1985",
        "sexe": "masculin",
        "score": "18974",
        "alias": "Super Mario",
    },
    "joueur_2": {
        "date": "1991",
        "sexe": "féminin",
        "score": "32007",
        "alias": "Sonic",
    }
}
```

As you can see, for simple datas, `orpyste` gives a very simple and efficient way to store informations.
