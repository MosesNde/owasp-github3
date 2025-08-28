 import io.netty.util.concurrent.Promise;
 import io.netty.util.internal.SocketUtils;
 import lombok.extern.slf4j.Slf4j;
 import org.springframework.http.client.reactive.ReactorClientHttpConnector;
 import org.springframework.util.StringUtils;
 import org.springframework.web.reactive.function.client.ExchangeFilterFunction;
 import org.springframework.web.reactive.function.client.WebClient;
 import reactor.core.publisher.Mono;
 @Slf4j
 public class WebClientUtils {
 
    private static final Set<String> DISALLOWED_HOSTS = Set.of("169.254.169.254", "metadata.google.internal");
 
     public static final String HOST_NOT_ALLOWED = "Host not allowed.";
 
    public static final ExchangeFilterFunction IP_CHECK_FILTER = ExchangeFilterFunction.ofRequestProcessor(request -> {
        if (!StringUtils.hasText(request.url().getHost())) {
            return Mono.error(new AppsmithPluginException(
                    AppsmithPluginError.PLUGIN_DATASOURCE_ARGUMENT_ERROR, "Requested url host is null or empty"));
        }
        return DISALLOWED_HOSTS.contains(request.url().getHost())
                ? Mono.error(new UnknownHostException(HOST_NOT_ALLOWED))
                : Mono.just(request);
    });
 
     private WebClientUtils() {}
 
         return false;
     }
 
     private static class NameResolver extends InetNameResolver {
 
         public NameResolver(EventExecutor executor) {