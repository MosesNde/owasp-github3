 import java.time.LocalDateTime;
 import java.util.ArrayList;
 import java.util.List;
 import java.util.UUID;
 
 @Service
         Airport origin = airportServ.findById(dto.getOriginAirportID());
         Airport destiny = airportServ.findById(dto.getDestinyAirportID());
 
        List<Ticket> ticketInDB = ticketServ.findByScheduleBetween(dto.getSchedule(), dto.getSchedule());
 
        ticketInDB.forEach(ticket -> {
            if (ticket.getAirplaneID().equals(dto.getAirplaneID()) && ticket.getSchedule().equals(dto.getSchedule()) && ticket.getSeat() == dto.getSeat()){
                throw new ExistingObjectException();
            }
        });
 
         double ticketPrice = PriceGenerator.calc(origin.getLatitude(), origin.getLongitude(), destiny.getLatitude(), destiny.getLongitude());
 
         Ticket ticket  = Ticket.builder()
                .airplane(airplane)
                 .airlineName(airplane.getAirlineName())
                 .origin(origin.getCity())
                 .originAirport(origin)
                .originAirportID(UUID.fromString(String.valueOf(dto.getOriginAirportID())))
                 .destiny(destiny.getCity())
                 .destinyAirport(destiny)
                 .destinyAirportID(dto.getDestinyAirportID())
         if (!(dto.getPrice()<1)){
             ticket.setPrice(dto.getPrice());
         }
        if (dto.getSchedule() != null && !dto.getSchedule().isAfter(LocalDateTime.now())){
             ticket.setSchedule(dto.getSchedule());
         }
         if (!(dto.getSeat()<0)){