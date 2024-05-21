function getStudentIdsSum(listofstudents) {
  return listofstudents.reduce((accumulator, current) => accumulator + current.id, 0);
}
export default getStudentIdsSum;
