 
 import static io.openbas.database.model.User.ROLE_ADMIN;
 import static io.openbas.service.EndpointService.JFROG_BASE;
 
 import com.fasterxml.jackson.databind.ObjectMapper;
 import io.openbas.database.model.Executor;
 import io.openbas.rest.helper.RestBehavior;
 import io.openbas.service.EndpointService;
 import io.openbas.service.FileService;
 import jakarta.annotation.Resource;
 import jakarta.transaction.Transactional;
 import jakarta.validation.Valid;
   }
 
   // Public API
   @GetMapping(
       value = "/api/agent/executable/openbas/{platform}/{architecture}",
       produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
   public @ResponseBody ResponseEntity<byte[]> getOpenBasAgentExecutable(
      @PathVariable String platform, @PathVariable String architecture) throws IOException {
     InputStream in = null;
     String resourcePath = "/openbas-agent/" + platform + "/" + architecture + "/";
     String filename = "";
   }
 
   // Public API
   @GetMapping(
      value = "/api/agent/package/openbas/{platform}/{architecture}",
       produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
   public @ResponseBody ResponseEntity<byte[]> getOpenBasAgentPackage(
      @PathVariable String platform, @PathVariable String architecture) throws IOException {
     byte[] file = null;
     String filename = null;
 
   }
 
   // Public API
   @GetMapping(value = "/api/agent/installer/openbas/{platform}/{token}")
   public @ResponseBody ResponseEntity<String> getOpenBasAgentInstaller(
      @PathVariable String platform, @PathVariable String token) throws IOException {
     Optional<Token> resolvedToken = tokenRepository.findByValue(token);
     if (resolvedToken.isEmpty()) {
       throw new UnsupportedOperationException("Invalid token");