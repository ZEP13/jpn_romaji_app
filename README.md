perment de passe le programme d'installation pour installer le package localement en mode édition
    
    uv tool install -e .
    (cela va le metre dans le local bin)

plus declare la command CLI "jpn" pour exécuter la fonction principale du module "main".
    [project.scripts]
    jpn = "main:main"

pour desinstaller le package localement en mode édition
    
    uv tool uninstall jpn
