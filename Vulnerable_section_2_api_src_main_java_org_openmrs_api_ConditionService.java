  */
 public interface ConditionService extends OpenmrsService {
 
	/**
	 * Saves a condition
	 *
	 * @param condition - the condition to be saved
	 * @throws APIException   
	 */
	@Authorized({ PrivilegeConstants.EDIT_CONDITIONS })
	Condition saveCondition(Condition condition) throws APIException;

	/**
	 * Voids a condition
	 *
	 * @param condition - the condition to be voided
	 * @param voidReason - the reason for voiding the condition
	 * @throws APIException   
	 */
	@Authorized({ PrivilegeConstants.EDIT_CONDITIONS })
	Condition voidCondition(Condition condition, String voidReason) throws APIException;

 	/**
 	 * Gets a condition based on the uuid
 	 *
 	/**
 	 * Gets a condition by id
 	 *
	 * @param conditionId - the id of the Condition to retrieve
 	 * @return the Condition with the given id, or null if none exists
 	 * @throws APIException
 	 */
 	@Authorized({ PrivilegeConstants.GET_CONDITIONS })
 	Condition getCondition(Integer conditionId) throws APIException;
 
 	/**
	 * Revive a condition (pull a Lazarus)
 	 *
 	 * @param condition Condition to unvoid
 	 * @throws APIException
 	 */
 	@Authorized(PrivilegeConstants.DELETE_CONDITIONS)
 	void purgeCondition(Condition condition) throws APIException;
	
 }