# Todo

## Technologies

* Starlette pour le web: rapide et simple.
  Nb: Il faudrait dans un 2ème temps simplifier la création de route et sous-routes mais c'est secondaire, on a le decorateur `app.route`
  Ce decorateur devra être fusionné avec celui de pony orm `db_session`

* PonyOrm pour l'orm: rapide et pythonique.

  Lacunes:

  * La notion de recordset d'Odoo était un gros gain
  * Génération de donnée selon une query (voir ponyjs?)
  * les hook: ils sont présent juste avant d'envoyer à la db, c-à-d on ne peut pas déclencher un write à partir d'un autre pour converger vers une solution qui convient aux 2 modules (mais on évite les récursions bizarres, mais c'est une perte)

* Dynaconf pour gérer la configuration et tout ce qui n'a pas besoin d'être en base de donnée (tout ce qui est unique)
* ModuleHandler pour fusionner les modules
* XMLego pour aggreger les templates



## Issues

* gérer la mise à jour de la db:
  * Mettre des scriptes par version du module?
  * Idealement, automatiser la mise à jour