Pour utiliser malt.labunix.uqam.ca comme un serveur flask, nous devrons nous établir un
tunnel SSH.

Putty -> Connection -> SSH -> Tunnels

```
Source port: XXXX
Destination: 127.0.0.1:XXXX
```

où XXXX est votre numéro de port qui est libre sur malt.

Allez ensuite dans "Session" en Host Name entrez malt.labunix.uqam.ca (port 22) puis Open.
Dites oui au dialogue et laissez la connection ouverte. Ne touchez plus à la fenêtre putty.

Sur X2go, vous pouvez lancer un serveur web de test de cette façon:

```
python -m SimpleHTTPServer XXXX
```
où XXXX est encore votre port.

De votre bureau, lancez un navigateur et accédez au 127.0.0.1:XXXX
Une arborescence de repertoire devrait apparaître.

Vous pouvez alors installer flask localement ou tout autre librairie python:
```
pip3 install --user flask
```

Testez que flask est bien installé:
```
python
>>> import flask
>>>
```
