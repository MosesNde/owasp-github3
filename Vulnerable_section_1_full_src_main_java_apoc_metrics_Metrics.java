 
 import java.io.File;
 import java.io.FilenameFilter;
 import java.util.Arrays;
 import java.util.HashMap;
 import java.util.Map;
  */
 @Extended
 public class Metrics {
     @Context
     public Log log;
 
         config.put("header", true);
 
         File metricsDir = FileUtils.getMetricsDirectory();

         if (metricsDir == null) {
             throw new RuntimeException("Metrics directory either does not exist or is not readable.  " +
                     "To use this procedure please ensure CSV metrics are configured " +
                     "https://neo4j.com/docs/operations-manual/current/monitoring/metrics/expose/#metrics-csv");
         }
 
        String url = new File(metricsDir, metricName + ".csv").getAbsolutePath();
         CountingReader reader = null;
         try {
             reader = FileUtils.SupportedProtocols.file