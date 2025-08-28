 import jakarta.inject.Inject;
 import jakarta.inject.Singleton;
 import java.net.URI;
 import java.util.List;
 import java.util.Map;
 import java.util.Optional;
      */
     public Mono<HttpResponse<ServerInfo>> version(String kafkaCluster, String connectCluster) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request = HttpRequest.GET(URI.create(StringUtils.prependUri(config.getUrl(), "/")))
             .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.exchange(request, ServerInfo.class));
     }
 
      */
     public Mono<Map<String, ConnectorStatus>> listAll(String kafkaCluster, String connectCluster) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
         HttpRequest<?> request = HttpRequest.GET(
                URI.create(StringUtils.prependUri(config.getUrl(), "/connectors?expand=info&expand=status")))
             .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.retrieve(request, Argument.mapOf(String.class, ConnectorStatus.class)));
     }
 
      * @param connectorSpecs The connector config
      * @return The configuration infos
      */
    public Mono<ConfigInfos> validate(String kafkaCluster, String connectCluster, String connectorClass,
                                       ConnectorSpecs connectorSpecs) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request = HttpRequest.PUT(URI.create(
                    StringUtils.prependUri(config.getUrl(), "/connector-plugins/"
                        + connectorClass + "/config/validate")),
                 connectorSpecs)
             .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.retrieve(request, ConfigInfos.class));
     }
 
      * @param connectorSpecs The connector config
      * @return The creation or update response
      */
    public Mono<ConnectorInfo> createOrUpdate(String kafkaCluster, String connectCluster, String connector,
                                               ConnectorSpecs connectorSpecs) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.PUT(URI.create(StringUtils.prependUri(config.getUrl(), CONNECTORS + connector + "/config")),
                    connectorSpecs)
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.retrieve(request, ConnectorInfo.class));
     }
 
      */
     public Mono<HttpResponse<Void>> delete(String kafkaCluster, String connectCluster, String connector) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.DELETE(URI.create(StringUtils.prependUri(config.getUrl(), CONNECTORS + connector)))
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.exchange(request, Void.class));
     }
 
      */
     public Mono<List<ConnectorPluginInfo>> connectPlugins(String kafkaCluster, String connectCluster) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.GET(URI.create(StringUtils.prependUri(config.getUrl(), "/connector-plugins")))
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.retrieve(request, Argument.listOf(ConnectorPluginInfo.class)));
     }
 
      */
     public Mono<ConnectorStateInfo> status(String kafkaCluster, String connectCluster, String connector) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.GET(URI.create(StringUtils.prependUri(config.getUrl(), CONNECTORS + connector + "/status")))
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.retrieve(request, ConnectorStateInfo.class));
     }
 
      */
     public Mono<HttpResponse<Void>> restart(String kafkaCluster, String connectCluster, String connector, int taskId) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request = HttpRequest.POST(URI.create(
                StringUtils.prependUri(config.getUrl(), CONNECTORS + connector + "/tasks/"
                    + taskId + "/restart")), null)
             .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.exchange(request, Void.class));
     }
 
      */
     public Mono<HttpResponse<Void>> pause(String kafkaCluster, String connectCluster, String connector) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.PUT(URI.create(StringUtils.prependUri(config.getUrl(), CONNECTORS + connector + "/pause")),
                    null)
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.exchange(request, Void.class));
     }
 
      */
     public Mono<HttpResponse<Void>> resume(String kafkaCluster, String connectCluster, String connector) {
         KafkaConnectHttpConfig config = getKafkaConnectConfig(kafkaCluster, connectCluster);
        HttpRequest<?> request =
            HttpRequest.PUT(URI.create(StringUtils.prependUri(config.getUrl(), CONNECTORS + connector + "/resume")),
                    null)
                .basicAuth(config.getUsername(), config.getPassword());
         return Mono.from(httpClient.exchange(request, Void.class));
     }
 