function getListStudentIds(studentarray) {
  if (!Array.isArray(studentarray)) {
    return [];
  }
  return studentarray.map((lambda) => lambda.id);
}
export default getListStudentIds;
