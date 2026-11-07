# Passage 2 : 2026-11-07 (cas 01, 03, 05, 06)

Coût : 2,14 $, 389 s. Filtre par étiquettes (`--case` n'accepte pas les classes de caractères).

| Cas | Passage 1 | Passage 2 | Échecs | Diagnostic |
|---|---|---|---|---|
| 01 | 0,83 | 0,75 | itx-platform, bios-warning | Le skill s'arrête pour poser 3 questions (budget, modèle de 3090, type de RAM) : estimation tok/s exacte (28-35, mesure 35,3 citée) mais aucune config. |
| 03 | 0,30 | 0,50 | table, prices | Fond nettement meilleur : 13 kits lus sur fiches produit, France + BE/NL/ES, blocages listés. Forme : en traduisant le tableau, colonnes type de vendeur, pays, prix rendu et confiance supprimées. |
| 05 | 0,50 | 0,88 | history | Relevé initial fait ; s'arrête pour demander quel planificateur (cloud sans disque ou local) : historique non initialisé. |
| 06 | 0,60 | 0,40 | landed, options, prices | « Monde entier » traité par l'Allemagne seulement (intra-UE, pas un import) ; colonne type de vendeur « seller not shown ». Constat solide : 32 Go de VRAM neufs hors d'atteinte à 2 000 € aux prix de novembre 2026 (DDR5 32 Go ≈ 560 €). |

## Corrections apportées

1. `research-method.md` : affichage compact autorisé (en-têtes traduisibles) avec colonnes obligatoires : date, article, vendeur, type de vendeur, pays, prix affiché (TVA), prix rendu ou `excluding fees`, stock, confiance, source.
2. `build-config` : ne bloque plus sur les questions si l'usage et le pays sont connus (configuration la moins chère qui remplit l'exigence, questions en fin de réponse) ; « monde entier » impose au moins un import hors de la zone douanière de l'acheteur, chiffré.
3. `track-price` : historique toujours créé dès le relevé initial ; choix du planificateur sans demander, limites indiquées dans la confirmation.
