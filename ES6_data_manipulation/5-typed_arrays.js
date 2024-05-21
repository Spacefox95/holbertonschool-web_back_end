function createInt8TypedArray(lenght, position, value) {
  const buffer = new ArrayBuffer(lenght);
  const view = new Int8Array(buffer);
  if (position < 0 || position >= lenght) {
    throw new Error('Position outside range');
  }
  view[position] = value;
  return buffer;
}
export default createInt8TypedArray;
