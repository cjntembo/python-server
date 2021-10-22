class Employee():

    def __init__(self, id, name, locationId, manager, fullTime, hourlyRate):
      self.id = id
      self.name = name
      self.locationId = locationId
      self.manager = manager
      self.fullTime = fullTime
      self.hourlyRate = hourlyRate

new_employee = Employee(1, "Steve", 1, "no", "yes", "19.23")
