     List<Ticket> findByDestinyAirportID(UUID airportID);
     @Query("MATCH (a:flight_ticket) WHERE a.airplaneID=$airplaneID AND a.seat=$seat RETURN a")
     Optional<Ticket> findByAirplaneIDAndSeat(UUID airplaneID, int seat);
 }