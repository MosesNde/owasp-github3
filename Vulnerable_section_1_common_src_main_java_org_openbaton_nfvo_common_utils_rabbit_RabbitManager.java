     return factory;
   }
 
  public static void main(String[] args) throws IOException {
    System.out.println(getQueues("localhost", "admin", "openbaton", "/", 5672));
  }
 }