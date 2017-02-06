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

Créez ensuite un environnement virtuel qui vous permettra d'installer flask localement (pour votre projet) et non
globalement (sur le système en entier).

Pour créer l'environnement virtuel:
```
python3 -m venv env
source env/bin/activate
```

Vous pouvez ensuite installer pip (qui vous permettra d'installer des librairies python)
wget https://bootstrap.pypa.io/get-pip.py
```
python get-pip.py
```

Vous pouvez alors installer flask ou tout autre librairie python:
```
pip3 install flask
```

Testez que flask est bien installé:
```
python
>>> import flask
>>>
```
