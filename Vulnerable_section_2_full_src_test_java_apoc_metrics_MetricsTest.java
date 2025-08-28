 import apoc.util.Neo4jContainerExtension;
 import apoc.util.TestUtil;
 import org.junit.AfterClass;
 import org.junit.BeforeClass;
 import org.junit.Test;
 import org.neo4j.driver.Session;
 import java.util.stream.Collectors;
 import java.util.stream.Stream;
 
 import static apoc.util.FileUtils.NEO4J_DIRECTORY_CONFIGURATION_SETTING_NAMES;
 import static apoc.util.TestContainerUtil.createEnterpriseDB;
 import static apoc.util.TestContainerUtil.testCall;
             neo4jContainer.close();
         }
     }
 
     @Test
     public void shouldGetMetrics() {