# COVID-19 Sorveglianza Integrata Italia

![get_data_from_iss](https://github.com/floatingpurr/covid-19_sorveglianza_integrata_italia/workflows/get_data_from_iss/badge.svg)
[![GitHub commit](https://img.shields.io/github/last-commit/floatingpurr/covid-19_sorveglianza_integrata_italia)](https://github.com/floatingpurr/covid-19_sorveglianza_integrata_italia/commits/master)

Serie storica dei dati della sorveglianza integrata COVID-19 in Italia. I dati sono disponibili nel folder [`data`](data) di questo repository.

## Stato degli aggiornamenti

I dati vengono aggiornati ogni 15 minuti. Il [badge](#COVID-19-Sorveglianza-Integrata-Italia) a inizio pagina è di colore verde se gli aggiornamenti stanno funzionando senza errori. Per ulteriori dettagli, verificare i log del [workflow di aggiornamento](https://github.com/floatingpurr/covid-19_sorveglianza_integrata_italia/actions?query=workflow%3Aget_data_from_iss).

## Licensing

Il dato giornaliero viene rilasciato quotidianamente dall'Istituto Superiore di Sanità in [questa pagina web](https://www.epicentro.iss.it/coronavirus/sars-cov-2-dashboard) in un file Excel che sembra sovrascrivere il precedente. Qualora l'Istituto Superiore di Sanità ritenesse che la storicizzazione di questi dati non sia consentita o violi determinate norme, si prega di contattare l'owner del repository per richiederne la rimozione.

L'utilizzo di questi dati è consentito limitatamente a quanto contemplato dall'Istituto Superiore di Sanità, in qualità di ente distributore del dato. Si prega di consultare il relativo [sito web istituzionale](https://www.epicentro.iss.it/coronavirus/sars-cov-2-dashboard) per maggiori informazioni.


## Note

Il file Excel di origine contiene talvolta date non consistenti. In questi casi, non sapendo come correggere l'errore, il file non verrà inserito nella serie storica e la data risulterà mancante (E.g.,: [#2][i2] e [#3][i3]).


[i2]: https://github.com/floatingpurr/covid-19_sorveglianza_integrata_italia/issues/2
[i3]: https://github.com/floatingpurr/covid-19_sorveglianza_integrata_italia/issues/3