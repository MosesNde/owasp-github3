     }
 
 
    public File downloader(ContractVersion version) throws IOException {
 
         int bufferSize = 1024;
 
             log.info("File name : {}", version);
             log.info("of bytes  : {}", byteWritten);
             log.info("-------Download End--------");
         }
 
        return new File(this.contractPath + File.separator + version + ".jar");
     }
 
     public boolean verifyContractFile(File contractFile, ContractVersion contractVersion) {
             ContractVersion checkVersion = ContractVersion.of(contractBinary);
             return contractVersion.toString().equals(checkVersion.toString());
         }  catch (IOException e) {
             return false;
         }
     }