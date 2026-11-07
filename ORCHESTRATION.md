# ORCHESTRATION : pc-hardware-advisor

Journal du rituel avant chaque phase (parallélisation, modèle, isolation) et des validations Opus.
Orchestrateur : Opus (session principale). Démarrage : 2026-11-07.

## Phase 0. Initialisation (2026-11-07)

- Parallélisable : non, tâches courtes et séquentielles (structure, manifeste, licence, pilotage).
- Modèle : Opus seul (fichiers courts, aucun volumineux).
- Isolation : sans objet.
- Fait : dépôt local `main`, arborescence du plan, `plugin.json` validé par `claude plugin validate`, `LICENSE` copié depuis le dépôt officiel PolyForm et comparé mot à mot au texte de polyformproject.org.

## Phase R. Recherche (2026-11-07)

- Parallélisable : oui, 10 sous-agents indépendants, aucun ne lit la sortie d'un autre.
- Modèles :
  - Haiku (lecture et extraction) : R1 Europe Ouest, R1 Europe Sud et Centre, R1 anglophones, R1 Asie, R3 critères et sites à éviter, R5 occasion.
  - Sonnet (faits techniques et règles fiscales, où l'erreur coûte cher) : R2 API et flux, R2 achat international, R4 plateformes et mémoire, R4 alimentation et formats, R4 GPU et IA.
- Isolation : répertoire `research/`, un fichier par sous-agent, noms disjoints. Pas de worktree (aucune écriture concurrente sur un même fichier).
- Synthèse : fusionnée dans la phase 1 (voir DECISIONS D4).

### Validation de couverture phase R (Opus, 2026-11-07)

- Rendus à ce stade : R1 Europe Ouest, R1 Europe Sud et Centre, R1 anglophones, R2 API, R3 critères, R5 occasion. Tous ont sections demandées, sources numérotées, section « Not verified ».
- Trou principal commun : limite de débit WebFetch due au parallélisme (des dizaines de sites « non testés » plutôt que « bloqués »). Traité comme lacune documentée, pas comblé par contournement. Piste v0.2 : repasse séquentielle sur les sites non testés.
- Données d'occasion EU quasi absentes (une seule donnée 3090) : le skill `review-used-listing` doit donc imposer une vérification en ligne systématique.

## Phase 1. Références partagées (2026-11-07)

- Parallélisable : oui, en trois lots disjoints selon la recherche disponible. Lot A (research-method, retailer-criteria, used-market-checklist) lancé dès R3 et R5 rendus ; lot B (retailers-by-country, international-buying) après R1 Asie et R2 achat ; lot C (5 références techniques) après R4.
- Modèle : Sonnet pour la rédaction ; Haiku pour la vérification mécanique (datation, citations, valeurs sans source).
- Isolation : `references/`, un fichier par rédacteur, aucun fichier partagé entre lots. Brief commun figé dans `research/_brief-common.md` (format de ligne de prix canonique).

## Phases 2, 3 et 4. Skills et agent (2026-11-07)

- Parallélisable : oui. Écart au plan : les phases 2 et 3 sont regroupées par dépendance plutôt que par ordre. Vague 1 (dépend seulement des références commerciales, déjà prêtes) : `hunt-prices` + agent `price-scout` (même rédacteur, cohérence du format de ligne), `review-used-listing`, `track-price`. Vague 2 (dépend de la recherche R4) : `check-compatibility`, `build-config`, `size-local-ai`.
- Modèle : Sonnet par skill ; relecture Opus de chaque skill contre la porte de validation §7.
- Isolation : `skills/<nom>/` propre à chaque rédacteur ; `agents/` réservé au rédacteur de `hunt-prices`. Brief commun : `research/_brief-skills.md`.
