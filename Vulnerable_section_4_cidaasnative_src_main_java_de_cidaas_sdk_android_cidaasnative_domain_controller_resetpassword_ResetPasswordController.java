 
 import androidx.annotation.NonNull;
 
 import java.util.Dictionary;
 
 import de.cidaas.sdk.android.cidaasnative.data.entity.resetpassword.ResetPasswordRequestEntity;
     public void notNullChecking(String baseurl, final ResetPasswordEntity resetPasswordEntity, final EventResult<ResetNewPasswordResponseEntity> resetpasswordResult) {
         String methodName = "RegistrationController :notNullChecking()";
         try {
            if (resetPasswordEntity.getPassword() != null && !resetPasswordEntity.getPassword().equals("") && resetPasswordEntity.getConfirmPassword() != null
                    && !resetPasswordEntity.getConfirmPassword().equals("")) {
                if (resetPasswordEntity.getPassword().equals(resetPasswordEntity.getConfirmPassword())) {
 
                     if (resetPasswordEntity.getResetRequestId() != null && !resetPasswordEntity.getResetRequestId().equals("") &&
                             resetPasswordEntity.getExchangeId() != null && !resetPasswordEntity.getExchangeId().equals("")) {
         String methodName = "RegistrationController :resetNewPassword()";
         try {
 
            if (resetPasswordEntity.getPassword() != null && !resetPasswordEntity.getPassword().equals("") &&
                    resetPasswordEntity.getConfirmPassword() != null && !resetPasswordEntity.getConfirmPassword().equals("")
                    && baseurl != null && !baseurl.equals("")) {
 
                 ResetPasswordService.getShared(context).resetNewPassword(resetPasswordEntity, baseurl,
                         new EventResult<ResetNewPasswordResponseEntity>() {