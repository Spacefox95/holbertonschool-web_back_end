function hasValuesFromArray(set, arr) {
  return arr.every((lambda) => set.has(lambda));
}
export default hasValuesFromArray;
