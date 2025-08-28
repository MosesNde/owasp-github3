 
             try {
                 // Load the class from the JAR
                Class<?> clazz = classLoader.loadClass("dev.aikido.agent_api.collectors.HostnameCollector");
 
                 // Run report with "argument"
                 for (Method method2: clazz.getMethods()) {