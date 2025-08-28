 
 import com.google.gson.Gson;
 import com.google.gson.GsonBuilder;
 import dev.aikido.agent_api.storage.RedirectNode;
 
 import java.util.ArrayList;
     protected transient ArrayList<RedirectNode> redirectStartNodes;
     protected transient Map<String, Map<String, String>> cache = new HashMap<>();
 
     public boolean middlewareExecuted() {return executedMiddleware; }
     public void setExecutedMiddleware(boolean value) { executedMiddleware = value; }
 
         return cookies;
     }
     public Map<String, Map<String, String>> getCache() { return cache; }
 
     public String toJson() {
         Gson gson = new GsonBuilder().setPrettyPrinting().create();