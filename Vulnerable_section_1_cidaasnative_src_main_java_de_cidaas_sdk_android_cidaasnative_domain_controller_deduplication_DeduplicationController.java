         try {
             String baseurl = result.get("DomainURL");
             String clientId = result.get("ClientId");
            if (loginEntity.getUsername() != null && !loginEntity.getUsername().equals("") && loginEntity.getPassword() != null &&
                    !loginEntity.getPassword().equals("")) {
 
 
                 LoginCredentialsRequestEntity loginCredentialsRequestEntity = new LoginCredentialsRequestEntity();