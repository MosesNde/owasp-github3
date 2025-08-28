 import org.springframework.http.ResponseEntity;
 import org.springframework.stereotype.Component;
 import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;
 
 import java.util.List;
 import java.util.Optional;
 import java.util.function.Function;
 
import static java.util.stream.Collectors.toList;
 import static no.nav.syfo.config.CacheConfig.CACHENAME_ANSATTE;
 import static no.nav.syfo.config.CacheConfig.CACHENAME_LEDER;
 import static no.nav.syfo.util.CredentialUtilKt.bearerHeader;
         String token = azureAdTokenConsumer.getAccessToken(narmestelederScope);
 
         ResponseEntity<NarmestelederResponse> response = restTemplate.exchange(
                getLederUrl(virksomhetsnummer),
                 GET,
                 entityForSykmeldt(token, fnr),
                NarmestelederResponse.class
         );
         throwExceptionIfError(response.getStatusCode(), HENT_LEDER_NARMESTELEDER_FEILET);
 
         return narmestelederUrl + "/leder/narmesteleder/aktive";
     }
 
    private String getLederUrl(String virksomhetsnummer) {
        return UriComponentsBuilder.fromHttpUrl(narmestelederUrl + "/sykmeldt/narmesteleder").queryParam("orgnummer", virksomhetsnummer).toUriString();
     }
 
     public boolean erNaermesteLederForAnsatt(String naermesteLederFnr, String ansattFnr) {
         List<String> ansatteFnr = ansatte(naermesteLederFnr).stream()
                 .map(Ansatt::fnr)
                .collect(toList());
 
         return ansatteFnr.contains(ansattFnr);
     }