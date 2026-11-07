<!-- language-bar -->
[English](../README.md) · **Français** · [Español](README.es.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)
<!-- /language-bar -->

# PC Hardware Advisor

> Traduction automatique non relue. La version anglaise (../README.md) fait foi. Les corrections sont bienvenues : voir ../CONTRIBUTING.md.

PC Hardware Advisor est un plugin pour Claude (Claude Code, et Cowork dans l'application de bureau Claude) qui rend Claude fiable sur le matériel PC de bureau. Il trouve le meilleur prix livré pour une pièce, où que ce soit dans le monde, vérifie que les pièces fonctionnent ensemble, conçoit des configurations complètes selon un usage et un budget, dimensionne des machines pour l'IA en local, évalue les annonces d'occasion et suit les prix selon un calendrier. Chaque chiffre fourni est daté, sourcé et noté selon sa fiabilité. Le plugin ne fait que lire : il n'achète jamais rien et ne contacte jamais un vendeur.

Claude répond dans la langue dans laquelle vous écrivez. Les noms de pièces, les références (SKU) et les unités restent tels que publiés.

## Ce qu'il fait

Six skills et un sous-agent.

- **`hunt-prices`** : trouve le meilleur prix livré (avec TVA, droits de douane et frais de port) pour un article précis, partout dans le monde. Les revendeurs directs apparaissent en premier, les places de marché sont listées à part, et chaque ligne contient une colonne de fiabilité. Il utilise l'agent `price-scout` pour lire plusieurs sites en parallèle.
- **`check-compatibility`** : donne des verdicts deux à deux entre des pièces : compatible, compatible sous conditions, ou incompatible. Un verdict conditionnel énonce la condition exacte et sa source.
- **`build-config`** : conçoit une configuration complète à partir de l'usage, du budget, du pays et de vos contraintes. Il renvoie une configuration principale, ainsi qu'une variante moins chère et une variante plus puissante. Il ne propose que des pièces neuves et des pièces reconditionnées par des professionnels.
- **`size-local-ai`** : dimensionne le matériel pour faire tourner des modèles en local. Il couvre la VRAM, la bande passante mémoire, les estimations de tokens par seconde (signalées comme estimations), le multi-GPU, les APU, les eGPU et les environnements logiciels.
- **`review-used-listing`** : examine une annonce d'occasion et renvoie un verdict : acheter, négocier ou éviter. Il ajoute des questions pour le vendeur, des tests à effectuer lors de la remise de l'objet, et une marge de négociation.
- **`track-price`** : met en place des contrôles réguliers d'un prix, ne vous alerte que lorsque le prix passe sous votre seuil, et tient à jour un fichier d'historique. Il n'achète jamais.
- **`price-scout`** (agent) : lit plusieurs pages de revendeurs ou de places de marché pour une pièce précise et renvoie des lignes de prix normalisées, sans analyse. `hunt-prices` le lance.

Hors périmètre : consoles, smartphones, tablettes, ordinateurs portables en tant que produits, et tout ce qui achète ou contacte des vendeurs.

## Principes

- **Chaque prix est daté.** Un prix sans date de relevé n'est pas reporté.
- **Le vendeur est typé.** Revendeur direct, vendeur de place de marché, reconditionneur et particulier sont des lignes distinctes, jamais mélangées.
- **Prix livré, ou « hors frais ».** Les prix incluent la TVA, les droits de douane et l'expédition vers votre pays. Lorsqu'un élément ne peut pas être établi, la ligne indique « hors frais » au lieu de deviner.
- **La fiabilité est affichée.** Chaque chiffre indique à quel point il est étayé.
- **Rien n'est inventé.** Si une caractéristique, un prix ou une règle ne peut pas être sourcé, Claude le dit.
- **Sites bloqués : repli sur le navigateur, jamais de contournement.** Si un site refuse la lecture automatisée et qu'un outil de navigateur est disponible, Claude ouvre de sa propre initiative les quelques pages qui comptent dans le navigateur, en lecture seule, et le signale. Il s'arrête à tout captcha ou contrôle anti-robot et n'imite jamais un humain pour le franchir. Sinon, il vous demande une capture d'écran ou un texte copié. Aucun user agent alternatif, cache ni miroir n'est utilisé.
- **Lecture seule.** Le plugin n'achète jamais, ne crée jamais de compte, ne soumet jamais de formulaire et ne contacte jamais de vendeur. C'est à vous de le faire.

Dix références partagées (méthode de recherche, revendeurs par pays, critères de revendeur, achat à l'international, liste de contrôle du marché d'occasion, sockets et chipsets, mémoire, alimentations et connectiques, formats et boîtiers, bande passante des GPU pour l'IA) sont datées et sourcées. Elles ont été vérifiées pour la dernière fois le 2026-11-07.

## Installation

### Claude Code

Utilisez le dépôt comme place de marché, puis installez le plugin depuis celle-ci.

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` accepte un dépôt GitHub (`owner/repo`), une URL git ou https, ou un chemin local. Pour ce dépôt, l'adresse GitHub est `brissonjo-sudo/pc-hardware-advisor`. Ajoutez `--scope project` ou `--scope local` à l'une ou l'autre commande si vous ne souhaitez pas d'installation pour l'ensemble de l'utilisateur (la valeur par défaut est `user`).

Pour vérifier ce qui est installé, utilisez `claude plugin marketplace list`.

### Développement local

Pour essayer le plugin depuis une copie de travail sans l'installer :

```
claude --plugin-dir <path to this repository>
```

### Application de bureau Claude / Cowork

Récupérez le fichier `pc-hardware-advisor.plugin` (joint à une version publiée lorsqu'il en existe une, ou généré à partir d'une copie de travail avec `python scripts/build_plugin.py`, qui l'écrit dans `dist/`), glissez-le dans l'application de bureau Claude, puis acceptez l'invite d'installation.

## Exemples de demandes

Claude choisit le bon skill à partir de la demande. Quelques exemples :

1. « Trouve le meilleur prix livré en Allemagne pour un Ryzen 7 9800X3D. Revendeurs directs d'abord, places de marché à part. »
2. « Est-il moins cher d'importer une RTX 5070 Ti depuis les États-Unis vers le Canada, une fois les droits de douane et l'expédition inclus ? »
3. « Ce kit DDR5-6000 fonctionnera-t-il avec une carte ASUS TUF B650 et un Ryzen 7 7700 ? Donne un verdict par paire. »
4. « Compose-moi un PC de jeu silencieux en 1440p pour 1 400 EUR en Espagne. Donne-moi aussi une variante moins chère et une variante plus puissante. »
5. « Je veux faire tourner un modèle de 70B en local à une vitesse utilisable. Quelle VRAM et quelle bande passante mémoire me faut-il, et deux GPU d'occasion de 24 Go suffiraient-ils ? »
6. « Examine cette annonce de RTX 3090 d'occasion (lien ci-dessous). J'achète, je négocie ou j'évite ? Que dois-je demander au vendeur ? »
7. « Surveille le prix du Samsung 990 Pro 2 To au Royaume-Uni, et alerte-moi seulement s'il descend sous 120 GBP. »
8. En français : « Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part. »
9. En español : « Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU? »
10. « Un APU avec 64 Go de mémoire unifiée peut-il faire tourner un modèle de 32B, et à quelle vitesse dois-je m'attendre ? Indique clairement ce qui est une estimation. »

## Connecteurs

Les skills désignent les outils par catégorie (recherche web, récupération de pages web, comparateur de prix, site d'annonces, navigateur, planificateur, notifications), et non par produit : tout outil équivalent convient. Rien dans le plugin n'exige un compte, une clé d'API ou un service payant. Les catégories, les sources de données facultatives et les règles qui s'appliquent à tous les outils sont décrites dans [CONNECTORS.md](../CONNECTORS.md).

## Limites

- **Les prix sont périssables.** Un prix n'est exact qu'à sa date de relevé. Les stocks et les promotions changent en quelques heures.
- **Certains sites bloquent la lecture automatisée.** Ces lignes sont marquées comme bloquées, et Claude vous demande une capture d'écran ou un texte copié.
- **Les règles fiscales et douanières évoluent vite.** La TVA, les droits de douane et les seuils de minimis ont changé à plusieurs reprises en 2025 et 2026. Vérifiez la source officielle avant un import important.
- **Les estimations restent des estimations.** Les chiffres de tokens par seconde et les projections similaires sont modélisés, non mesurés sur votre machine, et sont signalés comme tels.
- **La couverture de recherche comporte des lacunes.** Certains pays, revendeurs et pièces de niche sont couverts de manière superficielle. Les références indiquent où.
- **Ce n'est ni un conseil financier ni un conseil juridique.** Le plugin éclaire une décision d'achat. Il ne donne pas de conseil en matière fiscale, douanière ou de droit de la consommation.

## Confidentialité

Le plugin lui-même ne collecte rien et n'envoie rien nulle part. Les historiques de prix écrits par `track-price` restent là où vous choisissez de les conserver. Les outils que Claude utilise pour chercher et lire des pages (recherche web, récupération de pages web, planificateur) sont soumis aux conditions d'utilisation et aux politiques de confidentialité de leurs propres fournisseurs.

## Traductions

Traductions automatiques de ce README, non relues par un humain : [README.fr.md](README.fr.md), [README.es.md](README.es.md), [README.zh-CN.md](README.zh-CN.md), [README.hi.md](README.hi.md), [README.pt.md](README.pt.md), [README.ar.md](README.ar.md), [README.de.md](README.de.md), [README.ja.md](README.ja.md). La version anglaise fait foi.

## Contribuer

Les contributions sont bienvenues, selon des conditions précises, notamment une cession de droits. Lisez [CONTRIBUTING.md](../CONTRIBUTING.md) avant d'ouvrir une pull request.

## Licence

PC Hardware Advisor est disponible en source sous la PolyForm Noncommercial License 1.0.0 (SPDX : PolyForm-Noncommercial-1.0.0). L'usage non commercial est permis à tous ; l'usage commercial exige une licence distincte délivrée par l'auteur. La même licence couvre les skills, les références, la documentation et les traductions.

Texte intégral : [LICENSE](../LICENSE) et <https://polyformproject.org/licenses/noncommercial/1.0.0>.
