                                                                                                                 .narmesteLederFnr(LEDER_FNR)
                                                                                                                 .orgnummer(VIRKSOMHETSNUMMER));
 
        when(restTemplate.exchange(anyString(), eq(GET), any(HttpEntity.class), eq(NarmestelederResponse.class)))
                 .thenReturn(new ResponseEntity<>(narmestelederResponse, OK));
         when(narmesteLederRelasjonConverter.convert(any(NarmesteLederRelasjon.class), anyString()))
                 .thenReturn(new Naermesteleder()
 
         NarmestelederResponse narmestelederResponse = new NarmestelederResponse().narmesteLederRelasjon(null);
 
        when(restTemplate.exchange(anyString(), eq(GET), any(HttpEntity.class), eq(NarmestelederResponse.class))).thenReturn(
                 new ResponseEntity<>(narmestelederResponse, OK));
 
         Optional<Naermesteleder> naermestelederOptional = narmesteLederConsumer.narmesteLeder(SYKMELDT_FNR, VIRKSOMHETSNUMMER);