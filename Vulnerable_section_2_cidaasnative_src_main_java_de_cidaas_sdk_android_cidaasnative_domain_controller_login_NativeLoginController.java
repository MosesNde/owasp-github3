                 loginEntity.setUsername_type("email");
             }
 
            if (loginEntity.getPassword() != null && !loginEntity.getPassword().equals("") && loginEntity.getUsername() != null
                    && !loginEntity.getUsername().equals("") && requestId != null && !requestId.equals("")) {
 
                 loginCredentialsRequestEntity.setUsername(loginEntity.getUsername());
                 loginCredentialsRequestEntity.setUsername_type(loginEntity.getUsername_type());