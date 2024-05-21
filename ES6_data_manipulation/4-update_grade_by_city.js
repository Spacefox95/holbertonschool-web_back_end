function updateStudentGradeByCity(listofstudents, city, newGrades) {
  return listofstudents
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeexist = newGrades.find((grade) => grade.studentId === student.id);
      const grade = gradeexist ? gradeexist.grade : 'N/A';
      return { ...student, grade };
    });
}
export default updateStudentGradeByCity;
