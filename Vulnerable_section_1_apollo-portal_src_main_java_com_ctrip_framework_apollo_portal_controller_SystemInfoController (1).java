     List<Env> allEnvList = portalSettings.getAllEnvs();
 
     for (Env env : allEnvList) {
      EnvironmentInfo environmentInfo = new EnvironmentInfo();
      String metaServerAddresses = MetaDomainConsts.getMetaServerAddress(env);

      environmentInfo.setEnv(env);
      environmentInfo.setActive(portalSettings.isEnvActive(env));
      environmentInfo.setMetaServerAddress(metaServerAddresses);

      String selectedMetaServerAddress = MetaDomainConsts.getDomain(env);
      try {
        environmentInfo.setConfigServices(getServerAddress(selectedMetaServerAddress, CONFIG_SERVICE_URL_PATH));

        environmentInfo.setAdminServices(getServerAddress(selectedMetaServerAddress, ADMIN_SERVICE_URL_PATH));
      } catch (Throwable ex) {
        String errorMessage = "Loading config/admin services from meta server: " + selectedMetaServerAddress + " failed!";
        logger.error(errorMessage, ex);
        environmentInfo.setErrorMessage(errorMessage + " Exception: " + ex.getMessage());
      }
 
       systemInfo.addEnvironment(environmentInfo);
     }
 
   @PreAuthorize(value = "@permissionValidator.isSuperAdmin()")
   @GetMapping(value = "/health")
  public Health checkHealth(@RequestParam String host) {
    return restTemplate.getForObject(host + "/health", Health.class);
   }
 
   private ServiceDTO[] getServerAddress(String metaServerAddress, String path) {