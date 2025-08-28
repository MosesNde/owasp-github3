         });
     }
 
    @SetEnvironmentVariable(key = "AIKIDO_TOKEN", value = "invalid-token-2")
    @SetEnvironmentVariable(key = "AIKIDO_BLOCK", value = "true")
    @Test
    public void testSSRFWithoutPortAndWithoutThreadCache() throws Exception {
        setContextAndLifecycle("http://localhost:80");
        ThreadCache.set(null);
        assertThrows(ResourceAccessException.class, () -> {
            fetchResponse("http://localhost/weirdroute");
        });
    }

     private void fetchResponse(String urlString) {
         RestTemplate restTemplate = new RestTemplate();
         restTemplate.getForObject(urlString, String.class);