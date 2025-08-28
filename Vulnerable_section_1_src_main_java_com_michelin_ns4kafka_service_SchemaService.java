      */
     public Mono<Integer> register(Namespace namespace, Schema schema) {
         return schemaRegistryClient
            .register(namespace.getMetadata().getCluster(),
                schema.getMetadata().getName(), SchemaRequest.builder()
                     .schemaType(String.valueOf(schema.getSpec().getSchemaType()))
                     .schema(schema.getSpec().getSchema())
                     .references(schema.getSpec().getReferences())