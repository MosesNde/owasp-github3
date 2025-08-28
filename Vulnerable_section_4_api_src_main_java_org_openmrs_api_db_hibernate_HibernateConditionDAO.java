 
 import java.util.List;
 
import org.hibernate.Query;
 import org.hibernate.SessionFactory;
 import org.openmrs.Condition;
 import org.openmrs.Encounter;
 		this.sessionFactory = sessionFactory;
 	}
 	
	/**
	 * Saves the condition.
	 *
	 * @param condition the condition to save.
	 * @return the saved condition.
	 */
	@Override
	public Condition saveCondition(Condition condition) {
		sessionFactory.getCurrentSession().saveOrUpdate(condition);
		return condition;
	}
	
 	/**
 	 * Gets the condition with the specified id.
 	 *
 	 */
 	@Override
 	public Condition getCondition(Integer conditionId) {
		return (Condition) sessionFactory.getCurrentSession().get(Condition.class, conditionId);
 	}
 	
 	/**
 	 */
 	@Override
 	public Condition getConditionByUuid(String uuid) {
		return (Condition) sessionFactory.getCurrentSession().createQuery("from Condition c where c.uuid = :uuid")
				.setString("uuid", uuid).uniqueResult();
 	}
	
 	/**
	 * Gets all conditions related to the specified patient.
	 *
	 * @param patient the patient whose condition history is being queried.
	 * @return all active and non active conditions related to the specified patient.
 	 */
 	@Override
	public List<Condition> getConditionHistory(Patient patient) {
		Query query = sessionFactory.getCurrentSession().createQuery(
				"from Condition con where con.patient.patientId = :patientId and con.voided = false " +
						"order by con.onsetDate desc");
		query.setInteger("patientId", patient.getId());
 		return query.list();
 	}
 	
 	 */
 	@Override
 	public List<Condition> getActiveConditions(Patient patient) {
		Query query = sessionFactory.getCurrentSession().createQuery(
				"from Condition c where c.patient.patientId = :patientId and c.voided = false and c.endDate is null order "
						+ "by c.onsetDate desc");
		query.setInteger("patientId", patient.getId());
 		return query.list();
 	}
 
 	/**
	 * @see ConditionService#getAllConditions(Patient)
 	 */
 	@Override
 	public List<Condition> getAllConditions(Patient patient) {
		return this.getConditionHistory(patient);
 	}
 	
 	/**
 	}
 
 	/**
	 * @see ConditionService#getConditionsByEncounter(Encounter)
 	 */
 	@Override
	public List<Condition> getConditionsByEncounter(Encounter encounter) throws APIException {
		Query query = sessionFactory.getCurrentSession().createQuery(
				"from Condition c where c.encounter.encounterId = :encounterId and c.voided = false order "
						+ "by c.onsetDate desc");
		query.setInteger("encounterId", encounter.getId());
		return query.list();
 	}
 }