export default function concatArrays(array1, array2, string) {
  const array = [...array1, ...array2, ...string];
  return array;
}
