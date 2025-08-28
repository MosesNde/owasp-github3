         });
     }
 
    @SetEnvironmentVariable(key = "AIKIDO_TOKEN", value = "invalid-token-2")
    @SetEnvironmentVariable(key = "AIKIDO_BLOCK", value = "true")
    @Test
    public void testSSRFWithoutPortAndWithoutThreadCache() throws Exception {
        setContextAndLifecycle("http://localhost:80");
        ThreadCache.set(null);
        assertThrows(ConnectException.class, () -> {
            fetchResponse("http://localhost/weirdroute");
        });
    }

     @SetEnvironmentVariable(key = "AIKIDO_TOKEN", value = "invalid-token-2")
     @SetEnvironmentVariable(key = "AIKIDO_BLOCK", value = "true")
     @Test