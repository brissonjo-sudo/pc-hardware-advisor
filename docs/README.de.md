<!-- language-bar -->
[English](../README.md) · [Français](README.fr.md) · [Español](README.es.md) · **Deutsch** · [Português](README.pt.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)
<!-- /language-bar -->

# PC Hardware Advisor

> Maschinelle Übersetzung, nicht von einem Menschen geprüft. Maßgeblich ist die englische Version (../README.md). Korrekturen sind willkommen, siehe ../CONTRIBUTING.md.

PC Hardware Advisor ist ein Plugin für Claude (Claude Code sowie Cowork in der Claude-Desktop-App), das Claude bei Desktop-PC-Hardware verlässlich macht. Es findet den besten gelieferten Preis für ein Bauteil irgendwo auf der Welt, prüft, ob Teile zusammenarbeiten, plant komplette Builds für einen Einsatzzweck und ein Budget, dimensioniert Rechner für lokale KI, bewertet Gebrauchtangebote und überwacht Preise nach Zeitplan. Jede Angabe ist datiert, mit Quelle versehen und in ihrer Verlässlichkeit eingestuft. Das Plugin liest nur: Es kauft nie etwas und kontaktiert nie einen Verkäufer.

Claude antwortet in der Sprache, in der du schreibst. Teilenamen, SKUs und Einheiten bleiben so, wie sie veröffentlicht sind.

## Was es leistet

Sechs Skills und ein Sub-Agent.

- **`hunt-prices`**: findet den besten Endpreis (geliefert, inklusive MwSt., Zöllen und Versand) für ein exakt bestimmtes Produkt, weltweit. Direkte Händler stehen an erster Stelle, Marktplätze werden separat aufgeführt, und jede Zeile hat eine Spalte für die Verlässlichkeit. Der Skill nutzt den Agenten `price-scout`, um mehrere Shops parallel auszulesen.
- **`check-compatibility`**: gibt paarweise Urteile zwischen Teilen ab: kompatibel, kompatibel mit Bedingungen oder inkompatibel. Ein bedingtes Urteil nennt die genaue Bedingung und die Quelle.
- **`build-config`**: plant einen vollständigen Build aus Einsatzzweck, Budget, Land und deinen Vorgaben. Er liefert einen Hauptbuild sowie eine günstigere und eine stärkere Variante. Vorgeschlagen werden nur neue Teile und professionell aufbereitete Gebrauchtteile.
- **`size-local-ai`**: dimensioniert Hardware für das lokale Ausführen von Modellen. Abgedeckt werden VRAM, Speicherbandbreite, Schätzungen zu Tokens pro Sekunde (als Schätzungen gekennzeichnet), Multi-GPU, APUs, eGPUs und Software-Stacks.
- **`review-used-listing`**: prüft ein einzelnes Gebrauchtangebot und gibt ein Urteil ab: zugreifen, verhandeln oder meiden. Er liefert Fragen an den Verkäufer, Tests bei der Übergabe und eine Verhandlungsspanne.
- **`track-price`**: richtet geplante Preisprüfungen ein, benachrichtigt dich nur, wenn der Preis unter deine Schwelle fällt, und führt eine Verlaufsdatei. Er kauft nie.
- **`price-scout`** (Agent): liest mehrere Händler- oder Marktplatzseiten für ein exakt bestimmtes Teil aus und liefert normalisierte Preiszeilen ohne Analyse. `hunt-prices` startet ihn.

Nicht im Umfang enthalten: Konsolen, Smartphones, Tablets, Laptops als Produkte sowie alles, was kauft oder Verkäufer kontaktiert.

## Grundsätze

- **Jeder Preis ist datiert.** Ein Preis ohne Abfragedatum wird nicht ausgegeben.
- **Der Verkäufertyp ist angegeben.** Direkter Händler, Marktplatzverkäufer, Aufbereiter oder Privatperson sind verschiedene Zeilen und werden nie vermischt.
- **Endpreis, oder „ohne Gebühren".** Preise enthalten MwSt., Zölle und Versand in dein Land. Lässt sich ein Bestandteil nicht ermitteln, steht in der Zeile „ohne Gebühren", statt zu raten.
- **Die Verlässlichkeit wird angezeigt.** Jede Angabe zeigt, wie gut sie belegt ist.
- **Nichts wird erfunden.** Lässt sich eine Spezifikation, ein Preis oder eine Regel nicht belegen, sagt Claude das.
- **Gesperrte Seiten: Ausweichen auf den Browser, niemals Tricks.** Verweigert eine Seite das automatisierte Auslesen und steht ein Browser-Werkzeug zur Verfügung, bietet Claude dir in einer Zeile an, die Seite in deinem Browser zu öffnen; antwortest du mit „ja“, liest es die wenigen wichtigen Seiten, nur lesend, und sagt das. Bei Captchas oder Bot-Prüfungen hält es an und gibt sich nie als Mensch aus, um sie zu umgehen. Andernfalls bittet es dich um einen Screenshot oder eingefügten Text. Es werden keine alternativen User-Agents, Caches oder Spiegel verwendet.
- **Nur lesend.** Das Plugin kauft nie, legt keine Konten an, sendet keine Formulare ab und kontaktiert keine Verkäufer. Das machst du selbst.

Zehn gemeinsame Referenzen (Rechercheverfahren, Händler nach Land, Kriterien für Händler, internationaler Einkauf, Checkliste für den Gebrauchtmarkt, Sockel und Chipsätze, Speicher, Netzteile und Anschlüsse, Formfaktoren und Gehäuse, GPU-Bandbreite für KI) sind datiert und mit Quellen belegt. Sie wurden zuletzt am 2026-11-07 geprüft.

## Installation

### Claude Code

Verwende das Repository als Marketplace und installiere das Plugin von dort.

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` akzeptiert ein GitHub-Repository (`owner/repo`), eine Git- oder HTTPS-URL oder einen lokalen Pfad. Für dieses Repository lautet die GitHub-Adresse `brissonjo-sudo/pc-hardware-advisor`. Füge `--scope project` oder `--scope local` an einen der beiden Befehle an, wenn du keine benutzerweite Installation möchtest (Standard ist `user`).

Mit `claude plugin marketplace list` prüfst du, was installiert ist.

### Lokale Entwicklung

Um das Plugin aus einer Arbeitskopie auszuprobieren, ohne es zu installieren:

```
claude --plugin-dir <path to this repository>
```

### Claude-Desktop / Cowork

Besorge dir die Datei `pc-hardware-advisor.plugin` (sie hängt an einem Release, sobald eines veröffentlicht ist, oder du erstellst sie aus einer Arbeitskopie mit `python scripts/build_plugin.py`, das sie nach `dist/` schreibt), ziehe sie in die Claude-Desktop-App und bestätige die Installationsaufforderung.

### OpenAI Codex (experimentell)

Das Repository ist auch ein Codex-Marketplace (`.agents/plugins/marketplace.json`, Manifest `.codex-plugin/plugin.json`). Fügen Sie ihn hinzu und installieren Sie das Plugin dann aus dem Plugin-Verzeichnis der ChatGPT-Desktop-App oder von Codex (`/plugins`):

```
codex plugin marketplace add brissonjo-sudo/pc-hardware-advisor
```

Noch nicht getestet. Codex hat keine Sub-Agenten: Preisseiten werden einzeln gelesen, also langsamer. Die geplante Preisüberwachung braucht ein Planungswerkzeug in der Sitzung. Das Repository ist privat: Der Befehl braucht Git-Zugriff darauf.

## Aktualisieren, prüfen und deinstallieren

**Aktualisieren (Claude Code).** Marketplace aktualisieren, dann das Plugin aktualisieren, dann Claude Code neu starten:

```
claude plugin marketplace update pc-hardware-advisor
claude plugin update pc-hardware-advisor@pc-hardware-advisor
```

Ein Update wird nur angeboten, wenn sich die `version` in `plugin.json` ändert.

**Prüfen.** Fragen Sie Claude „Welche Plugin-Skills hast du für PC-Hardware?“ oder führen Sie `claude plugin list` aus und suchen Sie `pc-hardware-advisor` samt Version.

**Deinstallieren.** Führen Sie `claude plugin uninstall pc-hardware-advisor@pc-hardware-advisor` aus. In der Claude-Desktop-App entfernen Sie das Plugin in den Plugin-Einstellungen. Von Ihnen angelegte Preisverlaufsdateien bleiben dort, wo Sie sie abgelegt haben.

Das Repository ist derzeit privat, daher funktioniert der Marketplace-Weg nur für Konten mit Zugriff; die `.plugin`-Datei ist die Alternative.

## Beispielanfragen

Claude wählt den passenden Skill anhand der Anfrage. Ein paar Beispiele:

1. „Finde den besten gelieferten Preis nach Deutschland für einen Ryzen 7 9800X3D. Zuerst direkte Händler, Marktplätze separat."
2. „Lohnt es sich, eine RTX 5070 Ti aus den USA nach Kanada zu importieren, wenn Zölle und Versand enthalten sind?"
3. „Funktioniert dieses DDR5-6000-Kit mit einem ASUS TUF B650 und einem Ryzen 7 7700? Gib ein Urteil pro Paar."
4. „Baue mir einen leisen 1440p-Gaming-PC für 1.400 EUR in Spanien. Gib mir auch eine günstigere und eine stärkere Variante."
5. „Ich möchte ein 70B-Modell lokal mit brauchbarer Geschwindigkeit betreiben. Welchen VRAM und welche Speicherbandbreite brauche ich, und würden zwei gebrauchte 24-GB-GPUs reichen?"
6. „Prüfe dieses Gebrauchtangebot einer RTX 3090 für mich (Link unten). Zugreifen, verhandeln oder meiden? Was soll ich den Verkäufer fragen?"
7. „Beobachte den Preis der Samsung 990 Pro 2 TB in Großbritannien und benachrichtige mich nur, wenn er unter 120 GBP fällt."
8. En français : „Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part."
9. En español : „Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU?"
10. „Kann eine APU mit 64 GB einheitlichem Speicher ein 32B-Modell ausführen, und welche Geschwindigkeit ist zu erwarten? Kennzeichne, was eine Schätzung ist."

## Connectors

Die Skills verweisen auf Werkzeuge nach Kategorie (Websuche, Web-Abruf, Preisvergleich, Kleinanzeigen-Seite, Browser, Terminplaner, Benachrichtigungen), nicht nach Produkt, daher funktioniert jedes gleichwertige Werkzeug. Nichts im Plugin erfordert ein Konto, einen API-Schlüssel oder einen kostenpflichtigen Dienst. Kategorien, optionale Datenquellen und die Regeln, die für jedes Werkzeug gelten, stehen in [CONNECTORS.md](../CONNECTORS.md).

## Grenzen

- **Preise verfallen schnell.** Ein Preis gilt nur zum Abfragedatum. Bestand und Aktionen ändern sich innerhalb von Stunden.
- **Manche Seiten blockieren automatisiertes Auslesen.** Diese Zeilen sind als gesperrt markiert, und Claude bittet dich um einen Screenshot oder eingefügten Text.
- **Steuer- und Zollregeln sind volatil.** MwSt., Zölle und Freigrenzen (de minimis) haben sich 2025 und 2026 mehrfach geändert. Prüfe die offizielle Quelle, bevor du einen größeren Import tätigst.
- **Schätzungen bleiben Schätzungen.** Angaben zu Tokens pro Sekunde und ähnliche Prognosen sind modelliert, nicht auf deinem Rechner gemessen, und entsprechend gekennzeichnet.
- **Die Recherche hat Lücken.** Manche Länder, Händler und Nischenteile sind nur dünn abgedeckt. Die Referenzen sagen, wo.
- **Hohen Aufwand verwenden.** In Tests des Maintainers las `build-config` bei mittlerem Aufwand weniger Händler und übersah günstigere Optionen. Wählen Sie in Ihrer App hohen Aufwand, bevor Sie eine Konfiguration oder eine Preissuche anfragen.
- **Keine Finanz- oder Rechtsberatung.** Das Plugin unterstützt eine Kaufentscheidung. Es berät nicht zu Steuer-, Zoll- oder Verbraucherschutzfragen.

## Datenschutz

Das Plugin selbst erhebt nichts und sendet nichts irgendwohin. Preisverläufe, die `track-price` schreibt, bleiben dort, wo du sie speichern möchtest. Die Werkzeuge, mit denen Claude Seiten sucht und liest (Websuche, Web-Abruf, Terminplaner), unterliegen den Nutzungsbedingungen und Datenschutzrichtlinien ihrer jeweiligen Anbieter.

## Übersetzungen

Maschinelle Übersetzungen dieser README, nicht von einem Menschen geprüft: [README.fr.md](README.fr.md), [README.es.md](README.es.md), [README.zh-CN.md](README.zh-CN.md), [README.hi.md](README.hi.md), [README.pt.md](README.pt.md), [README.ar.md](README.ar.md), [README.de.md](README.de.md), [README.ja.md](README.ja.md). Maßgeblich ist die englische Version.

## Mitwirken

Beiträge sind unter bestimmten Bedingungen willkommen, einschließlich einer Übertragung der Rechte. Lies [CONTRIBUTING.md](../CONTRIBUTING.md), bevor du einen Pull Request eröffnest.

## Lizenz

PC Hardware Advisor ist unter der PolyForm Noncommercial License 1.0.0 als Source-Available-Software veröffentlicht (SPDX: PolyForm-Noncommercial-1.0.0). Nichtkommerzielle Nutzung ist für alle erlaubt; kommerzielle Nutzung erfordert eine separate Lizenz vom Autor. Dieselbe Lizenz gilt für die Skills, Referenzen, die Dokumentation und die Übersetzungen.

Volltext: [LICENSE](../LICENSE) und <https://polyformproject.org/licenses/noncommercial/1.0.0>.
