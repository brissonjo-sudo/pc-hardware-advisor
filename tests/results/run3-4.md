# Passages 3 et 4 : 2026-11-07

## Passage 3 (cas 01, 03, 05, 06) : 3,19 $, 501 s

| Cas | Score | Échecs | Constat |
|---|---|---|---|
| 01 | 0,83 (seuil atteint) | prices | Config complète proposée (carte ITX LGA1700, alertes BIOS et puissance, débit estimé), mais tableau sans type de vendeur par ligne. |
| 03 | 0,50 | table, prices | Fond conforme (date, vendeur typé, pays, « excluding fees », confiance par ligne). Restent : prix cités en prose sans leurs attributs, articles en rupture classés. |
| 05 | 0,88 (seuil atteint) | history | Relevé initial, historique CSV créé, aucune tâche annoncée faussement (aucun planificateur exposé dans le bac à sable), définition complète fournie, prudence sur une routine cloud. Colonnes de l'historique non montrées. |
| 06 | 0,60 | landed, prices | Tableau de synthèse à 4 colonnes ; import hors UE absent. |

Corrections : règle de prose (un prix cité renvoie à sa ligne), ruptures hors classement, colonnes obligatoires étendues à `size-local-ai`, en-tête de l'historique dans la confirmation de `track-price`.

## Passage 4 (cas 03, 06) : 1,68 $, 261 s

| Cas | Score | Échecs | Constat |
|---|---|---|---|
| 03 | 0,70 | table | Dates sans année (« 11-07 »), ordre de tri non strict. |
| 06 | 0,60 | landed, prices | Prix américain lu (2 199,99 $) mais prix rendu non calculé ; pays et type de vendeur « not shown » pour des revendeurs français pourtant qualifiés par la référence pays. Recommandation de fond pertinente (mini-PC Strix Halo 128 Go seul candidat proche du budget, mesures communautaires citées). |

Corrections : règles de remplissage de l'affichage compact (date ISO complète, pays et type tirés de la référence pays, tri strict), calcul obligatoire du prix rendu estimé pour tout prix étranger lu.
