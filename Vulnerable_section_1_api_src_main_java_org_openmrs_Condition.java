  */
 package org.openmrs;
 
import java.util.Date;
import java.util.Objects;

 import javax.persistence.AssociationOverride;
 import javax.persistence.AssociationOverrides;
 import javax.persistence.AttributeOverride;
 import javax.persistence.Table;
 import javax.persistence.Transient;
 
 /**
  * The condition class records detailed information about a condition, problem, diagnosis, or other
  * situation or issue. This records information about a disease/illness identified from diagnosis or
 	public void setEncounter(Encounter encounter) {
 		this.encounter = encounter;
 	}
			
 }