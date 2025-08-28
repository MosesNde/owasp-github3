 import org.springframework.beans.factory.annotation.Autowired;
 import org.springframework.http.HttpStatus;
 import org.springframework.http.ResponseEntity;
 import org.springframework.stereotype.Service;
 
 import javax.servlet.http.HttpSession;
 
     @Autowired
     UserRepository userRepository;
 
     @Override
     public ResponseEntity saveNewUser(User user) {
         String username = user.getUsername();
        String password = user.getPassword();  // TODO: for FIX, we need to hash password and store in DB: passwordEncoder.encode(password)
         BigDecimal balance = user.getBalance();
 
         // check duplicate user
     public ResponseEntity checkUser(User user, HttpSession session) {
         String username = user.getUsername();
         String password = user.getPassword();
        if (!userRepository.existsUserByUsernameAndPassword(username, password)) {
             ErrorResponse msg = ErrorResponse
                     .builder()
                     .code(HttpStatus.UNAUTHORIZED.value())