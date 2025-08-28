 import org.slf4j.LoggerFactory;
 
 import java.io.File;
import java.io.IOException;
 import java.util.ArrayList;
 import java.util.HashMap;
 import java.util.List;
             // step2: file check
             if (!contractManager.isContractFileExist(contractVersion)) {
                 log.info("{}.jar does not exist ", contractVersion);
 
                try {
                    // step3. download file that does not exist.
                    File contractFile = contractManager.downloader(contractVersion);

                    // step4. verifying contract File
                    boolean isVerified = contractManager.verifyContractFile(contractFile, contractVersion);
                    if (!isVerified) {
                        log.error("Verifying contract file {} has an error occurred.", contractVersion);
                    }

                    // step5: install contract
                    long result = contractManager.installContract(
                            contractVersion, contractFile, branchContract.isSystem());
 
                    if (result == -1) {
                        log.error("something wrong in installing contract version {}", contractVersion);
                    }
 
                } catch (IOException e) {
                    log.error("contract {} version download failed! ", contractVersion);
                }
             }
         }
 
        // step4. inject contract
         try {
             contractManager.reloadInject();
         } catch (IllegalAccessException e) {
             log.error(e.getMessage());
             throw new FailedOperationException("contract Inject Fail");
         }
 

     }
 
     private void initGenesis() {