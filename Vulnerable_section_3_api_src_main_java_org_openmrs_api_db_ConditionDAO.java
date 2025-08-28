 public interface ConditionDAO {
 
 	/**
	 * Saves the condition.
 	 *
	 * @param condition the condition to save.
	 * @return the saved condition.
 	 */
	Condition saveCondition(Condition condition);
 
 	/**
 	 * Gets the condition attached to the specified UUID.
 	 * @return the condition associated with the UUID.
 	 */
 	Condition getConditionByUuid(String uuid);

	/**
	 * Gets all conditions related to the specified patient.
	 *
	 * @param patient the patient whose condition history is being queried.
	 * @return all active and non active conditions related to the specified patient.
	 */
	List<Condition> getConditionHistory(Patient patient);

 	/**
 	 * Gets all active conditions related to the specified patient.
 	 *
 	List<Condition> getActiveConditions(Patient patient);
 
 	/**
	 * @see ConditionService#getAllConditions(Patient)
 	 */
 	List<Condition> getAllConditions(Patient patient);
 
 	/**
	 * @see ConditionService#getConditionsByEncounter(Encounter)
 	 */
 	List<Condition> getConditionsByEncounter(Encounter encounter) throws APIException;
 
 	/**
	 * Gets a condition by id
 	 *
	 * @param conditionId the id of the condition to return
	 * @return the condition associated with the id
 	 */
	Condition getCondition(Integer conditionId);
 	
 	/**
 	 * Removes a condition from the database