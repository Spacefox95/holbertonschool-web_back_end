export default function createEmployeesObject(departmentName, employees) {
  const newArray = {};
  newArray[departmentName] = employees;
  return newArray;
}
