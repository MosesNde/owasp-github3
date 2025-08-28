     }
 
     @GetMapping("/health")
    public String health(@RequestHeader String host) {
        return healthService.health(host);
     }
 }