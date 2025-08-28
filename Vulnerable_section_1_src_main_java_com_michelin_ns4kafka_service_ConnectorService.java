      */
     public Mono<List<String>> validateRemotely(Namespace namespace, Connector connector) {
         return kafkaConnectClient.validate(namespace.getMetadata().getCluster(),
                connector.getSpec().getConnectCluster(), connector.getSpec().getConfig().get(CONNECTOR_CLASS),
                ConnectorSpecs.builder().config(connector.getSpec().getConfig()).build())
             .map(configInfos -> configInfos.configs()
                 .stream()
                 .filter(configInfo -> !configInfo.configValue().errors().isEmpty())