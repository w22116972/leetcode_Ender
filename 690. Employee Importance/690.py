
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    # [Accepted]
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        total = 0
        id_to_employee = {employee.id: employee for employee in employees}
        queue = [id_to_employee[id]]
        while queue:
            current_employee = queue.pop(0)
            total += current_employee.importance
            if current_employee.subordinates:
                for sub_id in current_employee.subordinates:
                    queue.append(id_to_employee[sub_id])
        return total