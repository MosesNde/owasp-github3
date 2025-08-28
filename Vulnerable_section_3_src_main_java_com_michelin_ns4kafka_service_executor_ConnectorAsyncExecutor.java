     private Mono<ConnectorInfo> deployConnector(Connector connector) {
         return kafkaConnectClient.createOrUpdate(managedClusterProperties.getName(),
                 connector.getSpec().getConnectCluster(),
                connector.getMetadata().getName(), ConnectorSpecs.builder()
                     .config(connector.getSpec().getConfig())
                     .build())
             .doOnSuccess(