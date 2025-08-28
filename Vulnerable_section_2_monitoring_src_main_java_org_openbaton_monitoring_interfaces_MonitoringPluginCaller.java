 import java.io.Serializable;
 import java.lang.reflect.Type;
 import java.util.ArrayList;
import java.util.Date;
 import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
 import java.util.concurrent.TimeoutException;
 import org.openbaton.catalogue.mano.common.monitoring.AbstractVirtualizedResourceAlarm;
 import org.openbaton.catalogue.mano.common.monitoring.Alarm;
     pluginCaller.close();
   }
 
  public static void main(String[] args)
      throws IOException, TimeoutException, NotFoundException, ExecutionException,
          InterruptedException {
 
    ExecutorService executor = Executors.newFixedThreadPool(3);
 
    class Exec implements Callable<Object> {
 
      @Override
      public Object call() throws Exception {
        List<String> hosts = new ArrayList<>();
        hosts.add("hostname1");
        hosts.add("hostname2");
        return null /* new MonitoringPluginCaller("zabbix").getMeasurementResults(hosts, new ArrayList<String>(), "")*/;
       }
     }
 
     System.out.println("1st call");
     System.out.println(fut1.get());
     System.out.println("Time ---> " + (new Date().getTime() - time) / 1000);
  }
 
   @Override
   public String subscribeForFault(AlarmEndpoint filter) throws MonitoringException {