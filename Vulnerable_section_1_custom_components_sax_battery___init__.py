                 }
 
                 # Initialize last update times for this battery's registers
                self.last_updates[battery_id] = dict.fromkeys(self.modbus_registers[battery_id], 0)
 
                 self.batteries[battery_id] = SAXBattery(self.hass, self, battery_id)
                 await self.batteries[battery_id].async_init()