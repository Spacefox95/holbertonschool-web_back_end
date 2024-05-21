function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  const dv1 = new DataView(buffer);
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  view[position] = value;
  return dv1;
}
export default createInt8TypedArray;
