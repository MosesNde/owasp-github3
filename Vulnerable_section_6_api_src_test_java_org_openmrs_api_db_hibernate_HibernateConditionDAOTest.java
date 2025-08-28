 	}
 	
 	@Test
	public void shouldGetConditionHistory() {
 		Patient patient = new Patient(2);
		List<Condition> history = dao.getConditionHistory(patient);
 		
		assertEquals(3, history.size());
 	}
 	
 	@Test