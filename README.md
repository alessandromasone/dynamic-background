# Dynamic-background

## Descrizione
Dynamic-background è un'applicativo sviluppato per consentire agli utenti di impostare automaticamente uno sfondo dinamico sul loro desktop. L'applicativo controlla periodicamente un'immagine di sfondo da un URL specificato o da un URL predefinito e la imposta come sfondo del desktop. In questo modo, gli utenti possono godere di uno sfondo sempre nuovo e interessante senza doverlo cambiare manualmente.

## Requisiti
Per utilizzare correttamente Dynamic-background, è necessario soddisfare i seguenti requisiti:

- Sistema operativo Windows
- Connessione Internet attiva

## Istruzioni per l'uso
1. Assicurarsi di soddisfare i requisiti di sistema elencati sopra.
2. Scaricare il codice sorgente dell'applicativo Dynamic-background dal repository GitHub.
3. Aprire un prompt dei comandi e passare alla directory in cui è stato scaricato il codice sorgente.
4. Eseguire il seguente comando per installare le librerie
5. Eseguire il file `dynamic_background.py` per avviare l'applicativo.
6. L'applicativo si nasconderà tra i processi di sistema e inizierà a cambiare lo sfondo del desktop ogni X minuti (dove X è il valore impostato o il valore predefinito di 5 minuti).
7. Per personalizzare l'applicativo, è possibile utilizzare i seguenti parametri:
    - `-t <tempo>`: Imposta l'intervallo di tempo (in minuti) tra i cambiamenti dello sfondo del desktop. Il valore deve essere compreso tra 1 e 2592000 (30 giorni).
    - `-u <url>`: Imposta l'URL da cui l'applicativo scaricherà le immagini di sfondo. Se non viene specificato, verrà utilizzato l'URL predefinito "https://picsum.photos/3840/2160".

## Esempi di utilizzo
- Esempio 1: Esecuzione dell'applicativo con i valori predefiniti (cambio dello sfondo ogni 5 minuti con le immagini di default):
    ```
    python dynamic_background.py
    ```

- Esempio 2: Esecuzione dell'applicativo con un intervallo di tempo di 10 minuti:
    ```
    python dynamic_background.py -t 10
    ```

- Esempio 3: Esecuzione dell'applicativo con un URL personalizzato per le immagini di sfondo:
    ```
    python dynamic_background.py -u <url_personalizzato>
    ```

## Licenza
Dynamic-background è distribuito con licenza MIT.
