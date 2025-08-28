 import jakarta.inject.Inject;
 import jakarta.inject.Singleton;
 import java.net.URI;
 import java.util.Arrays;
 import java.util.List;
 import java.util.Optional;
      */
     public Mono<SchemaResponse> getSubject(String kafkaCluster, String subject, String version) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
         HttpRequest<?> request = HttpRequest.GET(
                URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + VERSIONS + version)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaResponse.class))
             .onErrorResume(HttpClientResponseException.class,
                 ex -> ex.getStatus().equals(HttpStatus.NOT_FOUND) ? Mono.empty() : Mono.error(ex));
      */
     public Flux<SchemaResponse> getAllSubjectVersions(String kafkaCluster, String subject) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
         HttpRequest<?> request = HttpRequest.GET(
                URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + "/versions")))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
 
         return Flux.from(httpClient.retrieve(request, Integer[].class))
             .flatMap(ids -> Flux.fromIterable(Arrays.asList(ids))
                 .flatMap(id -> {
                    HttpRequest<?> requestVersion = HttpRequest.GET(
                            URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + VERSIONS + id)))
                         .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
 
                     return httpClient.retrieve(requestVersion, SchemaResponse.class);
      */
     public Mono<SchemaResponse> register(String kafkaCluster, String subject, SchemaRequest body) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request =
            HttpRequest.POST(URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + "/versions")),
                    body)
                .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaResponse.class));
     }
 
      */
     public Mono<Integer[]> deleteSubject(String kafkaCluster, String subject, boolean hardDelete) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
         MutableHttpRequest<?> request = HttpRequest.DELETE(
                URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + "?permanent=" + hardDelete)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, Integer[].class));
     }
 
      * @param hardDelete   Should the subject be hard deleted or not
      * @return The version of the deleted subject
      */
    public Mono<Integer> deleteSubjectVersion(String kafkaCluster, String subject, String version,
                                                boolean hardDelete) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
         MutableHttpRequest<?> request = HttpRequest.DELETE(
                URI.create(StringUtils.prependUri(config.getUrl(), SUBJECTS + subject + VERSIONS + version
                + "?permanent=" + hardDelete)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, Integer.class));
     }
 
      * @param body         The request
      * @return The schema compatibility validation
      */
    public Mono<SchemaCompatibilityCheckResponse> validateSchemaCompatibility(String kafkaCluster, String subject,
                                                                               SchemaRequest body) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest.POST(URI.create(
                    StringUtils.prependUri(config.getUrl(), "/compatibility/subjects/" + subject
                        + "/versions?verbose=true")),
                body)
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaCompatibilityCheckResponse.class))
             .onErrorResume(HttpClientResponseException.class,
                 ex -> ex.getStatus().equals(HttpStatus.NOT_FOUND) ? Mono.empty() : Mono.error(ex));
      * @param body         The schema compatibility request
      * @return The schema compatibility update
      */
    public Mono<SchemaCompatibilityResponse> updateSubjectCompatibility(String kafkaCluster, String subject,
                                                                         SchemaCompatibilityRequest body) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request =
            HttpRequest.PUT(URI.create(StringUtils.prependUri(config.getUrl(), CONFIG + subject)), body)
                .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaCompatibilityResponse.class));
     }
 
      */
     public Mono<SchemaCompatibilityResponse> getCurrentCompatibilityBySubject(String kafkaCluster, String subject) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest.GET(URI.create(StringUtils.prependUri(config.getUrl(), CONFIG + subject)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaCompatibilityResponse.class))
             .onErrorResume(HttpClientResponseException.class,
                 ex -> ex.getStatus().equals(HttpStatus.NOT_FOUND) ? Mono.empty() : Mono.error(ex));
      */
     public Mono<SchemaCompatibilityResponse> deleteCurrentCompatibilityBySubject(String kafkaCluster, String subject) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        MutableHttpRequest<?> request =
            HttpRequest.DELETE(URI.create(StringUtils.prependUri(config.getUrl(), CONFIG + subject)))
                .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, SchemaCompatibilityResponse.class));
     }
 
      */
     public Mono<List<TagTopicInfo>> associateTags(String kafkaCluster, List<TagTopicInfo> tagSpecs) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest
            .POST(URI.create(StringUtils.prependUri(
                config.getUrl(),
                 "/catalog/v1/entity/tags")), tagSpecs)
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, Argument.listOf(TagTopicInfo.class)));
     }
 
      */
     public Mono<List<TagInfo>> createTags(String kafkaCluster, List<TagInfo> tags) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest.POST(URI.create(StringUtils.prependUri(
                config.getUrl(), "/catalog/v1/types/tagdefs")), tags)
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, Argument.listOf(TagInfo.class)));
     }
 
      */
     public Mono<HttpResponse<Void>> dissociateTag(String kafkaCluster, String entityName, String tagName) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest
            .DELETE(URI.create(StringUtils.prependUri(
                config.getUrl(),
                 "/catalog/v1/entity/type/kafka_topic/name/" + entityName + "/tags/" + tagName)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.exchange(request, Void.class));
     }
 
      */
     public Mono<TopicListResponse> getTopicWithCatalogInfo(String kafkaCluster, int limit, int offset) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest
            .GET(URI.create(StringUtils.prependUri(
                config.getUrl(), "/catalog/v1/search/basic?type=kafka_topic&limit="
                    + limit + "&offset=" + offset)))
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.retrieve(request, TopicListResponse.class));
     }
 
     public Mono<HttpResponse<TopicDescriptionUpdateResponse>> updateDescription(String kafkaCluster,
                                                                                 TopicDescriptionUpdateBody body) {
         ManagedClusterProperties.SchemaRegistryProperties config = getSchemaRegistry(kafkaCluster);
        HttpRequest<?> request = HttpRequest
            .PUT(URI.create(StringUtils.prependUri(
                config.getUrl(), "/catalog/v1/entity")), body)
             .basicAuth(config.getBasicAuthUsername(), config.getBasicAuthPassword());
         return Mono.from(httpClient.exchange(request, TopicDescriptionUpdateResponse.class));
     }
 