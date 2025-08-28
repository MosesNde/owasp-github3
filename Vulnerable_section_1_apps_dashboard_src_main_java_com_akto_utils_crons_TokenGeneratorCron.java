                 AccountTask.instance.executeTask(new Consumer<Account>() {
                     @Override
                     public void accept(Account t) {
                        if (!DashboardMode.isOnPremDeployment()) {
                             loggerMaker.infoAndAddToDb("Skipping tokenGeneratorScheduler, deployment type condition not satisfied");
                             return;
                         }