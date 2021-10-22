EMPLOYEES = [
    {
      "id": 2,
      "name": "Sarah Smith",
      "locationId": 1,
      "manager": "yes",
      "fullTime": "yes",
      "hourlyRate": "17.95"
    },
    {
      "id": 3,
      "name": "Mathew Johns",
      "locationId": 1,
      "manager": "no",
      "fullTime": "no",
      "hourlyRate": "11.50"
    },
    {
      "id": 4,
      "name": "Caroline Dubey",
      "locationId": 2,
      "manager": "no",
      "fullTime": "yes",
      "hourlyRate": "12.80"
    },
    {
      "name": "joker",
      "locationId": 1,
      "manager": "no",
      "fullTime": "no",
      "hourlyRate": "11.50",
      "id": 5
    },
    {
      "name": "Johnny Dash",
      "locationId": 1,
      "manager": "no",
      "fullTime": "no",
      "hourlyRate": "11.50",
      "id": 6
    },
    {
      "name": "Carter",
      "locationId": 1,
      "manager": "true",
      "fullTime": "no",
      "hourlyRate": "11.55",
      "id": 7
    }
  ]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)