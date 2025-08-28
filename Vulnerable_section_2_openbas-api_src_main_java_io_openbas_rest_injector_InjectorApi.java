 import static io.openbas.database.specification.InjectorSpecification.byName;
 import static io.openbas.helper.StreamHelper.fromIterable;
 import static io.openbas.service.EndpointService.JFROG_BASE;
 
 import com.fasterxml.jackson.core.JsonProcessingException;
 import com.fasterxml.jackson.databind.JsonNode;
       produces = MediaType.APPLICATION_OCTET_STREAM_VALUE)
   public @ResponseBody ResponseEntity<byte[]> getOpenBasImplant(
       @PathVariable String platform, @PathVariable String architecture) throws IOException {
     InputStream in = null;
     String filename = "";
     String resourcePath = "/openbas-implant/" + platform + "/" + architecture + "/";