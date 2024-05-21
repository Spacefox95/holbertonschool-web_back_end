function getStudentByLocation(listofstudent, city) {
  return listofstudent.filter((student) => student.location === city);
}
export default getStudentByLocation;
