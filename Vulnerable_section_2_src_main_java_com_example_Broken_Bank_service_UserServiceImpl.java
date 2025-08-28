 
 import javax.servlet.http.HttpSession;
 import javax.transaction.Transactional;
 import java.math.BigDecimal;
 import java.util.Date;
 import java.util.List;
 
import static com.example.Broken.Bank.constand.Constants.CURRENTUSER;

 @Service
 @Transactional
 public class UserServiceImpl implements UserService {
             ErrorResponse msg = ErrorResponse
                     .builder()
                     .code(HttpStatus.BAD_REQUEST.value())
                    .message("Bad request: duplicate username, empty initial balance etc.")
                     .timestamp(new Date())
                     .build();
             return ResponseEntity.badRequest().body(msg);
             ErrorResponse msg = ErrorResponse
                     .builder()
                     .code(HttpStatus.UNAUTHORIZED.value())
                    .message("User or password is not correct.Please check again")
                     .timestamp(new Date())
                     .build();
             return ResponseEntity.badRequest().body(msg);
             ErrorResponse msg = ErrorResponse
                     .builder()
                     .code(HttpStatus.BAD_REQUEST.value())
                    .message("Withdraw money is larger than your current balance!")
                     .timestamp(new Date())
                     .build();
             return ResponseEntity.badRequest().body(msg);