# Dynamic background

**dynamic-background** è un'applicazione che cambia automaticamente lo sfondo del desktop con immagini fresche e casuali scaricate da Internet. Può essere utilizzata su **Windows**, **macOS** e **Linux**, ed è completamente personalizzabile in base alle tue preferenze, come l'URL da cui scaricare le immagini e l'intervallo di tempo tra un cambio e l'altro.

## Funzionalità principali

- **Cambio automatico dello sfondo**: Imposta un intervallo di tempo in cui l'app cambierà lo sfondo del desktop con un'immagine diversa presa da un URL che supporta dimensioni dinamiche.
- **Compatibilità multi-piattaforma**: Funziona su Windows, macOS e Linux, quindi può essere usato su qualsiasi sistema si abbia.
- **Avvio automatico**: Può essere configurato per avviarsi automaticamente quando si accende computer.
- **Interfaccia semplice**: Una volta configurata, l'app funziona in background senza bisogno di interagire con essa.

## Come funziona

L'applicazione scarica un'immagine da un URL che è possibile configurare. Questo URL può contenere variabili per le dimensioni dello schermo, come `{screen_width}` e `{screen_height}`, in modo che l'immagine si adatti perfettamente alla risoluzione. 

Ad esempio, un URL come `https://picsum.photos/{screen_width}/{screen_height}` fornisce immagini a caso con le dimensioni dello schermo.

L'app quindi scarica l'immagine e la imposta come sfondo del desktop. Il processo si ripete ogni volta che passa l'intervallo di tempo impostato.

## Creazione dell'eseguibile

Per creare un eseguibile standalone per l'applicazione **Dynamic Background**, è possibile utilizzare **PyInstaller**, uno strumento che permette di trasformare gli script Python in eseguibili autonomi.

### Creazione dell'eseguibile con PyInstaller

Per creare un eseguibile che non mostri la finestra del terminale e non richieda un'installazione di Python sul sistema di destinazione, usare il comando seguente:

```bash
pyinstaller --onefile --windowed -i NONE main.py
```

- **`--onefile`**: Crea un singolo file eseguibile.
- **`--windowed`**: Impedisce che venga aperta una finestra del terminale quando l'applicazione viene eseguita.
- **`-i NONE`**: Impedisce l'inclusione dell'icona di default.

### Dipendenze da installare con `requirements.txt`

Per installare tutte le dipendenze necessarie per l'applicazione (incluso PyInstaller e altre librerie Python che potrebbero essere utilizzate), è possibile utilizzare `requirements.txt`.

**Installare tutte le dipendenze** utilizzando il comando `pip`:

```bash
pip install -r requirements.txt
```

Questo comando installerà tutte le librerie elencate nel file `requirements.txt` in un colpo solo, consentendo di preparare l'ambiente per l'esecuzione o la creazione dell'eseguibile.

## Come ottenere l'app

### Per gli utenti Windows, macOS e Linux

1. **Scarica l'app**:

   [Pagina delle release](https://github.com/alessandromasone/dynamic-background/releases) del repository su GitHub. Versioni precompilate per **Windows**, **macOS** e **Linux**.

2. **Installa l'app**:

   Una volta scaricato il file eseguibile per il sistema operativo, basta avviarlo come una normale applicazione. Non è necessario Python o altre dipendenze sul sistema.

3. **Configura l'app**:

   È possibile l'URL da cui scaricare le immagini e l'intervallo di tempo tra un cambio e l'altro. È possibile decidere se l'app debba avviarsi automaticamente con il sistema operativo.

4. **Fai partire l'app**:

   Dopo aver configurato tutto, l'app inizierà a cambiare automaticamente lo sfondo del desktop. Non è necessaria alcuna interazione manuale, se non per la configurazione iniziale.

## Personalizzazione

### URL dell'immagine

L'URL dell'immagine è la risorsa da cui l'app scarica le immagini da usare come sfondo. Si può personalizzare questo URL per usare un servizio di immagini casuali o anche un proprio server. 

L'URL supporta le variabili `{screen_width}` e `{screen_height}`, che verranno sostituite con la risoluzione dello schermo. Ad esempio:

- `https://picsum.photos/{screen_width}/{screen_height}`

### Intervallo di tempo

L'app cambierà lo sfondo a intervalli regolari. L'intervallo si imposta in secondi per determinare quanto spesso verrà cambiato lo sfondo. Ad esempio, se impostato a 10 secondi, ogni 10 secondi lo sfondo verrà cambiato con una nuova immagine.

### Avvio automatico

L'app può essere impostata per avviarsi automaticamente ogni volta che si accende il computer.

- **Windows**: L'app crea un collegamento nel menu di avvio di Windows.
- **macOS**: L'app viene configurata per avviarsi tramite un file di lancio che viene caricato automaticamente.
- **Linux**: L'app viene aggiunta alla lista delle applicazioni che si avviano all'accesso.

### Esempio di configurazione

Una volta configurata, l'app utilizzerà un file di configurazione salvato sul computer. Ecco un esempio di come potrebbe essere il file di configurazione:

```json
{
  "url": "https://picsum.photos/{screen_width}/{screen_height}",
  "tempo_intervalo": 10
}
```

In questo caso, l'URL usato per scaricare le immagini sarà quello di **Picsum Photos**, e lo sfondo cambierà ogni 10 secondi.

## Comandi della riga di comando

È possiible usare diversi comandi per configurare l'app direttamente dalla riga di comando (se impostato l'avvio automatico prendere le preferenze dell'ultimo avvio):

- **Personalizzare l'URL dell'immagine**:

    ```bash
    wallpaper_changer.exe -u "https://example.com/{screen_width}/{screen_height}"
    ```

- **Impostare l'intervallo di cambio dello sfondo** (in secondi):

    ```bash
    wallpaper_changer.exe -t 30
    ```

- **Abilitare l'avvio automatico**:

    ```bash
    wallpaper_changer.exe --setup-autostart
    ```

- **Disabilitare l'avvio automatico**:

    ```bash
    wallpaper_changer.exe --remove-autostart
    ```

## Sistema operativo supportati

L'app è compatibile con:

- **Windows**: Supporta Windows 7 e versioni successive.
- **macOS**: Funziona su macOS 10.10 (Yosemite) e versioni successive.
- **Linux**: Supporta le distribuzioni Linux più comuni che utilizzano GNOME come ambiente desktop.

## Contribuire

Se desideri contribuire a migliorare l'app, sei il benvenuto! Puoi fare una **fork** del repository, aggiungere le tue modifiche e inviare una **pull request**. Per favore, leggi le [linee guida per la contribuzione](CONTRIBUTING.md) prima di farlo.

## Supporto

Se hai domande o hai bisogno di aiuto, non esitare a **aprire una issue** su GitHub o a **contattarci** tramite i canali di supporto nel repository.

## Licenza

Distribuito sotto la **GNU General Public License v3.0**. Vedi il file [LICENSE](LICENSE) per maggiori dettagli.
