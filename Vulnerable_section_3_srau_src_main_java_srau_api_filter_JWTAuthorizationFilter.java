             String username = verify.getSubject();
             String roles = verify.getClaim("roles").asString();
 
            System.out.println(getAuthorities(roles));
             if (username != null) {
                 return new UsernamePasswordAuthenticationToken(
                         username,