export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getters
  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  // Setters
  set name(NewName) {
    if (typeof NewName === 'string') {
      this._name = NewName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  set length(newLength) {
    if (typeof newLength === 'number') {
      this._length = newLength;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  set students(NewStudent) {
    if (Array.isArray(NewStudent) && NewStudent.every((item) => typeof item === 'string')) {
      this._students = NewStudent;
    } else {
      throw new TypeError('Students must be an array of string');
    }
  }
}
